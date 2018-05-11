import csv
all = []
with open('file.csv','r') as finput:
    with open('out1.csv', 'w') as foutput:
        writer = csv.writer(foutput)
        reader = csv.reader(finput)

        
        row = next(reader)
        row.append('Copied Name')
        all.append(row)

        for row in reader:
            row.append(row[0])
            all.append(row)

        writer.writerows(all)
