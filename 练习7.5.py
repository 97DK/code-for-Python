age=int(input("Please input your age, stop when you input 'age<=0':"))
while 1 :
    if age <= 0:
        break
    elif age < 3:
        print("You are free")
    elif 3 <= age < 12:
        print("You should pay 10 dollars for the ticket")
    elif 12 <= age:
        print("You should pay 15 dollors for the ticket")
    age = int(input("Please input your age, stop when you input 'age<=0':"))