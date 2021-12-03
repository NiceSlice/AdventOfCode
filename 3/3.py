input = open("input.txt")
numbers = input.readlines();

numberOfDigits = (len(numbers[0]) - 1)
bitTrack = [0] * numberOfDigits;

for number in numbers:
  for i in range(len(number)):
    if number[i] == '1':
      bitTrack[i] += 1

gammaRate = ''
epsilonRate = ''

for number in bitTrack:
  if number >= len(numbers)/2:
    gammaRate += '1'
    epsilonRate += '0'
  else:
    gammaRate += '0'
    epsilonRate += '1'

powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)
print("part one:", powerConsumption)


def mostCommonBit(numbers, i):
  bitTrack = 0
  for number in numbers:
    if number[i] == '1':
      bitTrack += 1

  if bitTrack >= len(numbers)/2:
    return "1"
  return "0"

oxygenGeneratorRating = -1
CO2ScrubberRating = -1
filterOxygen = list(numbers)
filterCO2 = list(numbers)

for digitIndex in range(numberOfDigits):
  mostCommonBitOxygen = mostCommonBit(filterOxygen, digitIndex)
  i = 0
  while i < len(filterOxygen):
    if filterOxygen[i][digitIndex] != mostCommonBitOxygen and oxygenGeneratorRating == -1:
      filterOxygen.remove(filterOxygen[i])
      i -= 1
    i += 1

  mostCommonBitCO2 = mostCommonBit(filterCO2, digitIndex)
  i = 0
  while i < len(filterCO2):
    if filterCO2[i][digitIndex] == mostCommonBitCO2 and CO2ScrubberRating == -1:
        filterCO2.remove(filterCO2[i])
        i -= 1
    i += 1

  if len(filterOxygen) == 1:
    oxygenGeneratorRating = filterOxygen[0]
  if len(filterCO2) == 1:
    CO2ScrubberRating = filterCO2[0]

lifeSupportRating = int(oxygenGeneratorRating, 2) * int(CO2ScrubberRating, 2)
print("part two:", lifeSupportRating)
