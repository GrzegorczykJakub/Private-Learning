from collections import defaultdict

map = defaultdict(set)
with open('input.txt') as f:
    for line in f:
        a, b = line.strip().split('-')
        if a != 'end' and b != 'start':
            map[a].add(b)
        if a != 'start' and b != 'end':
            map[b].add(a)
from collections import Counter

def get_options(pos, route, part_2=False):
    c = Counter([c for c in route if c != 'start' and c.lower() == c])
    if part_2 and 2 not in set(c.values()):
        return map[pos]
    else:
        visited = {p for p in route if p.lower() == p}
        return map[pos] - visited
def get_routes(pos, route=None, part_2=False):
    if route is None:
        route = []
    route.append(pos)
    if pos == 'end':
        yield route
        return
    options = get_options(pos, route, part_2)
    if len(options) == 0:
        return
    for next_pos in options:
        yield from get_routes(next_pos, list(route), part_2)


print("Part 1:")
print(len(list(get_routes('start'))))
print("Part 2:")
print(len(list(get_routes('start', part_2=True))))

