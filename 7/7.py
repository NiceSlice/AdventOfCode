import math

input = open("input.txt")
crabPositions = input.readlines()[0].split(',')
max = 0

for i in range(len(crabPositions)):
  crabPositions[i] = int(crabPositions[i])
  max = crabPositions[i] if crabPositions[i] > max else max

necessaryFuel = -1

for i in range(max):
  fuel = 0
  for position in crabPositions:
    fuel += abs(position - i)
  necessaryFuel = fuel if fuel < necessaryFuel or necessaryFuel == -1 else necessaryFuel

print("part one:", necessaryFuel)

necessaryFuel = -1

def getFuel(steps):
  if steps % 2 == 0:
    return round((steps + 1) * (steps / 2))
  else:
    return (steps + 1) * (math.floor(steps / 2)) + (math.floor(steps / 2) + 1)

for i in range(max):
  fuel = 0
  for position in crabPositions:
    fuel += getFuel(abs(position - i))
    """
    5
    3
    
    5 + 4 + 3 + 2 + 1 = 15
    4 + 3 + 2 + 1 = 10
    3 + 2 + 1 = 6
    2 + 1 = 3
    1 = 1
    """
  necessaryFuel = fuel if fuel < necessaryFuel or necessaryFuel == -1 else necessaryFuel

print("part two:", necessaryFuel)
