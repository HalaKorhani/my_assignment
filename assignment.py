# ex1
age =int(input("enter your age "))
if age<18:
    print("the ticket price is 5$")
elif age <=40:
    print("the ticket price is 10$")
else:
    print("the ticket is 15$ ")


# ex2
number =int(input("Enter a number "))
if number%2==0:
    print("the number is even ")
else:
    print("the number is odd")

# ex3

username=input("Enter your username ")
password=input("enter your password")

if username=="admin" and password=="1234" :
   print("granted")
else:
    print("denied")
