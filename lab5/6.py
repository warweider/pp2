import re

with open("a.txt", "r") as f:
    text = f.read()

result = re.sub(r"[ ,.]", ":", text)

print(result)
