#Sean Nicholls
#Lists HWK

def table(end,name1,name2,name3,name4,name5,name6,name7,name8):   
    Students = [end,name1,name2,name3,name4,name5,name6,name7,name8]
    count = (0)
    for each in Students:
        print("{0}. {1}".format(count, each))
        count = count+(1)
def new_table(Students):
    count = (0)
    for each in Students:
        print("{0}. {1}".format(count, each))
        count = count+(1)
    
#mainprogram
end = ("End program")
name1 = input("Please enter the name of the first student: ")
name2 = input("Please enter the name of the second student: ")
name3 = input("Please enter the name of the third student: ")
name4 = input("Please enter the name of the fourth student: ")
name5 = input("Please enter the name of the fifth student: ")
name6 = input("Please enter the name of the sixth student: ")
name7 = input("Please enter the name of the seventh student: ")
name8 = input("Please enter the name of the eighth student: ")

table(end,name1,name2,name3,name4,name5,name6,name7,name8)

Students = [end,name1,name2,name3,name4,name5,name6,name7,name8]

selection = int(input("Please select a student to edit: "))
if selection == 0:
    print("Program Ended")
else:
    nameselected = Students[selection]
    Students.pop(selection)
    print("You have selected {0}".format(nameselected))
    newname = input("Please enter the students new name: ")
    re_enter = selection 
    Students.insert(re_enter, (newname))
    new_table(Students)
