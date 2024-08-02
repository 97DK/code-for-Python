print("Please input tow digit:")
try:
    a = int(input("a:"))
    b = int(input("b:"))
except ValueError:
    print("Please input digit not string!")
else:
    print(f"the sum of 'a'+'b' is {a+b}")