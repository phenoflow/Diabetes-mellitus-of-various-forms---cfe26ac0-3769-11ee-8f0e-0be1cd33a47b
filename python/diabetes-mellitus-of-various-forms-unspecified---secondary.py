# Prof. Elizabeth Sapey (UHB),PIONEER, 2023.

import sys, csv, re

codes = [{"code":"E106","system":"icd10"},{"code":"E106D","system":"icd10"},{"code":"E108","system":"icd10"},{"code":"E116","system":"icd10"},{"code":"E116D","system":"icd10"},{"code":"E118","system":"icd10"},{"code":"E118D","system":"icd10"},{"code":"E13","system":"icd10"},{"code":"E130","system":"icd10"},{"code":"E130D","system":"icd10"},{"code":"E136","system":"icd10"},{"code":"E138","system":"icd10"},{"code":"E139","system":"icd10"},{"code":"E139D","system":"icd10"},{"code":"E14","system":"icd10"},{"code":"E140","system":"icd10"},{"code":"E146","system":"icd10"},{"code":"E146D","system":"icd10"},{"code":"E148","system":"icd10"},{"code":"E149","system":"icd10"},{"code":"E149D","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-of-various-forms-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-of-various-forms-unspecified---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-of-various-forms-unspecified---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-of-various-forms-unspecified---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
