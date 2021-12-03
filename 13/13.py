import math

input = open("input.txt")
lines = input.readlines()

coordinates = []
foldingInstructions = []

width = 0
height = 0
for line in lines:
  line.strip()
  if 'fold' in line:
    line = line[11:len(line)]
    foldingInstruction = {'value': int(line[2:len(line)]), 'along': line[0]}
    foldingInstructions.append(foldingInstruction)
    continue

  coordinate = line.split(',')
  if len(coordinate) == 2:
    coordinates.append([int(coordinate[0]), int(coordinate[1])])
    width = int(coordinate[0]) if int(coordinate[0]) > width else width
    height = int(coordinate[1]) if int(coordinate[1]) > height else height

width += 1
height += 1

width  = 655 * 2 + 1
height = 447 * 2 + 1


def fold(foldingInstruction, currentCoordinates):
  global width
  global height
  newCoordinates = []

  for coordinate in currentCoordinates:
    if foldingInstruction['along'] == 'x':
      if coordinate[0] < foldingInstruction['value'] and not coordinate in newCoordinates:
        newCoordinates.append(coordinate.copy())
      elif not coordinate in newCoordinates:
        newCoordinate = coordinate.copy()
        newCoordinate[0] = width - (newCoordinate[0] + 1)
        if not newCoordinate in newCoordinates and newCoordinate[0] != foldingInstruction['value']:
          newCoordinates.append(newCoordinate)

    elif foldingInstruction['along'] == 'y':
      if coordinate[1] < foldingInstruction['value'] and not coordinate in newCoordinates:
        newCoordinates.append(coordinate.copy())
      elif not coordinate in newCoordinates:
        newCoordinate = coordinate.copy()
        newCoordinate[1] = height - (newCoordinate[1] + 1)
        if not newCoordinate in newCoordinates and newCoordinate[1] != foldingInstruction['value']:
          newCoordinates.append(newCoordinate)

  if foldingInstruction['along'] == 'x':
    width = foldingInstruction['value']
  elif foldingInstruction['along'] == 'y':
    height = foldingInstruction['value']

  return newCoordinates

def printMap():
  map = []
  for y in range(height):
    map.append([])
    for x in range(width):
      map[y].append('.')

  for coordinate in coordinates:
    map[coordinate[1]][coordinate[0]] = '#'

  for row in map:
    print(''.join(row))

  print()

for foldingInstruction in foldingInstructions:
  coordinates = fold(foldingInstruction, coordinates)

printMap()
