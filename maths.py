from random import *

tasks = 10   # number of questions
mult_mod = 2    # maximum number for multiplication


score = 0

def math():
    global score
    
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    if num1 < num2: # prevent negative numbers
        num1, num2 = num2, num1
        
    symbol = randint(1,3)

    if symbol == 1:
        question = eval(input(str(num1) + " + " + str(num2) + " = "))
        answer = num1 + num2
        question = int(question)
        
        if question == answer:
            score += 1
            print("Correct.")

    elif symbol == 2:
        question = eval(input(str(num1) + " - " + str(num2) + " = "))
        answer = num1 - num2
        question = int(question)
        
        if question == answer:
            score += 1
            print("Correct.")
            
    elif symbol == 3:
        if mult_mod > 0:
            num2 = mult_mod
            
        question = eval(input(str(num1) + " x " + str(num2) + " = "))
        answer = num1 * num2
        question = int(question)
        
        if question == answer:
            score += 1
            print("Correct.")
            
for i in range(tasks):
    math()

print(("Your score was " + str(score) + "out of " + str(tasks)))


