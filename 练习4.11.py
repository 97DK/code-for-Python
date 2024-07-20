my_pizza=['liulian pizza','turkey pizza','typical pizza']
friend_pizza=my_pizza[0:]
my_pizza.append('milk pizza')
friend_pizza.append("banana pizza")
print("My favorite pizzas are:")
for i in my_pizza:
    print(i,end=",")
print("My friend's favorite pizzas are:")
for i in friend_pizza:
    print(i,end=",")