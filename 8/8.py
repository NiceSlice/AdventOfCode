input = open("input.txt")
notes = input.readlines()

count = 0

for entry in notes:
  outputValue = entry.split('|')[1].strip().split(' ')
  for digit in outputValue:
    if len(digit) in [2, 3, 4, 7]:
      count += 1

print("part one:", count)

numbersAsSegments = [
  'abcefg',
  'cf',
  'acdeg',
  'acdfg',
  'bcdf',
  'abdfg',
  'abdefg',
  'acf',
  'abcdefg',
  'abcdfg'
]


def decode(signals):
  taken = []
  pairs = []
  codes = {
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
    'f': [],
    'g': [],
  }

  for signal in signals:
    if len(signal) == 2:
      for char in signal:
        codes[char] = ['c', 'f']
        taken.append(char)
      pairs.append(taken[-2:len(taken)])
      break

  for signal in signals:
    if len(signal) == 3:
      for char in signal:
        if not char in taken:
          codes[char] = ['a']
          taken.append(char)
      break

  for signal in signals:
    if len(signal) == 4:
      for char in signal:
        if not char in taken:
          codes[char] = ['b', 'd']
          taken.append(char)
      pairs.append(taken[-2:len(taken)])
      break

  for signal in signals:
    if len(signal) == 7:
      for char in signal:
        if not char in taken:
          codes[char] = ['g', 'e']
          taken.append(char)
      pairs.append(taken[-2:len(taken)])
      break


  ###

  match = ''
  options = []
  for code in codes:
    if ('c' in codes[code] and 'f' in codes[code]) or ('b' in codes[code] and 'd' in codes[code]) or ('a' in codes[code]):
      match += code
    if 'g' in codes[code] and 'e' in codes[code]:
      options.append(code)

  for signal in signals:
    if sorted(signal) == sorted(match+options[0]):
      codes[options[0]] = ['g']
      codes[options[1]] = ['e']
      break
    elif sorted(signal) == sorted(match+options[1]):
      codes[options[1]] = ['g']
      codes[options[0]] = ['e']
      break

  ###

  match = ''
  options = []
  for code in codes:
    if ('g' in codes[code]) or ('b' in codes[code] and 'd' in codes[code]) or ('e' in codes[code]) or ('a' in codes[code]):
      match += code
    if 'c' in codes[code] and 'f' in codes[code]:
      options.append(code)

  for signal in signals:
    if sorted(signal) == sorted(match+options[0]):
      codes[options[0]] = ['f']
      codes[options[1]] = ['c']
      break
    elif sorted(signal) == sorted(match+options[1]):
      codes[options[1]] = ['f']
      codes[options[0]] = ['c']
      break

  ###

  match = ''
  options = []
  for code in codes:
    if ('e' in codes[code]) or ('f' in codes[code]) or ('c' in codes[code]) or ('g' in codes[code]) or ('a' in codes[code]):
      match += code
    if 'b' in codes[code] and 'd' in codes[code]:
      options.append(code)

  for signal in signals:
    if sorted(signal) == sorted(match+options[0]):
      codes[options[0]] = ['b']
      codes[options[1]] = ['d']
      break
    elif sorted(signal) == sorted(match+options[1]):
      codes[options[1]] = ['b']
      codes[options[0]] = ['d']
      break

  return codes


def decodeOutputs(codedList, codes):
  decodedList = []
  number = ''

  for coded in codedList:
    decoded = ''
    for char in coded:
      decoded += codes[char][0]
    decodedList.append(''.join(sorted(decoded)))

  number = ''

  for decoded in decodedList:
    number += str(numbersAsSegments.index(decoded))

  return int(number)


sum = 0

for entry in notes:
  entry = entry.split('|')
  signals = entry[0].strip().split(' ')
  currentCodes = decode(signals)
  outputValue = entry[1].strip().split(' ')
  sum += decodeOutputs(outputValue, currentCodes)


print("part two:", sum)
