Project Description:
---

This project aims to utilize GFlowNets (Generative Flow Networks) to sample 3D models or game assets in proportion to a defined loss function. The loss function serves as a guide, allowing GFlowNets to explore and generate compositions that adhere to certain design principles or target characteristics (e.g., similarity to a reference model, pointiness, or other aesthetic metrics). This approach could significantly accelerate the creative process by proposing a variety of model configurations, streamlining asset creation for game development, or even aiding in automated level design.

Key Goals:

- **Loss-Guided Sampling**: Use a loss function (such as one based on aesthetics or gameplay functionality) to guide the sampling of possible 3D models or game assets.
- **Automated Exploration**: Enable rapid exploration of potential model configurations, allowing game developers or designers to quickly iterate over a wide variety of possible assets.
- **Creative Assistance**: Use the GFlowNet’s ability to explore high-dimensional spaces to assist artists and designers in discovering unique model compositions that align with their creative goals.
- **Game Development Integration**: Facilitate the integration of these generated assets into game engines like Unity or Unreal for real-time testing and development.

Presentation
---
![[Thesis_Prop_Leonard.pdf.pdf]]

Initial Paper Draft
---
![[CS640_F24_paper_19 (5).pdf]]
# Github
- [here](https://github.com/JayCeLeonardUO/bpygfn) - `https://github.com/JayCeLeonardUO/bpygfn`

# Nov 10
Progess

- found a promising library to use for the GFlowNet implementation
- looked more into CLI blender
- refined an idea for a "toy" example 
- progress on dev environment set up
- Documentation set up

Next

Goals:
- explore how long it takes to run the examples in the GflowNet Library
- get a Ubuntu workstation set up
- Test out blender python scripting in background mode
- refine my idea for a loss based on filling a volume

Extras:
- Read all the way through GflowNet Foundation paper
- Really search for a paper that tackles a problem with a similar state space to Blender

resource links : 

- [GFlowNet Library](https://github.com/alexhernandezgarcia/gflownet)
- [Using Blender From The Command Line](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html)
- [Blender 4.2 - Command Line Arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)

# Logs

## Dec 13

Progress

- set up portable `pip -e install .` project
- I now dont have to open blender at all and just use `bpy` directly in the notebook
- pytest
- *mock* paper

Next

- working on intial demo still. figuring out how to make a flow model that work's with my embeddings for a gflownet seq
- start of term have working demo.


## Jan 12

- found library for gflow nets to replace the other one I was useing
    -  https://github.com/GFNOrg/torchgfn
```
pip install torchgfn
```
- Was able to get several scripts for measure and constucting meshes in blender (without the need of blender)
- Nicely got all the packages Im using set up with poetry

## Jan 27
- in progress code here
    - [here](https://github.com/JayCeLeonardUO/bpygfn/blob/main/bpygfn/base.py) `https://github.com/JayCeLeonardUO/bpygfn/blob/main/bpygfn/base.py`
- Still working on getting the my blender state working with `torchgfn.env` class. 
- I After another lit review I found that this is the most relevent paper in the space
    - `https://arxiv.org/pdf/2410.15184` - ACTION ABSTRACTIONS FOR AMORTIZED SAMPLING

### next

- Get the env fully working with the "cube sampler" reward fn
- discuss the findings of `https://arxiv.org/pdf/2410.15184`

## JAN 31
how far am I from actually training the model
- after then env is done
	- can step
	- can preprocess
	- can reward states
- try with the model	
	- try with the trajectory based stuff	
## FEB 1
- im confident with where things are and how to edit them
	- step fn that does not crash
	- putting states into the fn
	- Validated appliing acctions to my simple env is as i expected
- even tho I am not done with the env should be good to look ahead to the gflownet training
	- This IS a [[hypergrid]] of actions so I can happen soon 
## FEB  2
- this is not really a hypergrid
	- its implimentation uses one hots for the flow net
- I DONT have to implimen
	- `make_random_states_tensor`
		- "random" states in my tensor would not make any sense anyway
- I DO HAVE TO
	- impliment... preprocessor 
	- `quat vol actions` - is encoding for actions
