import csv
import subprocess
with open('../File.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    result = []
    for row in reader:
        cmd = "python script.py english {0}".format(row[0])
        returned_output = subprocess.check_output(cmd)
        result.append(returned_output.decode('utf-8').lower().strip())
    print(result)


