"""
2. Vorgänger-Nachfolger-Ausgabe (Beispiel für Wertebereichsüberschreitung): 
- Berechnung und Ausgabe von Vorgänger und Nachfolger mit den Testwerten 0 und 65535
"""

# Simulation einer Wertebereichsüberschreitung

# Testwerte
wert1 = 0
wert2 = 65535
grenze = 65536

print("Simulation der Wertebereichsüberschreitung:")

# Test für 0
print(f"\nTestwert: {wert1}")
# Zieht man 1 von 0 ab, springt der Wert auf das Maximum (65535).
vorgaenger1 = (wert1 - 1) % grenze 
nachfolger1 = (wert1 + 1) % grenze
print(f"Vorgänger: {vorgaenger1}") 
print(f"Nachfolger: {nachfolger1}")

# Test für 65535
print(f"\nTestwert: {wert2}")
vorgaenger2 = (wert2 - 1) % grenze
# Addiert man 1 zu 65535, gibt es einen Überlauf auf 0.
nachfolger2 = (wert2 + 1) % grenze 
print(f"Vorgänger: {vorgaenger2}")
print(f"Nachfolger: {nachfolger2}")