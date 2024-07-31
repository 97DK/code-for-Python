class User:
    def __init__(self,first_name,last_name,age,city,frequency):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.city=city
        self.login_attempts=int(frequency)
    def describe(self):
        print(f"{self.first_name} {self.last_name} is {self.age},from {self.city}")
    def greet(self):
        print(f"{self.first_name} {self.last_name} how are you?")
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"登录次数是{self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts =0
        print(f"登录次数是{self.login_attempts}")
p=User('zhang','zhang','18','guangzhou','25')
p.describe()
p.increment_login_attempts()
p.increment_login_attempts()
p.reset_login_attempts()