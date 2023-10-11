# Overview
This is a interesting django misconfiguration challenge.
2 misconfigurations in total.

# Solution
The primary goal is to bypass 403 and login to admin panel to grab the flag, but we can't simply access it, since we don't have credential, and there' IP restriction.

The problem in the configuration is located in django's url.py.

Nginx will deny every "/admin" request if you're not localhost.
But in django config, it uses `re_path('admin/')` to create a route for admin panel, this regex didn't specified that the request url has to start with "/admin".

Therefore, if we use something like this: "/api/admin", we can bypass 403.
"/api" and "/admin" will both be proxied to django, but only "/admin" will check the IP.

Then, we have to get the credential.
The site has a article query APi made with Django Rest Framework.
And in the given source code, we know that we can inject any query we want into Article searching, not sure if this is some kind of SQL Injection lol.

Django filter can use something called "field lookup", it's some kind of syntax that you can query some object attributes with specified condition.
Normally, this is to search something like "username starts with 'H'", and the syntax will be: `{"username__startswith": "H"}`.
And actually, this feature can be used to query foreign key attributes!
The article table has a foreign key "created_by", and that is the "User" model.

We can use this injection to perform a boolean-based Django filter injection to leak the user's password hash! (username is already in article)
And the challenge hint tells us we need to crack the hash to retrieve the password, it turns out the password is "shrekndonkey".

Then, I login to the panel with "/api/admin/login" and access grab the flag in the Flag table.

DUCTF{oRm_i_g0oF3d_uP_m1_r3lAsHunSh1p5!}

{% note %}
In this challenge, I also knew how nginx proxy works in some way.
It seems that nginx will url-decode once, and then proxy the request to upstream server.
Because we can actually use "/api%252F%252E%252E%252Fadmin" to access the admin page in Django, it will redirect us to "/admin/login/?next={triple url-encoded path}".
But I don't know why, if I use that method to access "/api%252F%252E%252E%252Fadmin%252Flogin", it will return a 404.
Might have to dig into this to find out what happend.
{% endnote %}