# Napravi listu od 5 brojeva i smesti je u varijablu brojevi.
brojevi = [2, 8, 5, 11, 16]

# Iz liste iz prethodnog zadatka: ispiši prvi element, ispiši poslednji element.
prvi_element = brojevi[0]
poslednji_element = brojevi[len(brojevi)-1]

# Izračunaj i ispiši koliko elemenata ima lista brojevi.
count_brojevi = len(brojevi)
print(f"U listi ima ukupno {count_brojevi} brojeva.")

# Izračunaj zbir svih elemenata u listi koristeći sum() i smesti ga u varijablu
sum_svih_elemenata = sum(brojevi)
print(f"Sum svih elemenata {sum_svih_elemenata}")

# Izračunaj prosečnu vrednost elemenata iz liste brojevi.
prosecna_vrednost = sum(brojevi) / brojevi[len(brojevi)-1]
print(f"Prosecna vrednost {round(prosecna_vrednost, 2)}")

# Napravi listu sa imenima 4 grada.
gradovi = ["Novi Sad", "Kraljevo", "Pancevo", "Nis"]

# Spoji imena gradova u jedan string razdvojen zarezima.
print(f"{gradovi[0]}, {gradovi[1]}, {gradovi[2]}, {gradovi[3]}")

# Dodaj novi broj u listu brojevi pomoću append().
brojevi.append(23)
print(brojevi)

# Umetni broj 10 na drugo mesto u listi brojevi.
brojevi.insert(2, 10)

# Obriši poslednji element iz liste brojevi.
brojevi.pop(len(brojevi)-1)

# Pronađi najmanji i najveći broj u listi brojevi.
najmanji_broj = min(brojevi)
najveci_broj = max(brojevi)

# Sortiraj listu brojevi u rastućem redosledu.
brojevi.sort()

# Ispiši listu brojeva u obrnutom redosledu (koristeći slicing).
print(brojevi[::-1])

# Napravi još jednu listu brojeva i spoji je sa listom brojevi.
brojevi_2 = [32, 54, 61, 73, 89]
nova_lista_brojeva = brojevi + brojevi_2
print(nova_lista_brojeva)

# Prebroj koliko se puta broj 5 pojavljuje u listi.
print(brojevi.count(5))

# Proveri da li se broj 7 nalazi u listi brojevi.
if 7 in brojevi:
  print(f"Trazeni broj se nalazi u listi {brojevi.count(7)} puta")
else:
  print("Trazeni broj nije u listi")

# Napravi listu cena proizvoda i izračunaj: ukupnu cenu, prosečnu cenu'
cene_proizvoda = [1250, 980, 520, 1680, 2310]
ukupna_cena = sum(cene_proizvoda)
prosecna_cena = sum(cene_proizvoda) / len(cene_proizvoda)
print(int(prosecna_cena))

# Iz liste imena napravi poruku.
# Ovo pitanje nisam razumeo ?!

# Napravi listu od 5 ocena. izračunaj prosečnu ocenu, pronađi najveću i najmanju ocenu, ispiši sve u jednoj poruci.
# Ne znam na koje se ocene tacno misli, recimo da su skolske ocene.
ocene = [3, 5, 2, 3, 4]
prosecna_ocena = sum(ocene) / len(ocene)
najveca_ocena = max(ocene)
najmanja_ocena = min(ocene)
print(f"Prosecna ocena: {prosecna_ocena}, najveca ocena: {najveca_ocena} i najmanja ocena: {najmanja_ocena}")
