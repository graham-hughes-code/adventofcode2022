
def solve(input):
  elfs = input.split('\n\n')
  x = 0
  return sum(sorted([add_string_by_line(elf) for elf in elfs], reverse=True)[0:3])


def add_string_by_line(str):
  total = 0

  for line in str.split('\n'):
    total += int(line)

  return total

if __name__ == '__main__':
  with open('input.txt') as input:
    ans = solve(input=input.read())

  print(ans)