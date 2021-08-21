import csv

dataset1 = []
with open("dataset_1.csv", "r") as f:
    df = csv.reader(f)
    for i in df:
        dataset1.append(i)

dataset2 = []
with open("data_sorted.csv", "r") as q:
    df2 = csv.reader(q)
    for i in df2:
        dataset2.append(i)

header1 = dataset1[0]
header2 = dataset2[0]

planetdata1 = dataset1[1:]
planetdata2 = dataset2[1:]

headers = header1+header2

planetdata = []
for index, items in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("test.csv", "a+", newline="") as f:
    csvwrite = csv.writer(f)
    csvwrite.writerow(headers)
    csvwrite.writerows(planetdata)
