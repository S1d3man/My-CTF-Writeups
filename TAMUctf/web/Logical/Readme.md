# Overview
A SQLi challenge, but I failed at final step.

# Solution
I failed because I used "_" in the `like` field, and since "_" is the wildcard char, I retrieved the wrong flag.
Next time I should put _ to the last, or simply use `substr` to retrieve specific character.