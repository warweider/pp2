a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello"
b = "World"
c = a + " " + b
print(c)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)