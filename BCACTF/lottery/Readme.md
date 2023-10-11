# Overview
This challenge requires us to bypass the random checking mechanism to get the flag.

The code generates random six times for you, and if any of those is the same as the lottery, we win.

# Solution
The code has misused comparison and nullable type, so we can bypass the check if we just don't send anything.
It's because if you try to access a non-exist attribute of nullable variable, it just become undefined.
So according to this part of the source code:
```javascript
const winner = cry.randomBytes(111).toString('hex');
  if (req.data?.tickets?.indexOf(winner) != -1) {
    res.render("gamble.ejs", {msg: `Congrats! The flag is ${fs.readFileSync("flag.txt", "utf8")}.` });
  } else {
    res.render("gamble.ejs", {msg: "Nope. Better luck next time..."});
  }
```
If our data doesn't have "tickets", it just become `undefined` and bypass the check since it's not equal to `-1`.