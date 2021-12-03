input = open("input.txt")
lanternfish = input.readlines()[0].split(',')

def passDay(yesterdayFish):
  fish = [0] * 9
  for timer in range(len(yesterdayFish)):
    if timer == 0:
      fish[6] += yesterdayFish[timer]
      fish[8] += yesterdayFish[timer]
    else:
      fish[timer-1] += yesterdayFish[timer]
  return fish

def countFish(fish):
  count = 0
  for timer in range(len(fish)):
    count += fish[timer]
  return count

fish = [0] * 9
for i in range(len(lanternfish)):
  fish[int(lanternfish[i])] += 1

for i in range(80):
  fish = passDay(fish)

print("part one:", countFish(fish))

fish = [0] * 9
for i in range(len(lanternfish)):
  fish[int(lanternfish[i])] += 1

for i in range(256):
  fish = passDay(fish)

print("part two:", countFish(fish))
