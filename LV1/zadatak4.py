#dovrsitiii

suma = int(0)
brojac = int(0)

while 1:
    try:
        broj = input()
        if brojac == 0:
            min = max = broj
        if broj != "Done":
            broj = int(broj)
        else: 
            break    
    except:
        print("Krivi unos!")
        continue
    suma += broj 
    brojac += 1 

print("Uneseno je ", brojac, " brojeva")