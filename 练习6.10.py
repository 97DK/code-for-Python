prefer_digit={'Tom':['7','5','8'],
              'Jack':['5','6'],
              'jenny':['1','6','9'],
              'Timi':['1'],
              'joke':['8']
}
for name,digit in prefer_digit.items():
    print(f"{name} favorite digit are:")
    if len(digit)!=1:
        for i in digit:
            print(i)
    else:
        print(digit[0])