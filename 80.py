a = int(input('please enter the year'))

b = "there are 365 days"
c = "there are 366 days"

if a%4 == 0 and a%400 != 0:
    print(c)

elif a%4 == 0 and a%400 == 0:
    print(b)

else:
    print(b)
