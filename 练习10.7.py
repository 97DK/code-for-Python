print("Please input tow digit:")
while 1:
    try:
        a = int(input("a:"))
        b = int(input("b:"))
    except ValueError:
        print("Please input digit not string!")
        continue
    else:
        print(f"the sum of 'a'+'b' is {a + b}")
        break
