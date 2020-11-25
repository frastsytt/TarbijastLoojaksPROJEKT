import requests
import csv

# Defineerime arvutuse funktsiooni
def valuutavahetus(nimi, raha):
    if nimi.upper() in valuuta_nimed and type(raha) == float:
        pärast_vahetust = round(raha * float(kursi_väärtused[valuuta_nimed.index(nimi.upper())]), 2)
        return pärast_vahetust
    else:
        return "Sisestatud valuuta ei sobi."
    
# Teeme tühjad järjendid valuuta nimede ja väärtuste jaoks
valuuta_nimed = []
kursi_väärtused = []

# Läheme eestipank.ee lehele ja võtame sealt kursid
source = requests.get(url="https://www.eestipank.ee/valuutakursid/export/csv/latest", )
string = source.text
# Võtame csv failist esimesed 3 rida ära
postString = string.split("\n",3)[3]

# Teeme postStringi csv failiks
andmefail = open("andmed.csv", "w", encoding="UTF-8")
andmefail.write(postString)
andmefail.close()

# Paneme csv faili sisu järjenditesse
with open('andmed.csv') as csvfile:
    tabel = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in tabel:
        valuuta_nimed.append(row[0])
        kursi_väärtused.append(row[1])

# Kuvame kasutajale võimalike kursside nimed
for line in valuuta_nimed:
    print(line)

# Siseneme loop-i, et ei peaks programmi peale igat arvutust uuesti käivitama
while True:
    # Küsime kasutajalt sisendid ja arvutame väärtuse, vale väärtuste korral anname veateate
    try:
        print("")
        valuuta_nimi = str(input("Sisestage valuuta lühend: "))
        print("")
        raha_kogus = float(input("Sisestage vahetatava raha kogus: "))
        print("")
        print(valuutavahetus(valuuta_nimi, raha_kogus))
        print("")
    except ValueError:
        print("")
        print("Sisestage korrektsed sisendid. ")
