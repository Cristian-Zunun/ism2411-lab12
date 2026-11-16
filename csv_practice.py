# Exercise 2
import csv


with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)


    rows = list(reader)


    for row in rows:
        print(row)
# Exercise 3:
import csv


header = rows[0]
data = rows[1:]


print("Header:", header)


for row in data:
    print(row)
