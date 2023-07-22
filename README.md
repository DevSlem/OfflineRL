# OfflineRL

A collection of notebooks to describe offline reinforcement learning algorithms and their implementations. 

> This repository is based on: Levine, Sergey, et al. "[Offline reinforcement learning: Tutorial, review, and perspectives on open problems.](https://arxiv.org/abs/2005.01643)" arXiv preprint arXiv:2005.01643 (2020). 

I'm a beginner in offline RL, so I'm not sure if the descriptions and implementations are correct. But, I'm trying to make it as accurate as possible and describe in details. If you find an error or have any suggestions, please let me know by opening an issue.

## Contents

1. [Introduction](/chap1_introduction.ipynb) - Introduction to offline RL and off-policy methods.
2. Coming soon...

### Preliminary

We assume that the reader is familiar with the basic concepts of reinforcement learning, such as the Markov decision process (MDP), the Bellman equation, and the Q-learning algorithm, and with deep reinforcement learning, such as the deep Q-network (DQN), Policy Gradient. 

Furthermore, we assume that the reader is familiar with machine learning and deep learning concepts, such as the gradient descent method, the backpropagation algorithm, and the neural network.

> Note that if you're not familiar with off-policy methods, refer to the [1. Introduction](/chap1_introduction.ipynb) notebook.

## Setup

First of all, install [Python 3.10](https://www.python.org/downloads/) or higher. Then, install dependencies:

```bash
pip install torch==2.0.1
pip install matplotlib==3.7.2
pip install gymnasium==0.29.0
pip install swig
pip install "gymnasium[all]"
pip install ipykernel
pip install ipywidgets
```

> Note that the code is executed in Linux (Ubuntu 22.04). Dependencies may be different depending on your OS.

> Note that The above dependencies may change in the future as the code is updated.