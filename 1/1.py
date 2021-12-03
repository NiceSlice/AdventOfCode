input = open("input.txt")
numbers = input.readlines();
lastNumber = int(numbers[0]);
count = 0

for i in range(1, len(numbers)):
  number = int(numbers[i])
  if lastNumber < number:
    count += 1
  lastNumber = number
print("part one:", count)

count = 0

lastWindow = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
for i in range(1, len(numbers) - 2):
  window = int(numbers[i]) + int(numbers[i + 1]) + int(numbers[i + 2])
  if (lastWindow < window):
    count += 1
  lastWindow = window

print("part two:", count)
