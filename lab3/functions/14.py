from math import pi
from itertools import permutations

def sphere_volume(r):
    return (4/3) * pi * r**3

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for n in lst:
        print("*" * n)

def reverse_sentence(s):
    return " ".join(s.split()[::-1])

def permute(s):
    for p in permutations(s):
        print("".join(p))

if __name__ == "__main__":
    print("Sphere volume with radius 3:", sphere_volume(3))
    print("Is 'madam' palindrome?", is_palindrome("madam"))
    print("Reversed sentence:", reverse_sentence("We are ready"))
    print("Histogram of [3,5,2]:")
    histogram([3,5,2])
    print("Permutations of 'abc':")
    permute("abc")