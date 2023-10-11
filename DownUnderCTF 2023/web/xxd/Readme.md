# Overview
This is a file uploading challenge with length restriction.
The server will hexdump your uploaded file and and ceate a page to render it.

# Solution

There is a length limit here because the hexdump will append a new line after 16 bytes, which will cause the php syntax to break.
So, we need to run php in 16 chars.
We can utilize php echo shorthand to achieve this.

```php
<?=`cat /flag`?>
```

This equals to `<?php echo `cat /flag`?>`
We don't need ";" since this is the last line of code.
And this payload is exactly 16 chars long.