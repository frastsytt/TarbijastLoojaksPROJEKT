source = requests.get(url="https://www.eestipank.ee/valuutakursid/export/csv/latest", )
string = source.text
postString = string.split("\n",3)[3]
print(postString)

andmefail = open("andmed.csv", "w", encoding="UTF-8")
andmefail.write(postString)
andmefail.close()

#
#
#
# # output = ""
# # for kurss in source.text:
# #     if kurss.isalpha():
# #         output += kurss + " "
# #
# print(postString)

import csv
with open('andmed.csv') as csvfile:
    tabel = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in tabel:
        print(row[0])
