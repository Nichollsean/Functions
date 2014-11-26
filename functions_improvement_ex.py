# functions improvement exercise
# times-table tester
import random

def user_answer(Num1,Num2):
    UserAnswer = int(input(str(Num1))) + ' x ' + str(Num2) + ' = ? ')
    return(UserAnswer)
def actual_answer(Num1,Num2):
    Ans = Num1 * Num2
    return(Ans)
def timestable_answer(Num1,Num2):
    if actual_answer(Num1,Num2) == user_answer(Num1,Num2):
        print('Well done, you got the correct answer!')
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()
def what_times_table():
    Num1 = int(input("Which times-table do you want to be tested on? "))
    return(Num1)
def random_test_integer():
    Num2 = random.randrange(2,13)
    return(Num2)










# main program
print("Times-table tester")
print()
testTable = input("Which times-table do you want to be tested on? ")
testTable = int(testTable)


for questions in range(1,6):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    UserAnswer = int(UserAnswer)





    if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()
              

