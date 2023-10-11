# Overview
This is a path traversal challenge, the code is quite unclear.

There are several functions in the server:
1. readletter: read the file in the server.
2. hacking: this can help rename letter or reset letter storage.

# Solution
The file reading function is vulnerable to path traversal since it doesn't sanitize the input.

Initially, the letter is created and uses a hash a lettername.
But we can rename it later with hacking function, and it can be any string we want.

So we can just change the letter name to `../../../../../../flag.txt` to read the flag.

