import requests

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
# 1 ARRAY (LIST).
import urllib


# def kurss():
#     pass
#
#
# def arvuta_kurss(raha, uus_valuuta):
#     if float(uus_valuuta) > 0:
#         uus_raha = float(raha) * float(uus_valuuta)
#         return uus_raha
#     else:
#         return "Sisestage positiivne kurss!"
#
#
# # Küsib kasutajalt vahetatava raha kogust ja ümber vahetamise kurssi.
# raha = input("Sisestage raha kogus: ")
# uus_valuuta = input("Sisestage valuuta kurss milleks raha vahetatakse: ")
#
# with open("main_valuuta_nimed.txt", "r") as valuuta_nimed:
#     for nimi in valuuta_nimed:
#         print(nimi)

    # print(str(arvuta_kurss(raha, uus_valuuta)))

source = requests.get(url="https://www.eestipank.ee/valuutakursid/export/csv/latest", )

for kurss in source.text:
    if len(open(source.text).readlines(  )):
        pass
print(source.text)
