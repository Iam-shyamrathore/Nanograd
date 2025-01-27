
# NanoGrad

NanoGrad is a lightweight neural network library implemented from scratch in Python, inspired by Andrej Karpathy's Micrograd. 
It provides core functionality for building and training neural networks without relying on external ML libraries.

## Features
- Automatic differentiation and backpropagation
- Modular design with `Value`, `Neuron`, `Layer`, and `MLP` classes
- Visualization of computational graphs using Graphviz

## Installation
Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the example script:
```bash
python examples/example_usage.py
```

## Directory Structure
- `nanograd/`: Core library files
- `tests/`: Unit tests and validation
- `data/`: Sample test data for training and evaluation
- `examples/`: Example scripts

## License
MIT License
