

def find_union_in_sorted(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    result = []
    i = j = 0
    while(i < n1 and j < n2):
        if(arr1[i] < arr2[j]):
            result.append(arr1[i])
            i += 1
        elif(arr1[i] > arr2[j]):
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    while(i < n1):
        result.append(arr1[i])
        i += 1

    while(j < n2):
        result.append(arr2[j])
        j += 1

    return result


def find_intersection_in_sorted(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    result = []
    i = j = 0
    while(i < n1 and j < n2):
        if(arr1[i] < arr2[j]):
            i += 1
        elif(arr1[i] > arr2[j]):
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    return result


def find_union_and_intersection_in_sorted(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    union = []
    intersection = []
    i = j = 0
    while(i < n1 and j < n2):
        if(arr1[i] < arr2[j]):
            union.append(arr1[i])
            i += 1
        elif(arr1[i] > arr2[j]):
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            intersection.append(arr1[i])
            i += 1
            j += 1

    while(i < n1):
        union.append(arr1[i])
        i += 1

    while(j < n2):
        union.append(arr2[j])
        j += 1

    return union, intersection


if __name__ == "__main__":
    arr1 = [1, 2, 3, 5, 7, 8, 9, 11]
    arr2 = [2, 3, 4, 6, 7, 8, 10, 11]

    # Find Union in sorted array
    union = find_union_in_sorted(arr1, arr2)
    print(union, )

    # Find Intersection in sorted array
    intersection = find_intersection_in_sorted(arr1, arr2)
    print(intersection, )

    # Find Union and Intersection in sorted array
    union1, intersection1 = find_union_and_intersection_in_sorted(arr1, arr2)
    print(union1, )
    print(intersection1, )
