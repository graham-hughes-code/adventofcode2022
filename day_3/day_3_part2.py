
def solve(rucksacks):
  badges = []
  rucksacks = rucksacks.split('\n')

  groups = []
  for start in range(0, len(rucksacks), 3):
    groups.append(rucksacks[start : start + 3])

  for group in groups:
    badges.extend(find_diff(group))

  return property(badges)


def find_diff(group):
  items_in_all = []
  items_in_a = {letter: True for letter in group[0]}
  items_in_b = {letter: True for letter in group[1]}

  for letter in group[2]:
    if items_in_a.get(letter, False) and items_in_b.get(letter, False):
      items_in_all.append(letter)
  
  return list(set(items_in_all))

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