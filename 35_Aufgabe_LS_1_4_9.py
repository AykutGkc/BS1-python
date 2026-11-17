import math

bogenmass_input = float(input("Lütfen radyan değerini girin (Bitte geben Sie das Bogenmaß ein): "))


grad_ergebnis = bogenmass_input * (180 / math.pi)


print(f"Grad: {grad_ergebnis:.2f}°")