'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def overlaps(range1, range2):
    if range1[1] <= range2[0]:
        return False
    if range2[1] <= range1[0]:
        return False
    return True

def min_rooms_required(lectures):
    '''O(N^2)'''
    N = len(lectures)
    lectures = sorted(lectures)
    rooms = [None] * N
    for i in range(N):
        available_rooms = set(range(N))
        # elminate used rooms
        for j in range(i):
            if overlaps(lectures[i], lectures[j]):
                available_rooms.remove(rooms[j])
        # use the first still-available room
        rooms[i] = min(available_rooms)
    return max(rooms) + 1

print(min_rooms_required([(30, 75), (0, 50), (60, 150)]))
