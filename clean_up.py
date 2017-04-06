from pprint import pprint
import random

# a 10x10 grid of blocks represents the game board
game_board = range(1, 101)

# setting up the start situation on the game board
# defining each block's neighbors
# and setting them as 'False' (= not-selected)
blocks = list()
for id in game_board:
  if id <= 10:
    if id == 1:
      neighbors = [id+1, id+10]
    elif id == 10:
      neighbors = [id-1, id+10]
    else:
      neighbors = [id+1, id-1, id+10]
    blocks.append((id, neighbors, False))

  elif id >= 91:
    if id == 91:
      neighbors = [id+1, id-10]
    elif id == 100:
      neighbors = [id-1, id-10]
    else:
      neighbors = [id+1, id-1, id-10]
    blocks.append((id, neighbors, False))

  else:
    # finding the first ones of each 10s
    if (id-1) % 10 == 0:
      neighbors = [id+1, id+10, id-10]
    elif id % 10 == 0:
      neighbors = [id-1, id+10, id-10]
    else:
      neighbors = [id+1, id-1, id+10, id-10]
    blocks.append((id, neighbors, False))

#pprint(blocks)

# game agent's trajectory
agent_start = random.randint(1, 100)
print agent_start

def next_move(id, blocks):
  # fetch the 'neighbors' array from the current block
  current_neighbors = blocks[id-1][1]
  next_id = random.choice(current_neighbors)
  print next_id

next_move(agent_start, blocks)