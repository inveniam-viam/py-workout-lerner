from operator import itemgetter
def format_sort_records(leaders_list):

    for person in sorted(leaders_list, key = itemgetter(1, 0)):

        print(f"{person[1]:10}{person[0]:10}{person[2]:5.2f}")


PEOPLE = [('Donald', 'Trump', 7.85),
         ('Vladimir', 'Putin', 3.626),
         ('Jinping', 'Xi', 10.603)]

format_sort_records(PEOPLE)
