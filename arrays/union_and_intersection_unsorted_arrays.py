

def find_union_in_unsorted(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    result = []
    hash_map = {}

    for i in range(n1):
        hash_map[arr1[i]] = 1
        result.append(arr1[i])

    for i in range(n2):
        if(arr2[i] not in hash_map.keys()):
            result.append(arr2[i])

    return result


def find_intersection_in_unsorted(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    result = []
    hash_map = {}

    for i in range(n1):
        hash_map[arr1[i]] = 1

    for i in range(n2):
        if(arr2[i] in hash_map.keys()):
            result.append(arr2[i])

    return result


def find_union_and_intersection_in_unsorted(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    union = []
    intersection = []
    hash_map = {}

    for i in range(n1):
        hash_map[arr1[i]] = 1
        union.append(arr1[i])

    for i in range(n2):
        if(arr2[i] not in hash_map.keys()):
            union.append(arr2[i])
        else:
            intersection.append(arr2[i])

    return union, intersection


if __name__ == "__main__":
    arr1 = [7, 1, 5, 2, 3, 6]
    arr2 = [3, 8, 6, 20, 7]

    # Find Union in sorted array
    union = find_union_in_unsorted(arr1, arr2)
    print(union, )

    # Find Intersection in sorted array
    intersection = find_intersection_in_unsorted(arr1, arr2)
    print(intersection, )

    # Find Union and Intersection in sorted array
    union1, intersection1 = find_union_and_intersection_in_unsorted(arr1, arr2)
    print(union1, )
    print(intersection1, )
