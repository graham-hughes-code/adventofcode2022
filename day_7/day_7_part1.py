
class Node:

  def __init__(self, name, size=0, parent=None):
    self.name = name
    self.size = size
    self.parent = parent
    self.children = []

  def get_size(self):
    child_size = 0
    for child in self.children:
      child_size += child.get_size()
    return_size = self.size + child_size
    print(f'name {self.name} size: {return_size},'
          f'children: {[child.name for child in self.children]}')
    return return_size

  def get_ans(self):
    total = 0
    for child in self.children:
      total += child.get_ans()

    size = self.get_size()
    if self.children and size <= 100000:
      return size + total

    return total



def solve(input_file):
  root = Node('root')
  current_node = root
  for instuction in input_file.split('$')[2:]:
    p_instuction = parse_instuction(instuction)
    print(f'name {current_node.name} children: {[child.name for child in current_node.children]}')
    print(f'p_instuction: {p_instuction} \n')
    if p_instuction['instuction'] == 'ls':
      current_node.children = [
        Node(name=f['name'], size=f['size'], parent=current_node) for f in p_instuction['returns']
      ]
    if p_instuction['instuction'] == 'cd':
      if p_instuction['args'] == '..':
        current_node = current_node.parent
      else:
        for child in current_node.children:
          if child.name == p_instuction['args']:
            current_node = child
            break

  return root.get_ans()



def parse_instuction(instuction):
  print(instuction)
  if 'cd ' in instuction:
    return {'instuction': 'cd', 'args': instuction.split(" ")[2].strip()}
  if 'ls' in instuction:
    return {'instuction': 'ls', 'returns': [
      {'name': x.split(' ')[1], 'size': int(x.split(' ')[0]) if x.split(' ')[0] != 'dir' else 0} for x in instuction.split('\n')[1:-1]]}

if __name__ == '__main__':

  with open('input.txt') as input_file:
    ans = solve(input_file.read())

  print(f'ans: {ans}')