marks = float(input('Enter your marks: '))
if marks>=90:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=50:
    grade="C"
elif marks>=40:
    grade="D"
else:
    grade="F"
    
print(grade)
