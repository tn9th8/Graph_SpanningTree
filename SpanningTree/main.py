import full_animation

prompt = """\n
    Spanning Tree Finding Algorithm: BFS
    Run now: [y/n]?\n"""
  
choice = input(prompt)

if choice == 'y': full_animation.run()
if choice == 'n': print("The end")

print("run again and type 1, 2, or 3 only")