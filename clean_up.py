from pprint import pprint
import random

# a 10x10 grid of blocks represents the game board
game_board = range(1, 101)

def set_board(game_board):
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
  return blocks

blocks = set_board(game_board)
#pprint(blocks)


### SETTING UP THE STARTING POSITION ###
# making the bot run its path

# game agent's trajectory
agent_start = random.randint(1, 100)
#print agent_start

# how many steps to take
moves = 500

# indicating the beginning and end with a 0
# NOTE: this is a workaround that could be improved
# it's here because I am doing 'agent_path[-2]' in the
# next_move() function to avoid back-stepping of the agent
# so I need two entries in the initial list to avoid an
# index error. I'm sure there's a better way to do this!
agent_path = [0, agent_start]

def next_move(id, blocks, moves, agent_path):
  # base truth to snap out of recursion
  if moves <= 0:
    # this is the end... tam tam tam, my only friend, the end
    agent_path.append(0)
    return agent_path
  else:
    # fetch the 'neighbors' array from the current block
    current_neighbors = blocks[id-1][1]
    next_id = random.choice(current_neighbors)
    # prevent the agent to hop back onto the block it just came from
    while next_id == agent_path[-2]:
      next_id = random.choice(current_neighbors)
    # add the field, remove one step
    agent_path.append(next_id)
    moves -= 1
    # recursively call the function to generate more steps
    return next_move(next_id, blocks, moves, agent_path)


export = next_move(agent_start, blocks, moves, agent_path)
# remove the start and end digits
export = export[1:-1]

str_export = list()
for b in export:
  str_export.append(str(b))
print str_export