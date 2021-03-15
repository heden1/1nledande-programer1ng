def grades(points):
    if points<=1:
        grade='F'
    elif points<=2:
        grade='D'
    elif points<=3:
        grade='C'
    elif points<=4:
        grade='B'
    elif points<=5:
        grade='A'
    return grade
print(grades(4))