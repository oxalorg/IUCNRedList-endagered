import csv

FILENAME = 'endagered-animalia.csv'

names = []
with open(FILENAME, newline='', encoding='latin1') as csvfile:
    animal_reader = csv.DictReader(csvfile)
    for row in animal_reader:
        names.append(row['Common names (Eng)'])


names = [name for name in names if name.strip()]

uniq_names = []
for name in names:
    aliases = [x.strip().replace(r"'", "") for x in name.split(',')]
    uniq_names.extend(aliases)

uniq_names = list(set(name.lower() for name in uniq_names))

uniq_names = [name.title().replace(' ', '') for name in uniq_names]

for name in uniq_names:
    print(name)
