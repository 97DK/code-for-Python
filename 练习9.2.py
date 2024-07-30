class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"restaurant type is {self.cuisine_type}")
    def open_restaurant(self):
        print("restaurant is open now")
restaurant=Restaurant('Taste','xiangcai')
restaurant.describe_restaurant()
restaurant.open_restaurant()
p=Restaurant('KFC','Western-style food')
p.open_restaurant()
