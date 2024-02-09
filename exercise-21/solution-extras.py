# Solutions to additional problems from Exercise 21
import hashlib
import os
import arrow
# Solution to 21.1

def file_hashing(in_filepath: str):

    hash_dict: dict = {}

    for file in os.listdir(in_filepath):

        if os.path.splitext(file)[-1] == ".txt":

            hash_val = hashlib.md5()

            with open(file, "r", encoding = "utf-8") as f:

                for line in f:

                    hash_val.update(line.encode(encoding = "utf-8"))
                
            hash_dict[file] = hash_val.digest()
    
    return hash_dict

# Solution to 12.2

def files_updates(in_filepath: str):

    for file in os.listdir(in_filepath):

        print(f"{file} was last updated {arrow.get(os.stat(file).st_mtime).humanize()}")


# Solution to 12.3
        
def response_codes(in_file: str) -> dict:

    out_dict: dict = {}

    with open(in_file, "r", encoding = "utf-8") as f:

        for line in f:

            potential_code = line.split()[8]

            if potential_code.isdigit():

                out_dict[potential_code] = out_dict.get(potential_code, 0) + 1
    
    return out_dict
