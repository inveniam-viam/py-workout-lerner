# Solutions to additional problems - Exercise 17

# Problems 17.1 and 17.2 bundled together

# the sample-log.txt file is just one that I asked ChatGPT to generate for me

import os


def log_file_addresses_responses(log_file):

    ip_addresses: set = set()

    response_codes: set = set()

    with open(log_file, "r", encoding = "utf-8") as f:

        for line in f:

            ip_addresses.add(line.split()[0])
            response_codes.add(line.split()[8])
    
    return ip_addresses, response_codes



ips, codes = log_file_addresses_responses("sample-log.txt")

print(ips)
print(codes)


# 17.3

def distinct_exts():

    distinct_extensions = set()

    files = os.listdir()

    for file in files:

        distinct_extensions.add(os.path.splitext(file))

    
    return distinct_extensions

