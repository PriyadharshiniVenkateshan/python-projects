adult_no=int(input("count of adult:"))
child_no=int(input("count of child:"))
num_person=adult_no+child_no
print("total number of person: ",num_person)
user_input=input("enter the place:")
if user_input == "goa":
    adult,child = (1000,1000/2)
elif user_input == "manali":
    adult,child = (2000,2000/2)
elif user_input == "shimla":
    adult,child = (3000,3000/2)
elif user_input == "kashmir":
    adult,child = (5000,5000/2)
else:
    print("not available")
print("The amount per head adult is :",adult)
print("The amount per head child is :",child)
totalcost=(adult_no*adult)+(child_no*child)
print("total amount of tikects:",totalcost)
