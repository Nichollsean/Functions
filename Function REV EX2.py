
#Sean Nicholls
#27/11/14
#Functions REV EX2



def user_number():
    num1 = int(input("Please enter an odd number: "))
    if num1%2 ==0:
        print("This number is even try again")
    else:
        print("This is correct, your pyramid will be created :) ")
    return num1

def create_pyramid(num1):
    center = num1
    
    for count in range(num1, 0, -2):
        stars =(num1*("*"))
        print("{0:^{1}}".format(stars, center))
        num1 = (num1-2)
    print("Here is a lovely pyramid, have a merry christmas :) ")
def run_program():
    num1 = user_number()
    create_pyramid(num1)
        

run_program()

