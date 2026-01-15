import re

str = "an example word:cat!!"
match = re.search(r"word:\w\w", str)

print(match.group())
