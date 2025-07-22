# Creating Classes
class User:
    def __init__(self):
        print("Print this.....")

user_1=User()
user_1.id="001"
user_1.username="sarath"

user_2=User()
user_2.id="002"
user_2.username="kj"

#####################

class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        self.followers=0
    
car_1=Car("Benz","Mercedez")
car_2=Car("Chiron","Bugati")
print(car_1.name)
print(car_1.followers)

#######################
class instagram:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1

user_1=instagram("01","Sarath")
user_2=instagram("02","Bharath")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



        
        

## constructor
# is a part of blueprint that allows us to specify what should happen when an object is being constructed
# used to initialize an object
# using init function to initialize the attributes
# self inside an init is the actual object that is being created or being initialized

