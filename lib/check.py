import csv
import subprocess
with open('File.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    result = []
    expectList = []
    for row in reader:
        expectList.append(row[1])
    expect = "[\'" + '\', \''.join(expectList) + '\']'
    cmd = "python run.py"
    result = subprocess.check_output(cmd).decode('utf-8').strip()
    print('Полученный результат: '+result)
    print('Ожидаемый результат: '+expect)
    if result == expect:
        print('Результаты совпали')
    else:
        print('Результаты не совпали')

