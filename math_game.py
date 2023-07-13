import random


def select_operation():
    print (''' select the operation
1. addition(+)
2. subtraction(-)
3. multiplication(x)
4. division(/)
''')
    
def random1(level):
    import random
    if level== '1' : #low level
        num1 = random.randint(1,10)
        return num1
    if level== '2' :#mid level
        num1= random.randint(11, 50)
        return num1
    if level== '3' : #high level
        num1= random.randint(51, 100)
        return num1

def random2(level):
    import random
    if level== '1' : #low level
        num2 = random.randint(1,10)
        return num2
    if level== '2' :#mid level
        num2= random.randint(11, 50)
        return num2
    if level== '3' : #high level
        num2= random.randint(51, 100)
        return num2


def assign_operator(operator):
    if operator== '1' :
        operator= '+'
    if operator == '2' :
        operator= '-'
    if operator == '3' :
        operator= '*'
    if operator== '4' :
        operator= '/'
    return operator
def correct_answer(operator,a,b):
    if operator== '+':
        c= a+b
    if operator == '-':
        c = a-b
    if operator== '*' :
        c = a*b
    if operator== '/':
        c = a/b
    return c
print("**THE ART OF ARITHMETIC**")
print("welcome \n this game suports 3 levels :-")
print('''
1. low level
2. mid level
3. high level
''')
points = 0
while True:
    level = input('what level do you wish to play?\n')

    if level=='1' or level== '2' or level=='3':
        select_operation()
        while True:
            operation = input('what operation do you wish to use?\n')
            if operation == '1' or operation == '2' or operation== '3' or operation== '4':
                break
            else:
                print('INVALID INPUT!!')
                continue
        print('you chose level '+ level + ' and the ' + assign_operator(operation) + ' operator')
        num1= random1(level)
        num2= random2(level)
        answer = correct_answer(assign_operator(operation), num1, num2)
        print('what is '+ str(num1)+ str(assign_operator(operation)) + str(num2))
        your_answer = int(input("input your answer:\n"))

        if answer == your_answer:
            points= points + 1
            print ('correct answer!')
            print(''' do you wish to try again?
y/n''')
            another_trial= input()
            if another_trial == 'y' or another_trial== 'Y':
                continue
            else :
                print('you earned '+ str(points) +' points')
                print(' byeee')
                break
           
            
        else:
            print('no, the correct answer is ' + str(answer))
            print(''' do you wish to try again?
y/n''')
            another_trial= input()
            if another_trial == 'y' or another_trial== 'Y':
                continue
            else :
                print('you earned '+ str(points) +'points')
                print(' byeee')
                break
            
         
    else:
        print("INVALID INPUT!!!!")
        continue

        












