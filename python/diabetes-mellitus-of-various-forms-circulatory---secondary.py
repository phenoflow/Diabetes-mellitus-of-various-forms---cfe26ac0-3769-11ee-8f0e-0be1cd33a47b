# Prof. Elizabeth Sapey (UHB),PIONEER, 2023.

import sys, csv, re

codes = [{"code":"E105","system":"icd10"},{"code":"E105D","system":"icd10"},{"code":"E115","system":"icd10"},{"code":"E115D","system":"icd10"},{"code":"E125","system":"icd10"},{"code":"E135","system":"icd10"},{"code":"E145","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-of-various-forms-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-of-various-forms-circulatory---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-of-various-forms-circulatory---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-of-various-forms-circulatory---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
