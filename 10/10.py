import math

input = open("input.txt")
lines = input.readlines()

brackets = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

corruptedScores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

scores = {  
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def getCorruptedScore(line):
  stack = []

  for bracket in line:
    # opening bracket
    if bracket in brackets:
      stack.append(bracket)

    # closing bracket
    elif brackets[stack.pop()] != bracket:
      return corruptedScores[bracket]
  return 0

def getScore(line):
  stack = []

  for bracket in line:
    # opening bracket
    if bracket in brackets:
      stack.append(bracket)

    # closing bracket
    elif brackets[stack.pop()] != bracket:
      return corruptedScores[bracket]
  
  score = 0
  while len(stack) > 0:
    score *= 5
    score += scores[brackets[stack.pop()]]
  return score


corruptedScoreTotal = 0
allScores = []
for line in lines:
  line = line.strip()
  corruptedScore = getCorruptedScore(line)
  corruptedScoreTotal += corruptedScore
  if corruptedScore == 0:
    allScores.append(getScore(line))

print("part one:", corruptedScoreTotal)

allScores.sort()
middleIndex = math.floor(len(allScores)/2)
print("part two:", allScores[middleIndex])
