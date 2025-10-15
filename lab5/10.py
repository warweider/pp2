import re

with open("a.txt", "r") as f:
    text = f.read().strip()

def camel_to_snake(s):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()

snake_text = camel_to_snake(text)

print(snake_text)
