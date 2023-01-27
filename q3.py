# import random 

# num1=random.randint(1,10)
# num2=random.randint(1,10)
# print(int(num1))
# print(int(num2))
# a=num1*num2

# b=int(input("enter your answer"))

# if a==b:
#     print("you are right")
# else:
#     print("you are wrong" ,  ",right answer is", a)


import random

num1=random.randint(1,10)
print(num1)
num2=random.randint(1,10)
print(num2)

a=num1*num2

mul_user=int(input("enter product of above two numbers: "))

if mul_user==num1*num2:
    print("hurray,Your answer is correct")

else:
    print("Oops!,your answer is not correct",a, "is the correct ans of this question")
            
