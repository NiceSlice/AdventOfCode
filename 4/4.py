input = open("input.txt")
allRows = input.readlines();
numbers = allRows.pop(0).split(',')

class Board:
  def __init__(self, rows, n):
    self.bingo = False
    self.fields = []
    row = []
    for i in range(len(rows)):
      row.append([rows[i], False])
      if i % n == 4:
        self.fields.append(row)
        row = []

boards = []
n = 5

i = 0
while i < len(allRows):
  if allRows[i] == '\n':

    rows = []
    for j in range(1, n+1):
      rows += allRows[i + j].strip().split()
    i += n + 1

    newBoard = Board(rows, n)
    boards.append(newBoard)



def drawNumber(boards, number):
  for board in boards:
    if board.bingo == False:
      for row in board.fields:
        for field in row:
          if field[0] == number:
            field[1] = True
  
def bingo(boards, n):
  result = -1
  for i in range(len(boards)):
    if boards[i].bingo == False:
      for row in boards[i].fields:
        bingo = True
        for field in row:
          if field[1] == False:
            bingo = False
        if bingo == True:
          boards[i].bingo = True
          result = i

      #columns
      for x in range(n):
        bingo = True
        for y in range(n):
          if boards[i].fields[y][x][1] == False:
            bingo = False
        if bingo == True:
          boards[i].bingo = True
          result = i
  
  return result

def getScore(board, lastCallednumber):
  sum = 0
  for row in board.fields:
    for field in row:
      if field[1] == False:
        sum += int(field[0])
  return sum * lastCallednumber


firstWinner = -1
currentWinner = -1
lastWinner = -1
lastNumber = -1
boardCount = len(boards)

for number in numbers:
  drawNumber(boards, number)
  currentWinner = bingo(boards, n)
  if currentWinner != -1:
    boards[currentWinner].bingo = True
    lastWinner = currentWinner
    lastNumber = number

    if firstWinner == -1:
      firstWinner = currentWinner
      print("part one:", getScore(boards[firstWinner], int(number)))

print("part two:", getScore(boards[lastWinner], int(lastNumber)))
