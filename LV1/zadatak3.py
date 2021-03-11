def total_kn(sati, knH):
    return sati * knH

sati = float(input("Unesite broj radnih sati: ", ))
placaPoSatu = float(input("Unesite koliko je placa za jedan sat: ", ))

print("Radni sati: ", sati, "h")
print("kn/h: ", placaPoSatu, )
print("Ukupno: ", total_kn(sati, placaPoSatu), "kn")