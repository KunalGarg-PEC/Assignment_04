marks = int(input("enter student's marks: "))

if marks<25:
    print("F")

elif 25<=marks<45:
    print("E")    

elif 45<=marks<50:
    print("D")    

elif 50<=marks<60:
    print("C")

elif 60<=marks<80:
    print("B")

elif marks>=80:
    print("A")

else:
    print("enter valid marks")    

    