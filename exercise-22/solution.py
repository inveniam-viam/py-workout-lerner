import csv

def passwd_to_csv(in_file: str, out_file: str):

    """Transfer the user name and user ids to a csv with tab delimiting"""

    with open(in_file, "r", encoding = "utf-8") as infile, open(out_file, "w", encoding = "utf-8") as outfile:

        writing = csv.writer(outfile, delimiter = "\t")

        for line in infile:

            if not line.startswith("#"):

                writing.writerow([line.split(":")[0], line.split(":")[2]])

passwd_to_csv("input.txt", "test-out.csv")

        
# alt 

def pass_to_csv(in_file: str, out_file: str):

    """same thing as above, but exclusively using csv.reader and csv.writer"""

    with open(in_file, "r", encoding = "utf-8", newline = '\n') as infile, open(out_file, "w", newline = '\n', encoding = "utf-8") as outfile:

        reading = csv.reader(infile, delimiter = ":")

        writing = csv.writer(outfile, delimiter = "\t")

        for row in reading:

            if not row[0].startswith("#"):

                writing.writerow([row[0], row[2]])

