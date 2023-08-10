# Prof. Elizabeth Sapey (UHB),PIONEER, 2023.

import sys, csv, re

codes = [{"code":"E12","system":"icd10"},{"code":"E120","system":"icd10"},{"code":"E120D","system":"icd10"},{"code":"E126","system":"icd10"},{"code":"E126D","system":"icd10"},{"code":"E128","system":"icd10"},{"code":"E129","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-of-various-forms-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-of-various-forms-malnutritionrelated---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-of-various-forms-malnutritionrelated---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-of-various-forms-malnutritionrelated---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
