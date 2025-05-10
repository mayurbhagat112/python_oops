#initiate a class
class empolyee:
     #special method/magic method/dunder method-constructor
     def __init__(self):
          print("started executing attributes/data")
          self.id=123
          self.salary=5000
          self.designation="DS"
          print("attributes/data have been initiated")

     def travel(self,desitnation):
          print("this travel method was called manually ")
          print(f"empolyee is now travelling to {desitnation}")
    
#create an obj/instance of the class
sam=empolyee()

#printing the attributes
# print(sam.id)

#calling a method
#sam.travel("nagpur")
print(type(sam))