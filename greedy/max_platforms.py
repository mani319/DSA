"""
Given arrival and departure times of all trains that reach a railway station,
find the minimum no of platforms required for station so that no train waits.
We are given two arrays which represent arrival and departure times of trains.

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

The idea is to consider all events in sorted order.
Once we have all events in sorted order,
    we can trace the number of trains at any time keeping track of trains
        that have arrived, but not departed.
"""


def maxPlatformsNeeded(arr, dep):
    n = len(arr)

    platforms, max_platforms = 1, 1
    i, j = 1, 0
    while(i < n and j < n):
        if(arr[i] < dep[j]):
            platforms += 1
            max_platforms = max(platforms, max_platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    print(maxPlatformsNeeded(arr, dep))
