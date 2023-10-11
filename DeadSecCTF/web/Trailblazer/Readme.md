# Overview
I didn't manage to solve this challenge, but i'm kinda close to solve it.

This is a RCE challenge written in python.

The website is simple, we can found a image in the 404 error page.
The image lead to a url "/now".

# Solution
We can confirm this page is written in python by checking the header.
The url returns a datetime image is "/now".
The datetime format looks really familiar, after some testing, I confirm it's a function under `datetime` module in python.

My exploit cannot succeed because the python version is probably different, and I forgot that.
But after reading other's write-ups, I found a interesting behavior in python

The server probably `eval()` the code in a if or a function, so it's really easy to break the code and get nothing.
At first I thought it was executed by some kind of method caller, so we can't execute arbitrary code.

But it turns out I was wrong and this is probably the real scenario:
```python
eval(f"something({URL_LOCATION}())")
```

So if we supply a '#' at the end it will break.
But this syntax will not break and only get a warning:
```
print(123) and 1()
```
The above code will print "123" and will not raise a error, because the `1()` isn't actually executed.

Therefore, we can do that in this challenge and run this to run arbitrary code:
```
http://chall.com/images/print(123)%20and%201
```

Inspired by: https://blog.westernsecurity.ie/2023/05/21/Deadsec-Trailblazer.html