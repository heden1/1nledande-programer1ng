def kcals(nutrition,recipe):
    tKcals=0
    for i in range (len(recipe)):

        rec=str(recipe[i])
        rec=rec.strip('(').strip(')').strip(' \' ')
        x=rec.split(',')
        x[1]=x[1].strip(' \' ')
        amount=float(x[0])
        key=str(x[1])
        kcals=nutrition.get(key)
        tKcals=tKcals+kcals*amount
    return(tKcals)
        #rec=rec.strip('(')
        #
        #print(x)
        #print(x[i])
        #t=float(x[i])
        #print (t)
    #calst=calst +clas *i
    #return calst
kcals({'vetemjöl': 352, 'ägg': 137, 'socker': 405, 'vatten': 0, 'potatis': 59},[(2, 'ägg')])
kcals({'vetemjöl': 352, 'ägg': 137, 'socker': 405, 'vatten': 0, 'potatis': 59},[(1, 'vetemjöl'), (6, 'ägg'), (0.2, 'socker'), (0.5, 'vatten')])



