class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served=0
    def describe_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"restaurant type is {self.cuisine_type}")
        print(f"have {self.number_served} people was served in this restaurant")
    def open_restaurant(self):
        print("restaurant is open now")