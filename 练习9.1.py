class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"restaurant type is {self.cuisine_type}")
    def open_restaurant(self):
        print("restaurant is open now")
    def icecream_describe(self):
        print("we have those flavour icecreams in our restaurant:")
        for i in self.flavors:
            print(i)
p=Restaurant('Kfc','Western style food')
p.describe_restaurant()
p.open_restaurant()