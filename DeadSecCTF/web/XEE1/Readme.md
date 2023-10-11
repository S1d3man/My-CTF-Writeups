# Overview
This is a XXE challenge, but the output is filtered if it contains the flag.

We can simply send XML data to XXE.

# Solution
If we use simple XXE: `file:///flag.txt` -> `<msg>You can't read the flag</msg>`
But since the page is php, we can actually try using `php://filter` to do this.
And if we use php filter to encode the output to base64, we can retrieve the flag:
```
php://filter/convert.base64-encode/resource=/flag.txt
```