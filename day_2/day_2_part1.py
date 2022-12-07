opponent_to_move = {
  'A': 'Rock',
  'B': 'Paper',
  'C': 'Scissors'
}

player_to_move = {
  'X': 'Rock',
  'Y': 'Paper',
  'Z': 'Scissors'
}

move_to_score = {
  'Rock': 1,
  'Paper': 2,
  'Scissors': 3
}

round_score = {
  'lost': 0,
  'draw': 3,
  'won': 6
}

def solve(input):
  opponent_score, player_score = 0, 0
  for round in input.split('\n'):
    opponent_move, player_move = parce_round(round)
    opponent_score, player_score = score(opponent_move,
                                         opponent_score,
                                         player_move,
                                         player_score)
  return player_score


def score(opponent_move, opponent_score, player_move, player_score):
  opponent_move = opponent_to_move[opponent_move]
  player_move = player_to_move[player_move]
  print(f'opponent_move: {opponent_move} player_move: {player_move}')

  # draw
  if opponent_move == player_move:
    print('draw')
    opponent_score += round_score['draw'] + move_to_score[opponent_move]
    player_score += round_score['draw'] + move_to_score[player_move]

  # player_score win
  if ((player_move == 'Rock' and opponent_move == 'Scissors') or
      (player_move == 'Paper' and opponent_move == 'Rock') or
      (player_move == 'Scissors' and opponent_move == 'Paper')):
    print('player_score win')
    opponent_score += round_score['lost'] + move_to_score[opponent_move]
    player_score += round_score['won'] + move_to_score[player_move]

  # opponent_move win
  if ((player_move == 'Scissors' and opponent_move == 'Rock') or
      (player_move == 'Rock' and opponent_move == 'Paper') or
      (player_move == 'Paper' and opponent_move == 'Scissors')):
    print('opponent_move win')
    opponent_score += round_score['won'] + move_to_score[opponent_move]
    player_score += round_score['lost'] + move_to_score[player_move]

  return opponent_score, player_score


def parce_round(round):
  moves = round.split(' ')
  return (moves[0], moves[1])

if __name__ == '__main__':
#   input = \
#   '''A Y
# B X
# C Z'''
  # ans = solve(input)

  with open('input.txt') as input:
    ans = solve(input=input.read())

  print(f'ans: {ans}')