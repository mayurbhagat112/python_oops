#initiate a class
class empolyee:
     #special method/magic method/dunder method-constructor
     def __init__(self):
         #print(id(self))
          #print("started executing attributes/data")
          self.id=123
          self.salary=5000
          self.designation="DS"
         #print("attributes/data have been initiated")

     def travel(self):
          print("this travel method was called manually ")
          print(f"empolyee is now travelling to mumbai")
    
#create an obj/instance of the class
sam=empolyee()
sam.name=" sam kumar"
shaktiman=empolyee()
print(sam.name)
print(id(sam))
print(id(shaktiman))

#printing the attributes
# print(sam.id)

#calling a method
#sam.travel()  #object vo default argument method access class object then called self
#print(type(sam))