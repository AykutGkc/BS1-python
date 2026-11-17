""" 
Schreiben Sie ein Programm, das die Anzahl der Felder eines Spielbretts (Schachbrett) einliest. 

Anschließend soll das Gewicht eines Reiskorns (25 mg) in kg und das Gesamtgewicht aller Reiskörner auf dem letzten Feld des Spielfeldes ausgegeben werden, wenn man bei jedem Feld die 

Anzahl der Reiskörner verdoppelt.
"""

felder = int(input("Bitte geben Sie die Anzahl der Felder des Spielbretts ein: "))
gewicht_reiskorn = 25 / 1000000  # Gewicht eines Reiskorns in kg

koerner_letztes_feld = 2 ** (felder - 1)
gewicht_letztes_feld_kg = koerner_letztes_feld * gewicht_reiskorn

koerner_gesamt = (2 ** felder) - 1
gewicht_gesamt_kg = koerner_gesamt * gewicht_reiskorn

print(f"\nOyun tahtasındaki toplam kare sayısı: {felder}")
print(f"Son karedeki (letztes Feld) pirinç tanelerinin ağırlığı: {gewicht_letztes_feld_kg} kg")
print(f"Tüm tahtadaki (Gesamt) pirinç tanelerinin toplam ağırlığı: {gewicht_gesamt_kg} kg")
 
