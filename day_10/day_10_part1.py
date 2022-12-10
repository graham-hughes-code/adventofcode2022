
def solve(input_file):
  instructions = input_file.split('\n')
  x = 1
  signal_strengths = []
  cycles = 0
  cycles_per_instruction = 0
  for instruction in instructions:
    cycles_per_instruction = 1 if instruction == 'noop' else 2

    for instruction_cycle in range(cycles_per_instruction):
      cycles += 1

      if cycles == 20 or (cycles - 20) % 40 == 0:
        signal_strengths.append(cycles * x)
    
    if instruction != 'noop':
      x += int(instruction.split(' ')[1])

  return sum(signal_strengths)

if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')