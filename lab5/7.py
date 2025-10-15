with open("a.txt", "r") as f:
    text = f.read().strip()

def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.title() for word in parts[1:])

camel_text = snake_to_camel(text)

print(camel_text)
