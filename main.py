import csv

with open('input.csv') as fichier_csv:
    data = []
    reader = csv.DictReader(fichier_csv, delimiter= ',')
    for lign in reader:
        data.append(lign)

print(data)

en_tete = ["nom", "salaire"]
with open('output.csv') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter= ",")
    writer.writerow(en_tete)