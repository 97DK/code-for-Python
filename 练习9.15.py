from random import randint, choice
prize_s=[]
prize=['s','6','3','8','t','c','e','g','2','1']
print("if your lottery ticket include those ,you will get big prize:")
for i in range(1,5):
    prize_s.append(choice(prize))
print(prize_s)
my_s=[]
a=0
while 1:
    for i in range(1, 5):
        my_s.append(choice(prize))
        a=a+1
    if my_s==prize_s:
        print(my_s)
        print("You get big prize")
        print(f"抽中一共花了{a}次")
        break
    else:
        my_s = []
