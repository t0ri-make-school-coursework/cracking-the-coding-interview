import itertools
# 8.4
# Power Set
# Write a method to return all subsets of a set.

def power_set_pythonic():
    a_set = {"a", "b", 1, 2}
    data = itertools.combinations(a_set, 2)
    subsets = set(data)
    return subsets


def power_set(current, subset):
    if subset:
        return power_set(current, subset[1:]) + power_set(current + [subset[0]], subset[1:])
    return [current]


if __name__ == "__main__":
    # print(power_set_pythonic())
    print(power_set([], [4, 5, 6]))