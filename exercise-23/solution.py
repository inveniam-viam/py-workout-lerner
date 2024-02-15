# Solution to main problem from Exercise 23

import glob
import json
from collections import defaultdict

def print_scores(dir_name: str):

    subject_dict = defaultdict(list)

    for file in glob.glob(f"{dir_name}/*.json"):

        with open(file, "r") as f:

            data = json.load(f)

            for item in data:

                for k, v in item.items():

                    subject_dict[k].append(v)
    
    print(file)

    for k, v in subject_dict.items():

        print(f"{k}: min {min(v)}, max {max(v)}, average {sum(v)/len(v): .1f}")


if __name__ == "__main__":

    print_scores("./")
        
