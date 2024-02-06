# Solution to Main Problem from Exercise 19

def user_information_from_etcpasswd(in_filepath: str) -> dict:

    user_info: dict = {}

    with open(in_filepath, "r", encoding = "utf-8") as f:

        for line in f:

            if not line.startswith(("#", '\n')):

                username = line.split(":")[0]
                user_id = line.split(":")[2]

                user_info[username] = user_id 
    
    return user_info
        

print(user_information_from_etcpasswd("/Users/jarwind/Work/python-rushmore/reuven-lerner/py-workout-lerner/exercise-19/passwd.txt"))

