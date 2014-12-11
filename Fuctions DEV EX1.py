#Sean Nicholls
#02/12/14
#Functions DEV EX1

def get_hours():
    hours = int(input("How many hours?: "))
    return hours

def get_mins():
    mins = int(input("How many minutes?: "))
    return mins

def get_seconds():
    seconds = int(input("How many seconds?: "))
    return seconds

def total_seconds(hours, mins, seconds):
    secondshours = (hours*60)*60
    secondsmins = (mins*60)
    totalseconds = (secondshours+secondsmins+seconds)
    print("In this amount of time there is {0} seconds".format(totalseconds))

def run_program():
    hours = get_hours()
    mins = get_mins()
    seconds = get_seconds()
    total_seconds(hours, mins, seconds)

#main program

run_program()
