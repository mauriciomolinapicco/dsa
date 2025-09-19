# problem 2418 return the names of the people sorted

def sortPeople(names, heights):
    n = len(names)
    pairs = {}
    for i in range(n):
        pairs[heights[i]] = names[i]

    heights.sort(reverse=True)
    res = []

    for height in heights:
        res.append(pairs[height])
    
    return res
