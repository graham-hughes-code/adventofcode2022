
def solve(all_pairs):
  total = 0
  for pair in all_pairs.split('\n'):
    print(pair)
    first, second = parse_to_hash(pair)
    if check_full_overlap(first, second):
      print('overlap')
      total += 1
  return total

def check_full_overlap(first, second):

  first_full = True
  second_full = True

  for num in first:
    if num not in second:
      first_full = False
  
  for num in second:
    if num not in first:
      second_full = False

  return first_full or second_full

def parse_to_hash(pair):
  pair = pair.split(',')

  first = pair[0].split('-')
  second = pair[1].split('-')

  first = [i for i in range(int(first[0]), int(first[1]) + 1)]
  second = [i for i in range(int(second[0]), int(second[1]) + 1)]
  return (first, second)

if __name__ == '__main__':

  with open('input.txt') as all_pairs:
    ans = solve(all_pairs.read())

  print(f'ans: {ans}')