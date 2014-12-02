#Sean Nicholls
#02/12/14
#Functions REV EX4


def get_temp_fahrenheit():
    temp = int(input("What is the temperature in Fahrenheit?: "))
    return temp

def create_celsius(temp):
    celsius = (temp-32) * (5/9)
    celsiusround = round(celsius)
    print("The temperature in celsius is {0}".format(celsiusround))

def run_program():
    temp = get_temp_fahrenheit()
    create_celsius(temp)

#main program


run_program()
        
