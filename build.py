import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def solution_asc(dic):
    dc_sort = sorted(dic.items(),key = operator.itemgetter(0),reverse = False)
    return dc_sort

print solution_asc(d)


def solution_desc(dic):
    dc_sort = sorted(dic.items(),key = operator.itemgetter(0),reverse = True)
    return dc_sort

print solution_desc(d)
