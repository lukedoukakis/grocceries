window.onload = function() {
    console.log(7);
    readCookie();
    makeCookie();
};

function makeCookie()
{
    document.cookie = "username=John Doe";
}

function readCookie()
{
    var x = document.cookie;
    console.log(x);
}