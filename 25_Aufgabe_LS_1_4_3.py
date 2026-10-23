"""
3. Einfacher Taschenrechner:
Verrechnen Sie zwei Zahlen zu den Ergebnissen von Summe, Differenz, Produkt und Quotienten
"""

print("=Einfacher Taschenrechner=")

zahl1=float(input("Geben Sie die erste Zahl ein: "))
zahl2=float(input("Geben Sie die zweite Zahl ein: "))

summe=zahl1+zahl2;
print(f"\nSumme: {summe}")

differenz=zahl1-zahl2;
print(f"Differenz: {differenz}")

produkt=zahl1*zahl2;
print(f"Produkt: {produkt}")

if zahl2!=0:
    quotient=zahl1/zahl2;
    print(f"Quotient: {quotient}")
else:
    print("Quotient: Division durch Null ist nicht erlaubt.")   
    
