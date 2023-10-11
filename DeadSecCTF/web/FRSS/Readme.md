# Overview
SSRF simple filter bypass challenge

The page has a input for us to send http request.

Source code
```php
$x = curl_init($url);
curl_setopt($x, CURLOPT_REDIR_PROTOCOLS, CURLPROTO_HTTP);
curl_setopt($x, CURLOPT_PROTOCOLS, CURLPROTO_HTTP);
curl_setopt($x, CURLOPT_MAXREDIRS, 1);

echo curl_exec($x);
```

# Solution

Website seems to restict the url length. Also, it says flag is in hehe.txt.
The web server denied all `/*.txt` access attempts, so the flag is probably here.

There is a filter in the source code, but the challenge didn't give it to us.
The filter is not a keyword filter, instead, it's a length filter, so we have to try to reduce the url length to minimum or we'll get an error 'Oh no no, url is too long I can't handle it'.

Tried url:
```
localhost/hehe.txt => 18
127.0.0.1/hehe.txt => 18
0/hehe.txt => bad request
0.0.0.0/hehe.txt => 16 => Get Flag
```


dead{Ashiiiibaaa_you_hAv3_Pybass_chA11}