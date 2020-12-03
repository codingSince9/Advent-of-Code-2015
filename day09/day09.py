import itertools

routes = {}
cities = []

for route in open("day09.txt", "r"):
    connection = route.split()[0] + ',' + route.split()[2]
    routes[connection] = int(route.split()[4])

for key in routes.keys():
    for city in key.split(','):
        if city not in cities:
            cities.append(city)

combinations = list(itertools.permutations(cities))

shortestDistance = 0
longestDistance = 0
for travelPath in list(itertools.permutations(cities)):
    distance = 0
    twoCities = []
    for city in travelPath:
        cityToRemove = city

        if len(twoCities) == 0:
            twoCities.append(city)
            continue
        elif len(twoCities) < 2:
            twoCities.append(city)
        elif len(twoCities) < 3:
            twoCities.pop(0)
            twoCities.append(city)

        try:
            distance += routes[','.join(twoCities)]
        except KeyError:
            twoCities.reverse()
            distance += routes[','.join(twoCities)]
            twoCities.reverse()

    if shortestDistance == 0:
        shortestDistance = distance
    elif shortestDistance > distance:
        shortestDistance = distance

    if longestDistance == 0:
        longestDistance = distance
    elif longestDistance < distance:
        longestDistance = distance

print("Part 1:", shortestDistance)
print("Part 2:", longestDistance)
