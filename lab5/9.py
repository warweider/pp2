import re

with open("a.txt", "r") as f:
    text = f.read().strip()

result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

print(result)
