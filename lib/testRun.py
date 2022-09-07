import csv
import subprocess
with open('../File.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    #result = []
    expect = []
    for row in reader:
        expect.append(row[1])
    print(expect)

