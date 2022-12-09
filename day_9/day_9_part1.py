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
    self.head = {'x': 0, 'y': 4}
    self.tail = {'x':0, 'y': 4}
    self.past_tail_pos = {(0, 0)}

  def move_head(self, direction, amount):
    for _t in range(amount):
      self.head['x'] += simulation.DIRECTION_ADDR[direction]['x']
      self.head['y'] += simulation.DIRECTION_ADDR[direction]['y']

      self._move_tail(direction)
      self.print_state()
      print('')
      # input('')

  def _move_tail(self, head_dir):

    if math.dist(list(self.head.values()), list(self.tail.values())) > 1.42:
      xdiff = self.head['x'] - self.tail['x']
      ydiff = self.head['y'] - self.tail['y']
      if xdiff != 0 and ydiff != 0:

        if xdiff > 0 and ydiff < 0:
          self.tail['x'] += simulation.DIRECTION_ADDR['UR']['x']
          self.tail['y'] += simulation.DIRECTION_ADDR['UR']['y']
        elif xdiff > 0 and ydiff > 0:
          self.tail['x'] += simulation.DIRECTION_ADDR['DR']['x']
          self.tail['y'] += simulation.DIRECTION_ADDR['DR']['y']
        elif xdiff < 0 and ydiff > 0:
          self.tail['x'] += simulation.DIRECTION_ADDR['DL']['x']
          self.tail['y'] += simulation.DIRECTION_ADDR['DL']['y']
        elif xdiff < 0 and ydiff < 0:
          self.tail['x'] += simulation.DIRECTION_ADDR['UL']['x']
          self.tail['y'] += simulation.DIRECTION_ADDR['UL']['y']

      else:
        self.tail['x'] += simulation.DIRECTION_ADDR[head_dir]['x']
        self.tail['y'] += simulation.DIRECTION_ADDR[head_dir]['y']

      self.past_tail_pos.add((self.tail['x'], self.tail['y']))

  def print_state(self):
    board = [['.' for _x in range(6)] for _row in range(5)]

    for y in range(len(board)):
      row = []
      for x in range(len(board[0])):
        if x == self.head['x'] and y == self.head['y']:
          row.append('H')
        elif x == self.tail['x'] and y == self.tail['y']:
          row.append('T')
        elif x == 0 and y == 4:
          row.append('s')
        else:
          row.append('.')
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