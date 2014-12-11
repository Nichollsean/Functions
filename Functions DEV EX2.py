#Sean Nicholls
#04/12/14
#Functions DEV EX2

def user_number():
    num1 = int(input("Please enter an odd number: "))
    if num1%2 ==0:
        print("This number is even try again")
    else:
        print("This is correct, your diamond will be created :) ")
        create_diamond
    
def create_pyramid(start,stop,step):
    if step >0:
        center = stop
    else:
        center = start
    for count in range(start, stop, step):
        stars = count*"*"
        print("{0:^{1}}".format(stars, center))        
    
def create_diamond








def run_program():
    num1 = user_number()
    
create_pyramid(1,6,2)
print("Here is a lovely pyramid, have a merry christmas :) ")
