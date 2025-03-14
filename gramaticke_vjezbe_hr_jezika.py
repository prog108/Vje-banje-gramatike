print('')
print('*' * 10 + 'VJEŽBA IZ GRAMATIKE HRVATSKOGA JEZIKA:' + '*' * 10)
print('')
print('*' * 17 + 'PRIDJEVI PO RODU I BROJU' + '*' * 17)
print('')



#Otvaranje .txt datoteke
with open('zadaci.txt', 'r', encoding='utf-8') as file:
    vjezba_gramatike = file.read()

#Postavljanje oznaka koje će program tražiti u datoteci
oznaka_sprijeda = "<"
oznaka_straga = ">"

#Brojčanik i for petlja za pretragu oznaka
brojanje = -1
popis_pridjeva = []

for broj, znak in enumerate(vjezba_gramatike):
    if znak == oznaka_sprijeda:
           brojanje = broj

#Definiranje riječi u datoteci te popunjavanje liste "popis_pridjeva"
    if znak == oznaka_straga and brojanje != -1:
        rijec = vjezba_gramatike[brojanje: broj + 1]
        popis_pridjeva.append(rijec)
        brojanje = -1


odgovori = {}

#Promijena vrijednosti u listi te prebacivanje liste u rječnik
for indx in popis_pridjeva:
        odgovor = input("Unesi odgovarajući pridjev: " + indx + ": ")
        odgovori[indx] = odgovor

#Iz rječnika mijenjamo stringove unutar datoteke
for indx in popis_pridjeva:
     vjezba_gramatike = vjezba_gramatike.replace(indx, odgovori[indx])


 
print('')
print('*' * 10 + 'USPOREDIMO OBLIK PRIDJEVA S IMENICOM UZ KOJU STOJE' + '*' * 10)
print('')
print('*' * 10 + 'PRIDJEVI' + '*'*10)

print('')
print(vjezba_gramatike)
print('')

