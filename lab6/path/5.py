f = open("hello.txt", "a")
lst = ["yeah im a list"]
f.write(f"\nnow u have list {lst}")
f.close()

f = open("hello.txt", "r")
lines = f.readlines()
f.close()

f = open("hello.txt", 'r')
print (f.read())