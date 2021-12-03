input = open("input.txt")
linesOfVents = input.readlines();

class Map:
  def __init__(self, x, y):
    self.fields = []
    for i in range(y):
      self.fields.append([0] * x)

  def addLine(self, x1, y1, x2, y2, drawDiagonal = True):
    # horizontal
    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        self.fields[y][x1] += 1

    # vertical
    elif y1 == y2:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        self.fields[y1][x] += 1

    # diagonal
    elif drawDiagonal:
      x = x1
      y = y1
      self.fields[y][x] += 1
      while x != x2 and y != y2:
        x = x + 1 if x < x2 else x - 1
        y = y + 1 if y < y2 else y - 1
        self.fields[y][x] += 1

  
  def countDangerAreas(self):
    count = 0
    for row in self.fields:
      for field in row:
        if field > 1:
          count += 1
    return count

x = 0
y = 0
for i in range(len(linesOfVents)):
  line = linesOfVents[i]
  line = line.strip().split(' -> ')
  line[0] = line[0].split(',')
  line[1] = line[1].split(',')
  line = [int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])]
  linesOfVents[i] = line

  x = line[0] if line[0] > x else x
  x = line[2] if line[2] > x else x
  y = line[1] if line[1] > y else y
  y = line[3] if line[3] > y else y

map = Map(x + 1, y + 1)
for line in linesOfVents:
  map.addLine(*line, False)

print("part one:", map.countDangerAreas())

map = Map(x + 1, y + 1)
for line in linesOfVents:
  map.addLine(*line)

print("part two:", map.countDangerAreas())
