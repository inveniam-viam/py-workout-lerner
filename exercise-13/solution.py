from operator import itemgetter

def format_sort_records(leaders_list):

    out_list: list[str] = []

    for person in sorted(leaders_list, key = itemgetter(1, 0)):

        out_list.append(f"{person[1]:10}{person[0]:10}{person[2]:5.2f}")
    
    return '\n'.join(out_list)


PEOPLE = [('Donald', 'Trump', 7.85),
         ('Vladimir', 'Putin', 3.626),
         ('Jinping', 'Xi', 10.603)]

print(format_sort_records(PEOPLE))
