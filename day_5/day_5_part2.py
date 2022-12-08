import re

def solve(crates_input):
  stacks, procedures = parse_input(crates_input)
  stacks = moves(stacks, procedures)
  print(stacks)

  return ''.join([stack[len(stack) - 1] for stack in stacks])

def moves(stacks, procedures):
  for procedure in procedures:
    temp = []
    for _i in range(procedure['ammount']):
      temp.append(stacks[procedure['from']].pop())
    temp.reverse()
    stacks[procedure['to']].extend(temp)
  return stacks

def parse_input(crates_input):
  crates_input = crates_input.split("\n\n")
  procedures_input = crates_input[1].split("\n")
  crates = crates_input[0].split("\n")
  crates_len = int(re.findall(r'\d+', crates.pop())[-1])
  stacks = [[] for i in range(crates_len)]

  crates.reverse()
  for row in crates:
    for stack, x in enumerate(range(1, (crates_len * 4) - 1, 4)):
      if row[x] != ' ':
        stacks[stack].append(row[x])

  print(stacks)
  procedures = []
  for procedure in procedures_input:
    numbers = re.findall(r'\d+', procedure)
    procedures.append({'ammount': int(numbers[0]),
                       'from': int(numbers[1]) -1,
                       'to': int(numbers[2]) - 1})
  print(procedures)

  return (stacks, procedures)

if __name__ == '__main__':

  with open('input.txt') as crates_input:
    ans = solve(crates_input.read())

  print(f'ans: {ans}')