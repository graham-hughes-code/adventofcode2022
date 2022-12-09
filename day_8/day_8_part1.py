
def solve(input_file):
  trees = [[tree for tree in row] for row in input_file.split('\n')]
  visible = 0
  for y in range(len(trees)):
    for x in range(len(trees[y])):

      # edge
      if y == 0 or y == len(trees) - 1 or x == 0 or x == len(trees[y]) -1:
        visible += 1
      # check vis in mid
      elif check_visible(y, x, trees):
        visible += 1

  return visible

def check_visible(y, x, trees):

  mid_tree_height = trees[y][x]

  up_taller, dowm_taller, right_taller, left_taller = False, False, False, False

  for up in range(y -1, -1, -1):
    if trees[up][x] >= mid_tree_height:
      up_taller = True
  
  for down in range(y + 1, len(trees)):
    if trees[down][x] >= mid_tree_height:
      dowm_taller = True

  for right in range(x + 1, len(trees[y])):
    if trees[y][right] >= mid_tree_height:
      right_taller = True

  for left in range(x - 1, -1, -1):
    if trees[y][left] >= mid_tree_height:
      left_taller = True

  print(f'{(x, y)} {mid_tree_height}')
  print(f'up_taller: {up_taller}, dowm_taller: {dowm_taller}, right_taller: {right_taller}, left_taller: {left_taller}')
  print(f'{not up_taller or not dowm_taller or not right_taller or not left_taller}')
  return not up_taller or not dowm_taller or not right_taller or not left_taller

if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')