slowo = input("Podaj słowo: ")
slowo = slowo.capitalize()
srodek_slowa = slowo[1:-1].lower()
srodek_slowa = slowo[0] + srodek_slowa + slowo[-1]
print("Słowo z dużą literą na początku i małymi literami w środku: ", srodek_slowa)