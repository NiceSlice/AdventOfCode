input = open("input.txt")
commands = input.readlines();

horizontalPosition = 0
depth = 0

for command in commands:
  command = command.split(' ')
  if command[0] == 'forward':
    horizontalPosition += int(command[1])
  elif command[0] == 'up':
    depth -= int(command[1])
  else:
    depth += int(command[1])

print("part one:", horizontalPosition * depth)

horizontalPosition = 0
depth = 0
aim = 0

for command in commands:
  command = command.split(' ')
  if command[0] == 'forward':
    horizontalPosition += int(command[1])
    depth += aim * int(command[1])
  elif command[0] == 'up':
    aim -= int(command[1])
  else:
    aim += int(command[1])

print("part two:", horizontalPosition * depth)
