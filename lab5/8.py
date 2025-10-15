import re

with open("a.txt", "r") as f:
    text = f.read().strip()

parts = re.findall(r'[A-Z][^A-Z]*', text)

print(parts)
