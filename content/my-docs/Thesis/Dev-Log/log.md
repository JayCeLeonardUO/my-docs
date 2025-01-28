# Github
- [here](https://github.com/JayCeLeonardUO/bpygfn) - `https://github.com/JayCeLeonardUO/bpygfn`
# Nov 10
Progess
---
- found a promising library to use for the GFlowNet implementation
- looked more into CLI blender
- refined an idea for a "toy" example 
- progress on dev environment set up
- Documentation set up

Next
---
Goals:
- explore how long it takes to run the examples in the GflowNet Library
- get a Ubuntu workstation set up
- Test out blender python scripting in background mode
- refine my idea for a loss based on filling a volume

Extras:
- Read all the way through GflowNet Foundation paper
- Really search for a paper that tackles a problem with a similar state space to Blender

resource links : 
---
- [GFlowNet Library](https://github.com/alexhernandezgarcia/gflownet)
- [Using Blender From The Command Line](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html)
- [Blender 4.2 - Command Line Arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)

---
# Dec 13

Progress
---
- set up portable `pip -e install .` project
- I now dont have to open blender at all and just use `bpy` directly in the notebook
- pytest
- *mock* paper

Next
---
- working on intial demo still. figuring out how to make a flow model that work's with my embeddings for a gflownet seq
- start of term have working demo.

---
# Jan 12

- found library for gflow nets to replace the other one I was useing
    -  https://github.com/GFNOrg/torchgfn
```
pip install torchgfn
```
- Was able to get several scripts for measure and constucting meshes in blender (without the need of blender)
- Nicely got all the packages Im using set up with poetry

# Jan 27
- in progress code here
    - [here](https://github.com/JayCeLeonardUO/bpygfn/blob/main/bpygfn/base.py) `https://github.com/JayCeLeonardUO/bpygfn/blob/main/bpygfn/base.py`
- Still working on getting the my blender state working with `torchgfn.env` class. 
- I After another lit review I found that this is the most relevent paper in the space
    - `https://arxiv.org/pdf/2410.15184` - ACTION ABSTRACTIONS FOR AMORTIZED SAMPLING

## next

- Get the env fully working with the "cube sampler" reward fn
- discuss the findings of `https://arxiv.org/pdf/2410.15184`

---