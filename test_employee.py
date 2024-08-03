from employee_functions import Employee
def test_give_default_raise():
    emp = Employee("John", "Doe", 50000)
    emp.give_raise()  # 默认增加 5000 美元
    assert emp.salary == 55000
def test_give_custom_raise():
    emp = Employee("Jane", "Smith", 60000)
    emp.give_raise(10000)  # 自定义增加 10000 美元
    assert emp.salary == 70000
