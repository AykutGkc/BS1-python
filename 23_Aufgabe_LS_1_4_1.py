
"""
1.Quadrat-Kubikmeter-Rechner mit folgenden Funktionen:
    - Berechnung des Flächeninhaltes und/ oder Umfangs eines
    Rechtecks, Dreiecks bzw. Kreises
    - Berechnung des Volumens/ Oberflächeninhaltes eines
    Quaders, Zylinders bzw. einer Kugel
"""
import math

print("=Quadrat-Kubikmeter-Rechner=")
print("1: Rechteck (Fläche & Umfang)")
print("2: Dreieck (Fläche & Umfang)")
print("3: Kreis (Fläche & Umfang)")
print("4: Quader (Volumen & Oberfläche)")
print("5: Zylinder (Volumen & Oberfläche)")
print("6: Kugel (Volumen & Oberfläche)")

auswahl = input("Bitte wählen Sie eine Option (1-6): ")

if auswahl == '1':
    a = float(input("Seite a: "))
    b = float(input("Seite b: "))
    flaeche = a * b
    umfang = 2 * (a + b)
    print(f"Flächeninhalt: {flaeche:.2f}")
    print(f"Umfang: {umfang:.2f}")

elif auswahl == '2':
    a = float(input("Grundseite a: "))
    b = float(input("Seite b: "))
    c = float(input("Seite c: "))
    h = float(input("Höhe h (auf Seite a): "))
    flaeche = (a * h) / 2
    umfang = a + b + c
    print(f"Flächeninhalt: {flaeche:.2f}")
    print(f"Umfang: {umfang:.2f}")

elif auswahl == '3':
    r = float(input("Radius r: "))
    flaeche = math.pi * r**2
    umfang = 2 * math.pi * r
    print(f"Flächeninhalt: {flaeche:.2f}")
    print(f"Umfang: {umfang:.2f}")

elif auswahl == '4':
    a = float(input("Länge a: "))
    b = float(input("Breite b: "))
    c = float(input("Höhe c: "))
    volumen = a * b * c
    oberflaeche = 2 * (a*b + a*c + b*c)
    print(f"Volumen: {volumen:.2f}")
    print(f"Oberflächeninhalt: {oberflaeche:.2f}")

elif auswahl == '5':
    r = float(input("Radius r: "))
    h = float(input("Höhe h: "))
    volumen = math.pi * r**2 * h
    oberflaeche = 2 * math.pi * r * (r + h)
    print(f"Volumen: {volumen:.2f}")
    print(f"Oberflächeninhalt: {oberflaeche:.2f}")

elif auswahl == '6':
    r = float(input("Radius r: "))
    volumen = (4/3) * math.pi * r**3
    oberflaeche = 4 * math.pi * r**2
    print(f"Volumen: {volumen:.2f}")
    print(f"Oberflächeninhalt: {oberflaeche:.2f}")

else:
    print("Ungültige Eingabe!")
