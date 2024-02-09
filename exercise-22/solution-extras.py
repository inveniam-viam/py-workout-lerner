# Solutions to additional problems
import csv
import random
# Solution to 12.1



# Solution to 12.2 

def dict_to_csv(in_dict: dict, out_file: str):

    """Write dictionary to csv file"""

    with open(out_file, "w", newline = "\n", encoding = "utf-8") as f:

        writer = csv.writer(f, delimiter = ',')

        for key, value in in_dict.items():

            writer.writerow([key, value, type(value)])

# Solution to 12.3


def create_and_compute_csv(in_out_file: str) :

    with open(in_out_file, "w", newline = "\n", encoding = "utf-8") as writ:

        writing = csv.writer(writ, delimiter = ",")

        # only going to write 10 lines

        for i in range(10):

            writing.writerow([random.randint(0, 100) for char in range(10)])

    with open(in_out_file, "r", newline = "\n", encoding = "utf-8") as read:

        row_sum: int = 0

        row_mean: float = 0

        reading = csv.reader(read, delimiter = ",")

        for row in reading:

            row_clean = [int(num) for num in row]

            row_sum += sum(row_clean)

            row_mean = row_sum / len(row)

            print(f"Sum of the line is {row_sum} and mean of the line is {row_mean:.2f}")

# create_and_compute_csv("sample-file-extras-3.csv")


        
    