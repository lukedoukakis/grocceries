from django.db import models

# Create your models here.




# ------------------------------------------------------
# NOTES FOR USING THE TABLES IN A PYTHON SCRIPT OR SHELL

# create item and save to the database:
# item = <ModelName>(<parameters>)
# item.save()

# get item from database:
# <ModelName>.objects.get(id=<id of object>)

# get all results in a database (returns QuerySet):
# <ModelName>.objects.all()
# ------------------------------------------------------

class Address(models.Model):
    email = models.CharField(max_length=255)        # pk
    value = models.CharField(max_length=255)

    # set id to email
    def __str__(self):
        return self.email


class Account(models.Model):
    email = models.CharField(max_length=255)        # pk
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    
    # set id to email
    def __str__(self):
        return self.email


# represents a table
class Test(models.Model):

    # fields/columns for the table
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    # specifies that the id of an entry will be its number (optional)
    def __str__(self):
        return self.text


# this one takes an entry from another table as a field
class ForeignKeyExample(models.Model):
    name = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.name