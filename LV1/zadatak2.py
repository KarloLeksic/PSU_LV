try:
    ocjena = float(input("Unesi ocijenu: ", ))
except:
     print("Pogreska")   
     exit()
     
if ocjena < 0.0 or ocjena > 1.0:
    print("Krivi unos")
    exit()
else:
    if ocjena >= 0.9: print("A")
    elif ocjena >= 0.8: print("B")
    elif ocjena >= 0.7: print("C")
    elif ocjena >= 0.6: print("D")
    else: print("F")