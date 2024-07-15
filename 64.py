year=2001  
if (year <= 0): 
    print("0 and negative is not allow for a year") 
elif (year <= 100): 
    print("1st century") 
elif (year % 100 == 0): 
    print(year // 100,"century") 
else: 
    print(year // 100 + 1,"century")  
