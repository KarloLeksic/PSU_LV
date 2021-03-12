f = input("Enter File name: ")

#otvaranje datoteke
try:
    f = open(f, 'r')
except:
    print("Error opening file . . .")
    exit()

#pretraga
line = f.readLine()
if "X-DSPAM-Confidence:" in line:
    print("Pronadeno")