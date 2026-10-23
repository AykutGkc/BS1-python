"""
4. Schreiben Sie ein Programm, das einen Kleinbuchstaben einliest und anschließend den entsprechenden Großbuchstaben ausgibt.
"""

print("Klein- zu Großbuchstaben Konverter")

# Eingabe
kleinbuchstabe = input("Bitte geben Sie einen Kleinbuchstaben ein: ")

# Verarbeitung & Ausgabe 
if kleinbuchstabe.islower():
    # Wenn die Eingabe nur aus Kleinbuchstaben besteht, dann umwandeln
    grossbuchstabe = kleinbuchstabe.upper()
    print(f"Der entsprechende Großbuchstabe ist: {grossbuchstabe}")
else:
    # Wenn ein Großbuchstabe, eine Zahl, ein Symbol oder ein Leerzeichen eingegeben wurde, Warnung ausgeben
    print("Warnung: Falsche Eingabe! Bitte verwenden Sie nur Kleinbuchstaben.")