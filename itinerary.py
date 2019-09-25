'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. All flights must be used in the itinerary.

For example, given the following list of flights:

HNL ➔ AKL
YUL ➔ ORD
ORD ➔ SFO
SFO ➔ HNL
and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL. (This also happens to be the actual itinerary for the trip I'm about to take.)

You should take some time to try to solve it on your own! Notice that a greedy solution won't work, since it's possible to have a cycle in the graph.
'''

def cities(legs, used_legs, path_prefix):
    '''Each element of legs is a tuple of (start_city, end_city).
    There can be repeats in @legs.
    Returns a list of len(legs)+1 cities.
    '''
    if len(path_prefix) == len(legs) + 1:
        return path_prefix  # success

    for i in range(len(legs)):
        if used_legs[i]:
            continue
        leg = legs[i]
        if leg[0] != path_prefix[-1]:
            continue

        # try this leg...
        path_prefix.append(leg[1])
        used_legs[i] = True

        # check for success
        path = cities(legs, used_legs, path_prefix)
        if path is not None:
            return path

        # undo this leg
        path_prefix.pop()
        used_legs[i] = False

    return None  # failure

print(cities([('HNL', 'AKL'), ('YUL', 'ORD'), ('ORD', 'SFO'), ('SFO', 'HNL')], [False] * 4, ['YUL']))
