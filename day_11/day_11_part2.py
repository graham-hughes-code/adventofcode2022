import math

AMOUNT_OF_ROUNDS = 10000
monkeys = []

class Monkey():

  def __init__(self, input):
    lines = input.split('\n')
    self.common_divisor = 0
    self.items = [int(item) for item in lines[1].split(': ')[1].split(', ')]
    self.operation = lines[2].split('= ')[1].split(' ')
    self.test = int(lines[3].split('by ')[1])
    self.if_true = int(lines[4].split('monkey ')[1])
    self.if_false = int(lines[5].split('monkey ')[1])
    self.inspected = 0

  def turn(self):
    for _x in range(len(self.items)):
      self.inspected += 1
      curr_item = self.items.pop(0)

      a = curr_item if self.operation[0] == 'old' else int(self.operation[0])
      b = curr_item if self.operation[2] == 'old' else int(self.operation[2])

      if self.operation[1] == '+':
        curr_item = a + b
      elif self.operation[1] == '-':
        curr_item = a - b
      elif self.operation[1] == '*':
        curr_item = a * b
      else:
        print('error')

      if curr_item > self.common_divisor:
        curr_item = curr_item % self.common_divisor

      if curr_item % self.test == 0:
        monkeys[self.if_true].items.append(curr_item)
      else:
        monkeys[self.if_false].items.append(curr_item)


def solve(input_file):

  for line in input_file.split('\n\n'):
    monkeys.append(Monkey(line))

  common_divisor = math.lcm(*[monkey.test for monkey in monkeys])
  for monkey in monkeys:
    monkey.common_divisor = common_divisor

  for r in range(AMOUNT_OF_ROUNDS):

    for monkey in monkeys:
      monkey.turn()
    
    all_items = []
    for m, mkey in enumerate(monkeys):
      # print(f"Monkey {m}: {mockey.items}")
      all_items.extend(mkey.items)

    if r % 1000 == 0:
      for m, mkey in enumerate(monkeys):
        print(f"Monkey {m} inspected items {mkey.inspected} times.")


  monkey_inspected = []
  for m, mkey in enumerate(monkeys):
    print(f"Monkey {m} inspected items {mkey.inspected} times.")
    monkey_inspected.append(mkey.inspected)

  monkey_inspected.sort()
  return monkey_inspected[-1] * monkey_inspected[-2]


if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')