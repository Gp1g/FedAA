# FedAA: A Reinforcement Learning Perspective on Adaptive Aggregation for Fair and Robust Federated Learning (AAAI 2025)
This  repository contains the code for the paper titled **FedAA: A Reinforcement Learning Perspective on Adaptive Aggregation for Fair and Robust Federated Learning**, authored by Jialuo He, Wei Chen, Xiaojin Zhang.

Link to [AAAI.](https://ojs.aaai.org/index.php/AAAI/article/view/33878)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gp1g/FedAA.git
   cd FedAA
2. Create a new environment:
    ```bash
    conda create -n FedAA python==3.8
    conda activate FedAA
3. Install the necessary dependencies:
    ```bash 
    pip install -r requirements.txt
## Usage
We provide the initial data for MNIST in ./dataset, you can run the main.py as follows:
```shell
python main.py
```
## Citation 

``` 
@inproceedings{He_Chen_Zhang_2025,
  title     = {FedAA: A Reinforcement Learning Perspective on Adaptive Aggregation for Fair and Robust Federated Learning},
  author    = {He, Jialuo and Chen, Wei and Zhang, Xiaojin},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  volume    = {39},
  number    = {16},
  pages     = {17085--17093},
  year      = {2025},
}

```