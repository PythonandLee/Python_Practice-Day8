class User():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.first_name.title() + ", you are logging.")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + 
          self.last_name.title() + ".")
          
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login: " + str(self.login_attempts))
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login: " + str(self.login_attempts))

        
user_a = User('dan', 'joey')
user_a.describe_user()
user_a.greet_user()

user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.reset_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.reset_login_attempts()

