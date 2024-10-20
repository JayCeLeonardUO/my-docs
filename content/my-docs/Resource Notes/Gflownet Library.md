GflowNet Library
---
This Library [here](https://github.com/alexhernandezgarcia/gflownet) Will most likely save me from implementing everything from scratch

![[tetris_flows.png]] 

GflowNet Library Tetris Environment
---
**Note:**

- the Library seems  to define experiments as some custom "GFlowNetEnv" 


>Tetris environment: an environment inspired by the game of tetris. It's not supposed to be a game, but rather a toy environment with an intuitive state and action space.
``` python
# ...
from gflownet.envs.base import GFlowNetEnv
class Tetris(GFlowNetEnv):
	"""Tetris environment: an environment inspired by the game of tetris. It's not
    supposed to be a game, but rather a toy environment with an intuitive state and
    action space.
	...
	Attributes
    ----------
    width : int
        Width of the board.

    height : int
        Height of the board.

    pieces : list
        Pieces to use, identified by [I, J, L, O, S, T, Z]

    rotations : list
        Valid rotations, from [0, 90, 180, 270]
    """
	
```
action space Tetris example
---
```python
actions = []
pieces_mat = []
for piece in self.pieces:
	for rotation in self.rotations:
				piece_mat = torch.rot90(self.piece2mat(piece),
				k=self.rot2idx[rotation])
		if self.allow_redundant_rotations or not any(
			[torch.equal(p, piece_mat) for p in pieces_mat]
		):
			pieces_mat.append(piece_mat)
		else:
			continue
		for col in range(self.width):
			if col + piece_mat.shape[1] <= self.width:
				actions.append((self.piece2idx(piece), rotation, col))
actions.append(self.eos)
return actions
```

this means that the [action space] for this Tetris examples is

```
num cols* num peices * num rotations*
```

for for every rotation and horizontal position there is an action. And the [trajectories] that the GflowNet would sample in the end would be a trajectory that would choose one of the actions every "step"

from the graph below the [action] would be ...
![[{FDF5264A-4FF9-4DA6-8D58-1E9DC299BFDC}.png]]

state space in Tetris Environment
---
 the state in the Tetris example is the result of all the actions taken in the current [trajectory]. The [State space] is what might get really big. The attributes that set the bounds are the hight and width of the grid
 
**Note:**
- I do not know if this examples tries to generate "longer" trajectories. But I do know that In the Use case for blender nodes, a "max Len" or a "max # of instances" may be a good attribute to add to the environment