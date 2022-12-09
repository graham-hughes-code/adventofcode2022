
def solve(input_file):
  trees = [[tree for tree in row] for row in input_file.split('\n')]
  top_scenic = 0
  for y in range(len(trees)):
    for x in range(len(trees[y])):

      # edge
      if y == 0 or y == len(trees) - 1 or x == 0 or x == len(trees[y]) -1:
        continue
      top_scenic = max(top_scenic, find_scenic(y, x, trees))

  return top_scenic

def find_scenic(y, x, trees):

  mid_tree_height = trees[y][x]
  scenic_score_up, scenic_score_down, scenic_score_right, scenic_score_left = 0, 0, 0, 0

  for up in range(y -1, -1, -1):
    scenic_score_up += 1
    if trees[up][x] >= mid_tree_height:
      break

  for down in range(y + 1, len(trees)):
    scenic_score_down += 1
    if trees[down][x] >= mid_tree_height:
      break

  for right in range(x + 1, len(trees[y])):
    scenic_score_right += 1
    if trees[y][right] >= mid_tree_height:
      break

  for left in range(x - 1, -1, -1):
    scenic_score_left += 1
    if trees[y][left] >= mid_tree_height:
      break

  return scenic_score_up * scenic_score_down * scenic_score_right * scenic_score_left

if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')