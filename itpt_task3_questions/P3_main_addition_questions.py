"""
Task 3

Implement and test a program to ask a user 10 addition questions 
using randomly created numbers between 10 and 30. The program should:

1. check if each of the user’s answer is correct
2. keep a total of the number of correct answers
3. repeat the quiz until the user achieves more than seven correct
""" 
import random as r
from quizz1 import quizz1

a = []
for i in range(10):
    s = r.randint(10,30)
    a.append(s)

print(a)
"""
print("Please, solve the expresion: 5*x + 6*y + 3*z")
print(f"Where x = {a[0]}, y = {a[1]}, z = {a[2]}")
f1 = quizz1(a[0], a[1], a[2])
a1 = f1.equation1()
print(a1)
answer1 = int(input("The answer is: "))


if answer1 == a1:
    print(f"Corect answer. 5*{a[0]} + 6*{a[1]} + 3*{a[2]} = {a1}")
else:
    print("The anser is not correct")
"""
def comparation(a,b):
    if a > b:
        return a;
    elif b > a:
        return b; 
    else:
        return "="



    


