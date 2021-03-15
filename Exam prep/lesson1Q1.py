#input
paid=(float(input("how much haw you paid?")))
price=float(input("how much does it cost?"))


#calc
if paid<1175:
    procent=100
elif paid<1708:
    procent=50
elif paid<2189:
    procent=25
elif paid<2350:
    procent=10
else:
    procent=0

#output
print("You pay ",price*(procent/100), "kr")