input = open("input.txt")
map = input.readlines()

for y in range(len(map)):
  map[y] = map[y].strip()
  row = map[y]
  map[y] = []
  for x in range(len(row)):
    map[y].append({'energy': int(row[x]), 'flashed': False})

def printMap():
  for y in range(len(map)):
    row = ''
    for x in range(len(map[y])):
      row += str(map[y][x]['energy'])
    print(row)
  print()

def clear():
  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x]['flashed'] == True:
        map[y][x]['flashed'] = False
        map[y][x]['energy'] = 0

def countSurroundingFlashed(x, y):
  count = 0

  for yi in range(max(y - 1, 0), min(y + 2, len(map))):
    for xi in range(max(x - 1, 0), min(x + 2, len(map[y]))):
      if (yi != y or xi != x) and map[yi][xi]['flashed'] == True:
        count += 1

  return count

def step():
  flashes = 0
  flashesTemp = flashes

  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x]['energy'] <= 9:
        map[y][x]['energy'] += 1
      if map[y][x]['energy'] == 10:
        map[y][x]['flashed'] = True
        map[y][x]['energy'] -= 9
        flashes += 1

  while flashesTemp != flashes:
    flashesTemp = flashes
    for y in range(len(map)):
      for x in range(len(map[y])):
        if not map[y][x]['flashed']:
          surroundingFlashed = countSurroundingFlashed(x, y);
          if map[y][x]['energy'] + surroundingFlashed > 9:
            map[y][x]['flashed'] = True
            map[y][x]['energy'] -= 9
            flashes += 1
  
  for y in range(len(map)):
    for x in range(len(map[y])):
      surroundingFlashed = countSurroundingFlashed(x, y);
      map[y][x]['energy'] += surroundingFlashed

  clear()
  return flashes

steps = 0
totalFlashes = 0
synchronized = False

while not synchronized:
  currentFlashes = step()
  totalFlashes += currentFlashes
  steps += 1
  if steps == 100:
    print("part one:", totalFlashes)
  if currentFlashes == len(map) * len(map[y]):
    synchronized = True
    print("part two:", steps)
