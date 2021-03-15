def calculate_loan(property_price,loan,interest_rate):
  if property_price/loan>0.7:
    amort=2
  elif property_price/loan>0.5:
    amort=1
  else: 
    amort=0
  loan=loan/12
  amort=amort*0.01
  print(loan*amort)
  print(loan*interest_rate*0.01)
  print(loan*(interest_rate*0.01+amort))