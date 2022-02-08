from itertools import combinations
import cProfile, pstats, io


def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner


@profile
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


@profile
def findSubsetsWhile(lst_sets):
    last_changed = lst_sets.copy()
    to_change = lst_sets.copy()
    index = 0
    elem_left = len(to_change)
    while elem_left > index:
        rem = 0
        for i in list(range(elem_left)):
            if i == elem_left - (index + 1):
                break
            elif len(last_changed[index].intersection(last_changed[index + i + 1])) >= 3:
                del to_change[index + i + 1 - rem]
                rem += 1
        index += 1
        elem_left -= rem
        last_changed = to_change.copy()
    print("WHILE LENGTH", len(last_changed))
    return last_changed


if __name__ == "__main__":
    num = 16
    lst = combinations(range(1, num + 1), 4)
    lstSets = [set(i) for i in lst]
    print(f"LENGTH: {len(lstSets)}")
    print(findSubsetsWhile(lstSets))
