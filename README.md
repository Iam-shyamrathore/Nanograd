
# NanoGrad - A Lightweight Neural Network Library

**NanoGrad** is a minimalistic yet powerful neural network library built from scratch in Python, designed for educational purposes and ease of understanding. I, NanoGrad empowers you to learn and experiment with the core principles of neural networks without the overhead of large machine learning frameworks.

With NanoGrad, you can build, train, and experiment with custom neural networks while leveraging the power of automatic differentiation and backpropagation. 

### 🚀 Features
- **Automatic Differentiation**: Supports forward and backward passes with automatic gradient computation.
- **Backpropagation**: Easy implementation of backpropagation to train networks efficiently.
- **Modular Design**: Intuitive and flexible design, comprising `Value`, `Neuron`, `Layer`, and `MLP` classes that can be customized.
- **Visualization Support**: Visualize computational graphs with **Graphviz** to better understand the flow of data and gradients.
- **No External Dependencies**: Lightweight and educational, designed for learning without external ML dependencies.
- **Minimal Codebase**: Explore the core of neural networks in just a few hundred lines of Python code.

### 🌟 Why NanoGrad?
- **Build from Scratch**: Learn the fundamental concepts behind neural networks by building them from the ground up.
- **Super Lightweight**: NanoGrad focuses on the essentials, making it a perfect starting point for beginners.
- **Comprehensive Documentation**: Clear and concise documentation to help you understand each part of the code.
- **Customizable**: Tweak and modify components such as layers, activation functions, and optimizers to experiment with different architectures.

### 📦 Installation
To get started with NanoGrad, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Iam-shyamrathore/Nanograd.git
cd nanograd
pip install -r requirements.txt
```

### 🎬 Quick Start

Start experimenting with the `example_usage.py` script to see how NanoGrad can build and train neural networks:

```bash
python examples/example_usage.py
```

This example demonstrates how to create a simple Multi-Layer Perceptron (MLP) and train it on sample data.

### 🔧 Directory Structure
- **`nanograd/`**: Core library files containing the essential neural network classes and functionality.
- **`tests/`**: Unit tests to ensure correctness of the library and validate features.
- **`data/`**: Sample datasets for testing and experimentation with training.
- **`examples/`**: Example scripts to help you get started and inspire your own projects.

### 📊 Visualize Your Network
NanoGrad includes built-in support for visualizing your neural network’s computational graph using **Graphviz**. This helps you understand the flow of computations and the connections between different layers and neurons.

### 🛠 Core Components
- **Value Class**: Represents numbers and supports automatic differentiation.
- **Neuron Class**: The basic building block of the network, which performs computations.
- **Layer Class**: Contains multiple neurons and facilitates the connection between layers.
- **MLP Class**: A complete Multi-Layer Perceptron model with layers and backpropagation.

### 🔒 License
NanoGrad is released under the **MIT License**, allowing you to freely use, modify, and distribute it for both personal and commercial purposes.

### **Contribute to NanoGrad**
We welcome contributions to improve NanoGrad! Whether it’s fixing bugs, adding new features, or improving documentation, your contributions help the community grow. Feel free to open an issue or submit a pull request.

**Fork the project on GitHub**: [NanoGrad GitHub Repository](https://github.com/yourusername/nanograd)
