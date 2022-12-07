from collections import OrderedDict

def solve(ds):
  print(ds)
  for x in range(4, len(ds) - 1):
    print(f'x: {x}')
    print(ds[x - 4: x])
    f = ds[x - 4: x]
    s = ''.join(OrderedDict.fromkeys([c for c in ds[x - 4: x]]))
    print(f'f: {f} s: {s}')
    if f == s:
      return x

if __name__ == '__main__':

  with open('input.txt') as ds:
    ans = solve(ds.read())

  print(f'ans: {ans}')