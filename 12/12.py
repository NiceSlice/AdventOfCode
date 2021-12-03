input = open("input.txt")
paths = input.readlines()
map = {'visitedSmallCaveTwice': False}

for path in paths:
  path = path.strip().split('-')

  if path[0] in map and not path[1] in map[path[0]] and path[0] != 'end' and path[1] != 'start':
    map[path[0]]['caves'].append(path[1])
  elif path[0] != 'end' and path[1] != 'start':
    map[path[0]] = {'caves': [path[1]], 'visited': 0}
  if path[1] in map and not path[0] in map[path[1]] and path[1] != 'end' and path[0] != 'start':
    map[path[1]]['caves'].append(path[0])
  elif path[1] != 'end' and path[0] != 'start':
    map[path[1]] = {'caves': [path[0]], 'visited': 0}


def isBigCave(cave):
  if cave == cave.upper():
    return True
  return False


def getMapWithoutCave(removedCave, currentMap):
  newMap = {'visitedSmallCaveTwice': currentMap['visitedSmallCaveTwice']}
  for cave in currentMap:
    if cave != removedCave and cave != 'visitedSmallCaveTwice':
      newMap[cave] = {'caves': [], 'visited': currentMap[cave]['visited']}
      for dest in currentMap[cave]['caves']:
        if dest != removedCave:
          newMap[cave]['caves'].append(dest)
  return newMap


def increaseVisited(cave, currentMap):
  pass


def move(currentCave='start', currentMap=map, partOne=True, path='start,'):
  if currentCave == 'end':
    return 1

  if len(currentMap[currentCave]) == 0:
    return 0

  count = 0
  for nextCave in currentMap[currentCave]['caves']:
    if isBigCave(currentCave):
      if partOne:
        count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')
      else:
        if isBigCave(nextCave) or nextCave == 'end':
          count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')
        elif not currentMap['visitedSmallCaveTwice']:
          count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')
        elif currentMap[nextCave]['visited'] == 0:
          count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')

    else:
      if partOne:
        count += move(nextCave, getMapWithoutCave(currentCave, currentMap), partOne, path+nextCave+',')

      else:
        currentMap[currentCave]['visited'] += 1
        if currentMap[currentCave]['visited'] == 2 and not currentMap['visitedSmallCaveTwice']:
          currentMap['visitedSmallCaveTwice'] = True
          count += move(nextCave, getMapWithoutCave(currentCave, currentMap), partOne, path+nextCave+',')

        else:
          if isBigCave(nextCave) or nextCave == 'end':
            count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')
          elif not currentMap['visitedSmallCaveTwice']:
            count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')
          elif currentMap[nextCave]['visited'] == 0:
            count += move(nextCave, currentMap.copy(), partOne, path+nextCave+',')

        currentMap[currentCave]['visited'] -= 1

  return count

print("part one:", move())
print("part two:", move('start', map, False))
