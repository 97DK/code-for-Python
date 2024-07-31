class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.flavors=['apple_icecream','banana_icecream','strawberry_icecream']
    def describe_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"restaurant type is {self.cuisine_type}")
    def open_restaurant(self):
        print("restaurant is open now")
    def icecream_describe(self):
        print("we have those flavour icecreams in our restaurant:")
        for i in self.flavors:
            print(i)
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.flavors=['apple_icecream','banana_icecream','strawberry_icecream']
        super().__init__(name,type)
flavour=IceCreamStand('sweet','desert')
flavour.icecream_describe()
