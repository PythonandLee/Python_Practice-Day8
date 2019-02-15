# Use 'class' and gieve definitions. 
# Use 'self.valuations' to set values in '__init__'.

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("\nThe name of this restaurant is " + 
          self.restaurant_name.title() + ".")
        print("Their classic cuisine is " + self.cuisine_type.title() + ".")
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is still opening.")
        
restaurant_a = Restaurant('cooking chief', 'crab cake')
restaurant_a.describe_restaurant()
restaurant_a.open_restaurant()

restaurant_b = Restaurant("david's", 'italian')
restaurant_b.describe_restaurant()
restaurant_b.open_restaurant()