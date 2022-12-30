from ip import scanip1
import csv
from csv import writer,reader


def writeCsvFile(fname, data, *args, **kwargs):
    """
    @param fname: string, name of file to write
    @param data: list of list of items
 
    Write data to file
    """
    mycsv = csv.writer(open(fname, 'w'), *args, **kwargs)
    for row in data:
        mycsv.writerow(row)


def filtrer(filename):

    with open(filename,'r') as in_file, open('iplist_out2.csv','w') as out_file:
        seen = set()
        for line in in_file:
            if line in seen: continue

            seen.add(line)
            out_file.write(line)

            #out_file.write(scanip1(str(line)))
        #with open('iplist_out2.csv','w') as out_file2, open('iplist_out.csv','r') as out_file:    
            #csv_reader=reader(out_file)
            #csv_writer=writer(out_file2)
        #with open('iplist_out.csv', 'a') as csv_file:

            #dict_object = csv.DictWriter(csv_file, fieldnames='B') 
            #for line1 in out_file:
    mydat = [
    ['IP','RESULT']
    ]
    l = []
 
    with open('iplist_out2.csv','r') as in_file:
        for line in in_file:
            l.append(line.replace("\n", ""))
            l.append(scanip1(line))
            #print(list)
            mydat.append(l)
            l = []
    writeCsvFile('half_cooked.csv', mydat)
 
 
 
    with open('half_cooked.csv', newline='') as in_file2:
        with open('iplist_final.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file2):
                if row:
                    writer.writerow(row)
            