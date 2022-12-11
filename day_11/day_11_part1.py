AMOUNT_OF_ROUNDS = 20
monkeys = []

class Monkey():

  def __init__(self, input):
    lines = input.split('\n')
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

      curr_item = curr_item//3

      if curr_item % self.test == 0:
        monkeys[self.if_true].items.append(curr_item)
      else:
        monkeys[self.if_false].items.append(curr_item)


def solve(input_file):

  for line in input_file.split('\n\n'):
    monkeys.append(Monkey(line))

  for r in range(AMOUNT_OF_ROUNDS):

    for monkey in monkeys:
      monkey.turn()

    print('After round {r}, the monkeys are holding items with these worry levels:')
    for m, mockey in enumerate(monkeys):
      print(f"Monkey {m}: {mockey.items}")

  mockey_inspected = []
  for m, mockey in enumerate(monkeys):
    print(f"Monkey {m} inspected items {mockey.inspected} times.")
    mockey_inspected.append(mockey.inspected)

  mockey_inspected.sort()
  return mockey_inspected[-1] * mockey_inspected[-2]


if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')