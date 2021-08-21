import csv

data = []
with open("dataset_2.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        data.append(i)
        #print(data)

headers = data[0]
#print(headers)

planetdata = data[1:]
#print(planetdata)

for i in planetdata:
    i[2] = i[2].lower()

planetdata.sort(key = lambda a:a[2])
#print(data2)

with open("data_sorted.csv", "a+", newline="") as f:
    csvwrite = csv.writer(f)
    csvwrite.writerow(headers)
    csvwrite.writerows(planetdata)
