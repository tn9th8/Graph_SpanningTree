import game
from graph_data import graph
from constants import *

# prompt = """
#     Spanning Tree Finding Algorithm"""
# print(prompt)

# choice_algorithm = 'z'
# while choice_algorithm not in ['b', 'd']: 
#     prompt = """
#     Choice BFS or DFS: [b/d]?  """
#     choice_algorithm = input(prompt)

# choice_mode = 'z'
# while choice_mode not in ['a', 'o']: 
#     prompt = """
#     Choice auto-mode or one-step: [a/o]?  """
#     choice_mode = input(prompt)

# choice_root = 19
# while choice_root not in range(0, 19): 
#     prompt = """
#     Choice ROOT in range 0-18: [0-18]?  """
#     choice_root = int(input(prompt))

# choice_run = 'z'
# while choice_run not in ['y', 'n']:
#     prompt = """
#     Run now: [y/n]?  """
#     choice_run = input(prompt)

# choices = [choice_algorithm, choice_mode, choice_root]

# if choice_run == 'y': game.run(choices)
# if choice_run == 'n': print("\nThe end")
choices = 0
game.run(choices)