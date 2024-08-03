class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount  # 直接更新实例的 salary 属性
        print(f"{self.first_name} {self.last_name} 的年薪增加了 {amount} 美元，现在年薪为 {self.salary} 美元。")


