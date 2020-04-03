first = ['A', 'C', 'T', 'G', 'A', 'A', 'C', 'T', 'G', 'A']
second = ['seT', 'G', 'A', 'C', 'T', 'g', 'G', 'A', 'C', 'T']


def mistake(a, b):
    double = zip(a, b)
    correct = 0
    i = 0
    index = 0

    for (item1, item2) in double:
        if ((item1 == 'A' and item2 == 'T') or (item1 == 'T' and item2 == 'A') or (item1 == 'C' and item2 == 'G') or (item1 == 'G' and item2 == 'C')):
            correct += 1
        else:
            index = i
        i += 1

    if (len(double) == correct):
        return 'Seems correct'
    else:
        return 'Mistake is at position: ' + str(index+1)


print(mistake(first, second))