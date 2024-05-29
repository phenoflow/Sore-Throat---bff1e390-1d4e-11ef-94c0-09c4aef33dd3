# Victoria Palin, Anna Molter, Miguel Belmonte, Darren M Ashcroft, Andrew White, William Welfare, Tjeerd van Staa, 2024.

import sys, csv, re

codes = [{"code":"H02..12","system":"readv2"},{"code":"H02..11","system":"readv2"},{"code":"AA1..11","system":"readv2"},{"code":"1C9Z.00","system":"readv2"},{"code":"R041.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('sore-throat-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sore-throat---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sore-throat---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sore-throat---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
