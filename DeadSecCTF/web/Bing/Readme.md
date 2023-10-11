# Overview
This is a command injection challenge with lots of annoying filter.

# Solution
This is a blackbox challenge, so I spent some time fuzzing the filter.
It turned out the command input cannot contain `cat`, space, `flag.txt` and some other things.

Also the output is filtered if the result contains "dead", so we can't get the flag "dead{xxx}" directly.

Anyway, the special characters are allowed, so I tried using `${IFS}` as space to bypass the filter, and it worked.
But that's not enough to retrieve the flag, since we still need to get the content of the flag, we probably need `cat` or something.

I used a interesting method to bypass the blacklist, the "${cmd}" syntax in bash will return those outputs which aren't errors.
So if we just make a error, we can split the command string without interrupting the command execution.

My payload:
```bash
ca${asd}t${IFS}/fl${asd}ag.txt|base64
```
