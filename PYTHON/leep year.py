a = int(input("enter a year"))
if(a%400)==0:
    if(a%100)==0:
        if(a%4)==0:
            print("given year is a leap year")
        else:
            ("not a leap year")
    else:
        ("a  not leap year")
else:
    ("is not  a leap year")