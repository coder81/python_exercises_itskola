# Kreiraj varijable ime i prezime i ispiši ih u jednom redu.
ime = "Arnold"
prezime = "Schwarzenegger"
print(ime + " " + prezime)

# Deklariši varijablu godina_rodjenja i izračunaj starost (pretpostavi da je trenutna godina 2025).
godina_rodjenja = 1947
trenutna_starost = 2025 - godina_rodjenja
print(f"Trenutna starost: {trenutna_starost}")

# Kreiraj varijable: ceo broj, decimalni broj i string. Za svaku ispiši njen tip.
ceo_broj = 10
print(type(ceo_broj))
dec_broj = 10.5
print(type(dec_broj))
neki_string = "deset"
print(type(neki_string))

# Deklariši a = 12 i b = 8, pa izračunaj njihov zbir.
a = 12
b = 8
print("Zbir: ", a + b)

# Deklariši x = 50 i y = 18, pa izračunaj razliku.
x = 50
y = 18
print("Razlika: ", x - y)

# Deklariši cena = 25 i kolicina = 4, pa izračunaj ukupnu cenu.
cena = 25
kolicina = 4
print("Ukupna cena: ", cena * kolicina)

# Deklariši ukupno = 100 i ljudi = 4, pa izračunaj koliko svako dobija
ukupno = 100
ljudi = 4
print("Svako dobija: ", ukupno / ljudi)

# Deklariši a = 5 i izračunaj kvadrat tog broja.
a = 5
print(f"Kvadrat broja {a} : {a*a}")

# Deklariši tri broja i izračunaj njihovu prosečnu vrednost.
prvi_broj = 25
drugi_broj = 10
treci_broj = 20
prosecna_vrednost = (prvi_broj + drugi_broj + treci_broj) / 3
print("Prosecna vrednost :", round(prosecna_vrednost, 2))

# Kreiraj varijablu broj = 10. Promeni njenu vrednost na 25
moj_broj = 10
moj_broj = 25
print("Promenjena vrednost na: ", moj_broj)

# Deklariši grad i drzava, pa ih spoji u jedan string.
grad = "Bratislava"
drzava = "Slovacka"
print(f"{grad} - {drzava}")

# Kreiraj string i smesti njegovu dužinu u posebnu varijablu.
my_string = "Ovo je neki veoma bitan string."
len_string = len(my_string)
print("Duzina string-a je: ", len_string)

# Deklariši cena = 100 i porez = 20 (u procentima). Izračunaj cenu sa porezom.
cena = 100
porez = 20 #%
cena_sa_porezom = cena + ((porez * cena) / 100)
print("Cena sa porezom: ", int(cena_sa_porezom))

# Deklariši cenu i popust (u %), pa izračunaj konačnu cenu.
trenutna_cena = 1200
popust = 12 #%
konacna_cena = trenutna_cena - (trenutna_cena * (popust / 100))
print("Konacna cena: ", int(konacna_cena))

# U jednom redu dodeli vrednosti trima varijablama.
var_1, var_2, var_3 = 10, "Lorem ipsum...", 20.4

# Deklariši a = 7 i b = 3, pa zameni njihove vrednosti.
a = 7
b = 3
a, b = b, a # zamena vrednosti varijabli
print("a : ", a)
print("b : ", b)

# Deklariši širinu i visinu pravougaonika i izračunaj: površinu i obim
sirina = 12
visina = 18
povrsina_pravougaonika = sirina * visina
obim_pravougaonika = (sirina + visina) * 2
print("Povrsina pravougaonika: ", povrsina_pravougaonika)
print("Obim pravougaonika: ", obim_pravougaonika)

# Deklariši: ime, broj sati rada, cena po satu. Izračunaj i smesti u varijablu ukupnu zaradu.
ime = "Tom Cruise"
broj_sati = 38.5 # nedeljno
cena_po_satu = 50 #€
nedeljna_zarada = broj_sati * cena_po_satu # za nedelju dana
ukupna_zarada = nedeljna_zarada * 4 # mesecna zarada
print("Ukupna zarada: ", ukupna_zarada)
