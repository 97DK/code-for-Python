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
admin = Admin("John", "Doe")
admin.show_privileges(admin.first_name, admin.last_name)
