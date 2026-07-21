#----Turf-----
turf="circket foodball seattle volleyball kabadi";
choice=input("Enter your sports: ")
a=0;
if choice in turf:
    print("sports is available")
    if choice=="circket" or choice=="foodball":
        print("per hour 1000 for",choice)
        a=1000
    elif choice=="seattle" or choice=="volleyball":
        print("per hour 800 for",choice)
        a=800
    elif choice=="kabadi":
        print("per hour 750 for",choice)
        a=750
    if True:
        print("not include GST:",a)
        gstamt=((a/100)*118)
        print("with GST Amount is:",gstamt,"for",choice)
else:
    print("sports is not available")
