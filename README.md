# TetrisAttackAI

## Introduction

This repository experiments with different reinforcement learning algorithms to solve the game of tetris attack (SNES).
These algorithms are currently tested:

- DQN [[1]](#1)

Furthermore we apply the learners to different kinds of game modes, these include:

- Endless: A single agent environment where the goal is to accumulate points and survive as long as possible, just like in tetris.
- VS: A multi agent environment where the goal is to defeat the opponent by sending him blocks via combos. (to be developed)

Showcase of a episode:

https://user-images.githubusercontent.com/82235217/161298279-11cf789a-a025-4801-98c2-c8a51e9abc6b.mp4

## Observation Space

To simplify the observations of the agent and thus decrease training time, the image is transformed into the games most important components. To essentially play and understand the game the agent needs to observe:

- The type of block and its discrete location (or an indication that there is none at the moment)
- The position of the "cursor" i.e the white corners that the agent needs to use in order to switch blocks.

An example of the playing field (left) compressed into its logical structure (right) looks like this:

![state](https://user-images.githubusercontent.com/82235217/161408706-c167b8aa-5c36-45db-b6c5-680df2693bf6.jpeg)

where the white little point indicates the detected position of the agents cursor.


## References
<a id="1">[1]</a> 
Mnih et al. (2013). 
Playing Atari with Deep Reinforcement Learning

