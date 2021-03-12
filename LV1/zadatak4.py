suma = int(0)
brojac = int(0)

while 1:
    try:
        broj = input("Unesi broj: ")
        if broj != "Done":
            broj = int(broj)
            if brojac == 0:
                min = max = broj
        else: 
            break    
    except:
        print("Krivi unos!")
        continue
    suma += broj 
    brojac += 1 
    if broj < min:
        min = broj
    if broj > max:
        max = broj

print("Uneseno je ", brojac, " brojeva")
print("Najveci je ", max, " a najmanji ", min)
print("srednja vrijednost je", float(suma/brojac))

