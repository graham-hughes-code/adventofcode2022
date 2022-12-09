import math

class simulation():

  DIRECTION_ADDR = {
    'U': {'x': 0, 'y': -1},
    'R': {'x': 1, 'y': 0},
    'D': {'x': 0, 'y': 1},
    'L': {'x': -1, 'y': 0},

    'UR': {'x': 1, 'y': -1},
    'DR': {'x': 1, 'y': 1},
    'DL': {'x': -1, 'y': 1},
    'UL': {'x': -1, 'y': -1}
  }

  def __init__(self):
    self.head = {'x': 11, 'y': 15}
    self.tail = [{'x': 11, 'y': 15} for _x in range(9)]
    self.past_tail_pos = {(11, 15)}

  def move_head(self, direction, amount):
    for _t in range(amount):
      self.head['x'] += simulation.DIRECTION_ADDR[direction]['x']
      self.head['y'] += simulation.DIRECTION_ADDR[direction]['y']

      self._move_tail(direction)
      # self.print_state()
      # print('')
      # input('')

  def _move_tail(self, head_dir):

    last_pos = self.head

    for num, tail in enumerate(self.tail):
      # print('\n')
      if math.dist(list(last_pos.values()), list(tail.values())) > 1.42:
        # print(f'past {last_pos} curr {tail}')
        xdiff = last_pos['x'] - tail['x']
        ydiff = last_pos['y'] - tail['y']
        print(f'{xdiff} {ydiff}')
        if xdiff == 0:
          if ydiff < 0:
            tail['x'] += simulation.DIRECTION_ADDR['U']['x']
            tail['y'] += simulation.DIRECTION_ADDR['U']['y']
          else:
            tail['x'] += simulation.DIRECTION_ADDR['D']['x']
            tail['y'] += simulation.DIRECTION_ADDR['D']['y']
        elif ydiff == 0:
          if xdiff > 0:
            tail['x'] += simulation.DIRECTION_ADDR['R']['x']
            tail['y'] += simulation.DIRECTION_ADDR['R']['y']
          else:
            tail['x'] += simulation.DIRECTION_ADDR['L']['x']
            tail['y'] += simulation.DIRECTION_ADDR['L']['y']
        else:
          print('die')
          if xdiff > 0 and ydiff < 0:
            tail['x'] += simulation.DIRECTION_ADDR['UR']['x']
            tail['y'] += simulation.DIRECTION_ADDR['UR']['y']
          elif xdiff > 0 and ydiff > 0:
            tail['x'] += simulation.DIRECTION_ADDR['DR']['x']
            tail['y'] += simulation.DIRECTION_ADDR['DR']['y']
          elif xdiff < 0 and ydiff > 0:
            tail['x'] += simulation.DIRECTION_ADDR['DL']['x']
            tail['y'] += simulation.DIRECTION_ADDR['DL']['y']
          elif xdiff < 0 and ydiff < 0:
            tail['x'] += simulation.DIRECTION_ADDR['UL']['x']
            tail['y'] += simulation.DIRECTION_ADDR['UL']['y']
      # print(f'{num + 1}: {tail}')
      last_pos = tail

    self.past_tail_pos.add((self.tail[8]['x'], self.tail[8]['y']))


  def print_state(self):
    board = [['.' for _x in range(26)] for _row in range(21)]
    board[15][11] = 's'

    temp_tail = self.tail.copy()
    temp_tail.reverse()
    for num, tail in enumerate(temp_tail):
      if (not tail['x'] > len(board[0])
          and not  tail['x'] < 0 and not tail['y'] > len(board) and not  tail['y'] < 0):
        board[tail['y']][tail['x']] = str(9 - (num))

    for y in range(len(board)):
      for x in range(len(board[0])):
        if x == self.head['x'] and y == self.head['y']:
          board[y][x] = 'H'

    for row in board:
      print(' '.join(row))


  def get_ans(self):
    return len(self.past_tail_pos)

def solve(input_file):
  instructions = []
  for ins in input_file.split('\n'):
    temp = ins.split(' ')
    instructions.append({'direction': temp[0], 'amount': int(temp[1])})
  
  sim = simulation()
  for ins in instructions:
    print(ins)
    sim.move_head(**ins)

  print('')
  print(sim.past_tail_pos)

  return sim.get_ans()

if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

print(f'ans: {ans}')