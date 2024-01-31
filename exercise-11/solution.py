from operator import itemgetter

def alphabetize_names(PEOPLE) -> list[dict]:

    return sorted(PEOPLE, key = lambda person: (person['last'], person['first']))


if __name__ == "__main__":

    PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
              {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
              {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
            ]
    
    print(alphabetize_names(PEOPLE))

    # alternate implementation
    print(sorted(PEOPLE, key = itemgetter("last", "first")))
