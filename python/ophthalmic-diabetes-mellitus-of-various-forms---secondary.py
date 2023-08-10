# Prof. Elizabeth Sapey (UHB),PIONEER, 2023.

import sys, csv, re

codes = [{"code":"E103","system":"icd10"},{"code":"E103A","system":"icd10"},{"code":"E103D","system":"icd10"},{"code":"E113","system":"icd10"},{"code":"E113A","system":"icd10"},{"code":"E113D","system":"icd10"},{"code":"E123","system":"icd10"},{"code":"E123D","system":"icd10"},{"code":"E133","system":"icd10"},{"code":"E133D","system":"icd10"},{"code":"E143","system":"icd10"},{"code":"E143D","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-of-various-forms-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ophthalmic-diabetes-mellitus-of-various-forms---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ophthalmic-diabetes-mellitus-of-various-forms---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ophthalmic-diabetes-mellitus-of-various-forms---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
