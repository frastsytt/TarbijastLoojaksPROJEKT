import requests
import csv

# Lahenduse failis peab kommentaarina sisalduma ka püstitatud ülesande tekst ja autorite nimed.
#
# Arvutab euro valuutast raha ümber uude valuutasse
#
# HEAD COMMENTID.
#
# + 1 DEFINITION.
#
# + 1 IF LAUSE.
#
# + 1 WHILE / FOR LOOP.
#
# + READ FAILIST VÕI INPUT().
#
# + PRINT().
#
# + 1 ARRAY (LIST).
import urllib


source = requests.get(url="https://www.eestipank.ee/valuutakursid/export/csv/latest", )
string = source.text
postString = string.split("\n",3)[3]


andmefail = open("andmed.csv", "w", encoding="UTF-8")
andmefail.write(postString)
andmefail.close()

valuuta_nimed = []
kursi_väärtused = []


with open('andmed.csv') as csvfile:
    tabel = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in tabel:
        valuuta_nimed.append(row[0])
        kursi_väärtused.append(row[1])


def valuutavahetus(nimi, raha):
    if nimi.upper() in valuuta_nimed and type(raha) == float:
        pärast_vahetust = round(raha * float(kursi_väärtused[valuuta_nimed.index(nimi.upper())]), 2)
        return pärast_vahetust
    else:
        return "Sisestatud valuuta ei sobi."


for line in valuuta_nimed:
    print(line)

while True:
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






