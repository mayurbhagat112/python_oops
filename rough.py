lst=[1,2,3]   #random data structure in python such as list,dic,set,str are class
my_str="mlops"
my_int=122

#print(type(my_int))
#lst.clear()
#my_str=my_str.capitalize()
#print(my_str)

#="x"
#="y"
#rint(a+b)

#x+y)
#y

from oops_pro import chatbook

#user=chatbook()

#lst=[1,2,3]
#function

#a1=len(lst)

#print(a1)
#method
user1=chatbook()
#user1.sendmsg()

#print(user1._chatbook__name)

#getter and setter
#print(user1.get_name())
#user1.set_name("agent x")
#print(user1.get_name())

print(user1.id)

chatbook.set_id(10)
user2=chatbook()
print(user2.id)

#using static method directly from class rather than object
user3=chatbook()
print(user3.id)