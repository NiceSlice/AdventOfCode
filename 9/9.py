input = open("input.txt")
map = input.readlines()

for y in range(len(map)):
  map[y] = map[y].strip()

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.coordinate = str(x) + '|' + str(y)
    self.value = int(map[y][x])

def getAdjacentPoints(point):
  x = point.x
  y = point.y
  adjacentPoints = []
  if x > 0:
    adjacentPoints.append(Point(x-1, y))
  if x + 1 < len(map[0]):
    adjacentPoints.append(Point(x+1, y))
  if y > 0:
    adjacentPoints.append(Point(x, y-1))
  if y + 1 < len(map):
    adjacentPoints.append(Point(x, y+1))
  return adjacentPoints

def isLowPoint(x, y):
  currentPoint = Point(x, y)
  adjacentPoints = getAdjacentPoints(currentPoint)

  for point in adjacentPoints:
    if point.value <= currentPoint.value:
      return False
  return True

risk = 0
lowPoints = []
for y in range(len(map)):
  for x in range(len(map[0])):
    if isLowPoint(x, y):
      risk += int(map[y][x]) + 1
      lowPoints.append(Point(x, y))

print("part one:", risk)


def findBasin(currentPoint, basin):
  basin[currentPoint.coordinate] = True

  adjacentPoints = getAdjacentPoints(currentPoint)
  for point in adjacentPoints:
    if not point.coordinate in basin:
      pointInBasin = int(point.value) != 9
      basin[point.coordinate] = pointInBasin
      if pointInBasin:
        basin = findBasin(point, basin)

  return basin

def findBasinSize(basin):
  size = 0
  for coordinate in basin:
    if basin[coordinate]:
      size += 1
  return size

largestBasins = [0, 0, 0]

for lowPoint in lowPoints:
  newBasinSize = findBasinSize(findBasin(lowPoint, {}))

  for i in range(len(largestBasins)):
    if newBasinSize > largestBasins[i]:
      largestBasins[i] = newBasinSize
      largestBasins.sort()
      break

print("part two:", largestBasins[0] * largestBasins[1] * largestBasins[2])
