year=int(input("enter year"))

if year%100==0 and year%400==0:
    print(year,"is an leap year")

elif year%4==0:
    print(year,"is an leap year")

else:
    print(year,"not an leap year")    
