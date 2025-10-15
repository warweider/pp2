import re

with open("a.txt", "r") as f:
    text = f.read()

pattern = r'ab{2,3}'
matches = re.findall(pattern, text)


print(matches)

