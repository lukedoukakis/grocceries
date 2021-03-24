from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from myapp.models import ShoppingCart, Address, Order
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone

#
class AccountManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password, phone=None):
        if not email:
            raise ValueError('Accounts must have an email address')
        if not username:
            raise ValueError('Accounts must have a username')
        if not first_name:
            raise ValueError('Accounts must have a first name')
        if not last_name:
            raise ValueError('Accounts must have a last name')
        if not password:
            raise ValueError('Accounts must have a password')

        account = self.model(
            username=username,
            password=password,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )

        account.set_password(password)

        account.save(using=self._db)
        return account

    def create_superuser(self, username, email, password):
        if not username:
            raise ValueError('Superusers must have a username')
        if not password:
            raise ValueError('Superusers must have a password')
        if not email:
            raise ValueError('Superusers must have an email')

        account = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True

        account.set_password(password)
        account.save(using=self._db)
        return account


# Create your models here.
class Account(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username            = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name          = models.CharField(_('first name'), max_length=150)
    last_name           = models.CharField(_('last name'), max_length=150)
    email               = models.EmailField(_('email address'), unique=True)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_admin            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    last_login          = models.DateTimeField(_('last login'), auto_now=True)
    date_joined         = models.DateTimeField(_('date joined'), default=timezone.now)
    phone               = PhoneNumberField(null=True, blank=True, unique=True)
    shoppingCart        = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE, null=True)
    address             = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    is_driver           = models.BooleanField(default=False)


    # foreign key = one-to-many 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['email']

    objects = AccountManager()

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


    def __str__(self):
        return self.username

# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,
#                                 null=True, unique=True)
#     phone = PhoneNumberField(null=True, blank=False, unique=True)
#     shoppingCart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE, null=True)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
#     is_driver = models.BooleanField(default=False)
#     # one to many//an account can have many orders
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
#     def __str__(self):
#         return self.user.__str__()