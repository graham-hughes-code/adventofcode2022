
def solve(rucksacks):
  items_in_both = []
  for rucksack in rucksacks.split('\n'):
    items_in_both.extend(find_diff(rucksack))

  return property(items_in_both)


def find_diff(rucksack):
  a, b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
  print(f'{a} {b}')
  items_in_both = []
  items_in_a = {letter: True for letter in a}

  for letter in b:
    if items_in_a.get(letter, False):
      items_in_both.append(letter)
  
  return list(set(items_in_both))

def property(rucksacks_propertys):
  property = 0
  for rucksacks_property in rucksacks_propertys:
    if rucksacks_property.isupper():
      property += ord(rucksacks_property) - 38
    else:
      property += ord(rucksacks_property) - 96

  return property

if __name__ == '__main__':

  with open('input.txt') as rounds:
    ans = solve(rounds.read())

  print(f'ans: {ans}')