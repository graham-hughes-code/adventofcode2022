opponent_to_move = {
  'A': 'Rock',
  'B': 'Paper',
  'C': 'Scissors'
}

loss = {
  'Rock': 'Scissors',
  'Paper': 'Rock',
  'Scissors': 'Paper'
}

win = {
  'Rock': 'Paper',
  'Paper': 'Scissors',
  'Scissors': 'Rock'
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

def solve(rounds):
  opponent_score, player_score = 0, 0
  for round in rounds.split('\n'):
    opponent_move, player_move = parce_round(round)
    opponent_score, player_score = score(opponent_move,
                                         opponent_score,
                                         player_move,
                                         player_score)
  return player_score


def score(opponent_move, opponent_score, player_move, player_score):
  print(f'opponent_move: {opponent_move} player_move: {player_move}')
  opponent_move = opponent_to_move[opponent_move]
  if player_move == 'Y':
    player_move = opponent_move
  elif player_move == 'X':
    player_move = loss[opponent_move]
  elif player_move == 'Z':
    print('z')
    player_move = win[opponent_move]

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

  print(player_score)
  return opponent_score, player_score


def parce_round(round):
  moves = round.split(' ')
  return (moves[0], moves[1])

if __name__ == '__main__':
#   rounds = \
#   '''A Y
# B X
# C Z'''
  # ans = solve(rounds=rounds)

  with open('input.txt') as rounds:
    ans = solve(rounds.read())

  print(f'ans: {ans}')