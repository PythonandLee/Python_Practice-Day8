# Use 'class' and gieve definitions. 
# Use 'self.valuations' to set values in '__init__'.

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

        
    def describe_restaurant(self):
        print("\nThe name of this restaurant is " + 
          self.restaurant_name.title() + ".")
        print("Their classic cuisine is " + self.cuisine_type.title() + ".")
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is still opening.")
        
    def served_number(self):
        print("It has already " + str(self.number_served) + 
          " people been here.")
          
    def set_number_served(self, new_set):
        self.number_served = new_set       
        
restaurant_a = Restaurant('cooking chief', 'crab cake')
restaurant_a.describe_restaurant()
restaurant_a.open_restaurant()

restaurant_a.number_served = 200
restaurant_a.served_number()
restaurant_a.set_number_served(400)
restaurant_a.served_number()