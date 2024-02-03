# Solution to 14.1

from datetime import date

logins = dict(jared = "jared123", sean = "diane123", oli = "larizzelle123")

def login():

    print("Welcome to the XYZ Portal: ")

    login_attempts: int = 0

    while username := input("Please enter your username: "):

        if username in logins:

            password: str = input("Enter your password: ")

            if password == logins[username]:

                print("Logged in successfully!")
                break
            else:

                print("Your password is incorrect. Please try again.")
            
            login_attempts += 1

            if login_attempts == 4:

                print("You have exhausted your 4 login attempts.")
                break


# login()

# 14.2
            
#  the fact we have to use str keys makes this annoying
weather_dict: dict[str, int] = {
    "Feb 1": 30,
    "Feb 2" : 33,
    "Feb 3": 40,
    "Feb 4": 45,
    "Feb 5": 50,
    "Feb 6": 31,
    "Feb 7": 32
}

def get_weather():

    while user_date := input("Please enter date as (Feb 3): "):

        day_before :str = f"{user_date.split()[0]} {int(user_date.split()[1]) - 1}"

        day_after: str = f"{user_date.split()[0]} {int(user_date.split()[1]) + 1}"

        if user_date in weather_dict:

            if day_before in weather_dict:

                print(f"The weather the day before on {day_before} was {weather_dict.get(day_before, 'Unavailable')}")
            
            print(f"The weather on {user_date} is {weather_dict.get(user_date, 'Unavailable')}")

            if day_after in weather_dict:

                print(f"The weather on {day_after} is {weather_dict.get(day_after, 'Unavailable')}")
        
        break

# get_weather()
    
# 14.3

# use dt keys
    
birthdays: dict[str, str] = dict(me = "1997-10-05", mum = "1966-06-03",
                                 dad = "1966-11-09", bro = "1994-12-30", janet = "1997-07-12",)

# too lazy to write the dates as datetime objects so converting them here

def get_age_days():

    """Function to compute a person's age in days. 
    the person and their birthday are stored in a dictionary."""

    todayy = date.today()

    while who := input("Whose age in days would you like to know? "):

        if who in birthdays:

            print(f"{who} is {(todayy - date.fromisoformat(birthdays[who])).days} days old as of today")
        
        else:
            print("Couldn't find that person. Try again later.")
            break

get_age_days()
    


    


