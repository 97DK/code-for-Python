class User:
    def __init__(self,first_name,last_name,age,city):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.city=city
    def describe(self):
        print(f"{self.first_name} {self.last_name} is {self.age},from {self.city}")
    def greet(self):
        print(f"{self.first_name} {self.last_name} how are you?")
p=User('zhang','zhang','18','guangzhou')
p.describe()
p.greet()