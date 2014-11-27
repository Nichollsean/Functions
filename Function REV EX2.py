#Sean Nicholls
#27/11/14
#Functions REV EX2

def user_number():
    num1 = int(input("Please enter an odd number: "))
    if num1%2 ==0:
        print("This number is even try again")
    else:
        print("This is correct, your pyramid will be created")
    return num1

def create_pyramid(num1):
    for count in range(num1, 0, -2):
        print(num1*("*"))
        num1 = (num1-2)
        

create_pyramid(5)
