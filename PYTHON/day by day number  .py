# 61.	Write a program to print day according to the day number entered by the user
# days = str(input("enter a days"))
# day1 = str(input("monday"))
# day2 = str(input("tuesday"))
# day3 = str(input("wednesday"))
# day4 = str(input("thrusday"))
# day5 = str(input("friday"))
# day6 = str(input("satrday"))

# print(day1)
# print(day2)
# print(day3)
# print(day4)
# print(day5)
# print(day6)



weekday = int(input("enter a weekday (1-7):"))
if(weekday)==1:
    print("monday")
elif(weekday)==2:
    print("tuesday")
elif(weekday)==3:
    print("wednesday")
elif(weekday)==4:
    print("thruesday")
elif(weekday)==5:
    print("friday")
elif(weekday)==6:
    print("saterday")
elif(weekday)==7:
    print("sunday")
else:
    ("invalide date")