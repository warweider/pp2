import re

with open("a.txt", "r") as f:
    text = f.read()

pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, text)

print(matches)

