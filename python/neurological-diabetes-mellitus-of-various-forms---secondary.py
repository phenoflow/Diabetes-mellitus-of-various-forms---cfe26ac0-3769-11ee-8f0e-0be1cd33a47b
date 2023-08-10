# Prof. Elizabeth Sapey (UHB),PIONEER, 2023.

import sys, csv, re

codes = [{"code":"E104","system":"icd10"},{"code":"E104D","system":"icd10"},{"code":"E114","system":"icd10"},{"code":"E114A","system":"icd10"},{"code":"E114D","system":"icd10"},{"code":"E124","system":"icd10"},{"code":"E124A","system":"icd10"},{"code":"E124D","system":"icd10"},{"code":"E134","system":"icd10"},{"code":"E134D","system":"icd10"},{"code":"E144","system":"icd10"},{"code":"E144D","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-of-various-forms-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neurological-diabetes-mellitus-of-various-forms---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neurological-diabetes-mellitus-of-various-forms---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neurological-diabetes-mellitus-of-various-forms---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
