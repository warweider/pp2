import re

with open("a.txt", "r") as f:
    text = f.read()
text = "ac ab a abb abbb axyz"

pattern = r'ab*'
matches = re.findall(pattern, text)

print("Matches:", matches)