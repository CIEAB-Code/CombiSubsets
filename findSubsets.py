from itertools import combinations


def findSubsets(setList):
    last_changed = setList.copy()
    for i, a in enumerate(last_changed):
        if a == {0}:
            continue
        for ind, b in enumerate(last_changed[i + 1:]):
            if len(a.intersection(b)) >= 3:
                last_changed[ind + 1 + i] = {0}

    last_changed = list(filter(lambda x: x != {0}, last_changed))
    print(f"Final Length: {len(last_changed)}")
    return last_changed


def findSubsetsWhile(lstSets):
    last_changed = lstSets.copy()
    to_change = lstSets.copy()
    index = 0
    eleLeft = len(to_change)
    while eleLeft > index:
        rem = 0
        for i in list(range(eleLeft)):
            if i == len(last_changed)-(index+1):
                break
            elif len(last_changed[index].intersection(last_changed[index + i + 1])) >= 3:
                to_change.remove(last_changed[index+i+1])
                rem += 1
        index += 1
        eleLeft -= rem
        last_changed = to_change.copy()
    print("WHILE LENGTH", len(last_changed))
    return last_changed


if __name__ == "__main__":
    num = 16
    lst = combinations(range(1, num + 1), 4)
    lstSets = [set(i) for i in lst]
    print(f"LENGTH: {len(lstSets)}")
    print(findSubsetsWhile(lstSets))
