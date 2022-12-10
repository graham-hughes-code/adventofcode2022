
color = "\033[93m"
normal_color = "\033[00m"

dark = '██'
white = '░░'

def solve(input_file):
  instructions = input_file.split('\n')
  x = 1
  cycles = 0
  cycles_per_instruction = 0
  for instruction in instructions:
    cycles_per_instruction = 1 if instruction == 'noop' else 2

    for instruction_cycle in range(cycles_per_instruction):
      cycles_row = cycles if x > 40 else cycles - (40 * (cycles // 40))
      if cycles_row in [x - 1, x, x + 1]:
        print(f'{color}{dark}{normal_color}', end='')
      else:
        print(f'{white}', end='')
      if cycles_row == 39:
        print('')
      cycles += 1

    if instruction != 'noop':
      x += int(instruction.split(' ')[1])

  return

if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')