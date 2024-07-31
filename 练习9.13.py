from random import randint
class Die:
    def __init__(self,sides='6'):
        self.sides=sides
    def roll_die(self):
        print(f"将会投掷骰子{self.sides}次,结果分别为：")
        for i in range (1,int(self.sides)+1):
            print(randint(1,6))
p=Die('10')
p.roll_die()