'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

def itinerary_backtrack(legs, start):
    '''Each element of legs is a tuple of (start_city, end_city).
    There can be repeats in @legs.
    Returns a list of len(legs)+1 cities.
    '''
    if not legs:
        return [start]

    for i in range(len(legs)):
        leg = legs[i]
        if leg[0] != start:
            continue

        path = itinerary_backtrack(legs[0:i] + legs[i+1:], leg[1])
        if path is not None:
            return [leg[0]] + path

    return None  # failure

def itinerary(legs, start):
    legs = sorted(legs)
    return itinerary_backtrack(legs, start)

assert itinerary([('SFO','HKO'), ('YYZ','SFO'), ('YUL','YYZ'), ('HKO','ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None
assert itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') == ['A', 'B', 'C', 'A', 'C']
assert itinerary([('A', 'B'), ('A', 'B'), ('B', 'A'), ('B', 'A')], 'A') == ['A', 'B', 'A', 'B', 'A']
