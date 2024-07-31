class User:
    def __init__(self,first_name,last_name,age,city,frequency):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.city=city
        self.login_attempts=int(frequency)
        self.privileges=["can add post","can delete post","can ban user"]
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
    def show_privileges(self):
        print(f'Dear {self.first_name} {self.last_name} You can do:')
        for i in self.privileges:
            print(i)

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self, first_name, last_name):
        print(f'Dear {first_name} {last_name}, You can do:')
        for privilege in self.privileges:
            print(privilege)

class Admin(Privileges):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name