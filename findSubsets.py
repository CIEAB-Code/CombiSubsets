from itertools import combinations
import time


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


if __name__ == "__main__":
    num = 16
    lst = combinations(range(1, num + 1), 4)
    lstSets = [set(i) for i in lst]
    print(f"LENGTH: {len(lstSets)}")
    print(findSubsets(lstSets))
