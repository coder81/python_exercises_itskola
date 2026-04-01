# Napravi listu koja sadrži različite tipove podataka (npr. broj, string, float).
# Proveri da li je prvi element string i ispiši poruku ako jeste.
lista_tipova_podataka = [15, "hello_world", 22.5, True]
if(type(lista_tipova_podataka[0]) is str) :
  print("Prvi element jeste tipa -string-")
else:
  print("Prvi element nije tipa -string-")

# Napravi listu i proveri: ako je lista prazna → ispiši "Lista je prazna", ako nije → ispiši broj elemenata.
moja_lista = [5, 12, 18, 22]
if(len(moja_lista) > 0):
  print(len(moja_lista))
else:
  print("Lista je prazna!")

# Ako lista ima više od 3 elementa: ispiši prvi i poslednji element, u suprotnom ispiši poruku da je lista prekratka.
moja_lista = [5, 12, 18, 22, 32]
if(len(moja_lista) > 3):
  print(f"Prvi element : {moja_lista[0]}, poslednji element : {moja_lista[len(moja_lista) - 1]}")
else:
  print("Lista je prekratka!")

# Napravi listu godina starosti. Ako je bilo koji broj manji od 18, ispiši "Nisu svi punoletni".
godine_starosti = [9, 12, 21, 33, 45]
if all(godina < 18 for godina in godine_starosti):
  print("Nisu svi punoletni.")
else:
  print("Svi su punoletni.")

# Napravi listu cena proizvoda. Ako je prosečna cena veća od 1000, ispiši "Skupo" inače "Povoljno".
cene_proizvoda = [280, 1850, 560, 810, 1620]
prosecna_cena = sum(cene_proizvoda) / len(cene_proizvoda)
if prosecna_cena > 1000:
  print("Skupo")
else:
  print("Povoljno")

# Ako se u listi stringova nalazi reč "Python", ispiši "U listi je Python".
zivotinje = ["elephant", "monkey", "python", "lion"]
if "python" in zivotinje:
  print("U listi je Python")
else:
  print("U listi nije Python")

# Iz liste brojeva proveri: ako ima više pozitivnih nego negativnih → ispiši "Više pozitivnih".
moji_brojevi = [-1, 2, -3, -4, 5, 6, -7, 8, 9, 10]

negative_count = len([num for num in moji_brojevi if num < 0])
positive_count = len([num for num in moji_brojevi if num > 0])

if positive_count > negative_count:
  print("Vise je pozitivnih")
else:
  print("Vise je negativnih")

# Napravi listu reči. Ako je najduža reč duža od 8 karaktera, ispiši poruku.
lista_reci = ["peskir", "viljuska", "motokultivator", "volan"]
for i in range(len(lista_reci)):
   if len(lista_reci[i]) > 8:
     print("U listi se nalazi rec koja je duza od 8 karaktera")
     break
else:
 print("U listi se NE nalazi rec koja je duza od 8 karaktera")

# Napravi listu ocena (1–5). Ako lista sadrži ocenu 1, ispiši "Ima negativnih ocena".
negativne_ocene = [1, 2, 3, 4, 5, 4, 2].count(1)
if(negativne_ocene >=1):
  print("Ima negativnih ocena")

# Proveri da li su svi elementi u listi brojevi. Ako jesu, izračunaj njihov zbir.
lista_podataka = ["1", 2, 5, 8, 10, 15]
for i in range(len(lista_podataka)):
  if type(lista_podataka[i]) == str:
    print("Nisu svi elementi u listi brojevi, tipa -integer-")
    break
else:
  print("Zbir elemenata u listi: ", sum(lista_podataka))

# Iz liste brojeva proveri: ako ima bar jedan paran broj → ispiši "Lista sadrži paran broj".
lista_brojeva = [1, 3, 5, 9, 11, 15]
for i in range(len(lista_brojeva)):
  if lista_brojeva[i] % 2 == 0:
    print("Lista sadrzi paran broj")

# Ako lista imena ima više od 5 imena: ispiši "Velika lista imena".
lista_imena = ["Tom", "Arnold", "Patrick", "Bob", "Roberto", "Daniel"]
if len(lista_imena) > 5:
  print("Velika lista imena")

# Ako je najmanji broj u listi manji od 0, ispiši "Postoji negativan broj".
lista_brojeva = [-5, -2, 5, 9, 11, 15]
if min(lista_brojeva) < 0:
  print("Postoji negativan broj")

# Ako lista ima tačno 10 elemenata: ispiši "Lista ima idealnu dužinu".
lista_brojeva = [1, 3, 5, 9, 11, 15, 18, 22, 28, 33]
if len(lista_brojeva) == 10:
  print("Lista ima idealnu duzinu")

# Ako je poslednji element u listi tipa float, ispiši "Decimalni broj".
lista_brojeva = [5, 12, 18, 21, 25.5]
if type(lista_brojeva[len(lista_brojeva) - 1] == float):
  print("Decimalni broj")

# Ako je najveća cena u listi veća od 5000: primeni popust od 10% na tu cenu.lista_cena = [2250, 3420, 5200, 6360, 1820, 4550]
lista_cena = [2250, 3420, 5200, 6360, 1820, 4550]
for i in range(len(lista_cena)):
  if lista_cena[i] > 5000:
    cena_sa_popustom = int(lista_cena[i] - ((lista_cena[i] * 10) / 100))
    print(f"Cena sa popustom: {cena_sa_popustom} dinara.")

# Ako bar jedna rečenica u listi ima više od 20 karaktera: ispiši "Duga rečenica pronađena".
lista_recenica = ["Ovo je test", "Hello world", "Misim sta reci a ne zaplakati...", "Pajton iz nambr van!"]
for i in range(len(lista_recenica)):
  if len(lista_recenica[i]) > 20:
    print("Duga recenica pronadjena!")

# Ako lista sadrži i brojeve i stringove: ispiši "Mešoviti tipovi podataka".
lista_brojeva_stringova = ["test", 25, "proba", 55]
str_type_count = 0
int_type_count = 0
for i in range(len(lista_brojeva_stringova)):
  if type(lista_brojeva_stringova[i]) == str:
    str_type_count = str_type_count + 1
  else:
    int_type_count = int_type_count + 1

if str_type_count > 0 and int_type_count > 0:
  print("Mešoviti tipovi podataka")

# Ako je prosečna vrednost liste brojeva između 50 i 100: ispiši "Prosek je u očekivanom opsegu".
lista_brojeva = [25, 35, 58, 72, 88]
prosecna_vrednost = sum(lista_brojeva) / len(lista_brojeva)
if  prosecna_vrednost > 50 and prosecna_vrednost < 100:
  print("Prosek je u očekivanom opsegu")
else:
  print("Prosek nije u očekivanom opsegu")

# Napravi listu temperatura. ako je maksimalna > 30 → "Vruće", ako je između 15 i 30 → "Prijatno",  inače → "Hladno".
lista_temperatura = [25, 15, -10, 28, -2]
maksimalna_temperatura = max(lista_temperatura)
if maksimalna_temperatura > 30:
  print("Vruce")
elif maksimalna_temperatura < 30 and maksimalna_temperatura > 15:
  print("Prijatno")
else:
  print("Hladno")
