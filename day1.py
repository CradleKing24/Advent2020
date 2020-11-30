import csv
import math

with open("./resources/day1.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    lineCount = 0
    totalFuel = 0
    for module in csv_reader:
        fuel = 0
        fuel = int(module[0]) / 3
        fuel = math.floor(fuel)
        fuel -= 3
        totalFuel += fuel

print(totalFuel)