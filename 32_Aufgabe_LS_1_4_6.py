#Endkapital = Anfangskapital * (1 + Zinssatz / 100) Laufzeit

anfagskapital = float(input("Bitte geben Sie Ihr Anfangskapital ein: "))
zinssatz = float(input("Bitte geben Sie den Zinssatz in Prozent ein: "))
laufzeit = float(input("Bitte geben Sie die Laufzeit in Jahren ein: "))

endkapital = anfagskapital * (1 + zinssatz / 100) ** laufzeit

print(f"Endkapital nach {laufzeit} Jahren: {endkapital:.2f} €")

