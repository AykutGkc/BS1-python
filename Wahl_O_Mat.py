i_stimmenKandidat1=0
i_stimmenKandidat2=0
i_stimmen_ges=0
f_prozenteKanditat1=0
f_prozenteKanditat2=0

i_stimmenKandidat1= int(input("Bitte geben Sie die Stimmen für Kandidat 1 an: "))
i_stimmenKandidat2= int(input("Bitte geben Sie die Stimmen für Kandidat 2 an: "))

i_stimmen_ges= i_stimmenKandidat1 + i_stimmenKandidat2

f_prozenteKanditat1=(i_stimmenKandidat1/i_stimmen_ges)*100
f_prozenteKanditat2=(i_stimmenKandidat2/i_stimmen_ges)*100


print(f"Kandidat 1(in Prozent): {f_prozenteKanditat1:.2f}%")
print(f"Kandidat 2(in Prozent): {f_prozenteKanditat2:.2f}%")
