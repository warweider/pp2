import re

with open("a.txt", "r") as f:
    text = f.read()

pattern = r'a.*b'
matches = re.findall(pattern, text)

print(matches)
