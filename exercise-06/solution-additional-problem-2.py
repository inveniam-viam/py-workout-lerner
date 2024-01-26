
# desired behavior 

# transposer(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])
# returns ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']

def transposer(in_list: list[str]):

    # be careful - passing in a mutable type so avoid side-effects

    out_list: list[str] = []

    split_words = [s.split() for s in in_list]

    transposed = zip(*split_words)

    out_list = [' '.join(words) for words in transposed]

    return out_list



print(transposer(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
