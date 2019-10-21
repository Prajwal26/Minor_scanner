import csv
import itertools

with open("result1.txt",'r')as in_file:
    stripped=(line.strip() for line in in_file)
    lines =(line.split(",") for line in stripped if line)
    with open("result2.csv", 'w') as out_file:
        writer=csv.writer(out_file)
        writer.writerow(('title','intro'))
        writer.writerows(lines)