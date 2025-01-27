
import json
from nanograd.core import Value
from nanograd.nn import MLP

def test_mlp():
    # Load test data
    with open("../data/test_data.json") as f:
        data = json.load(f)
    xs = data["inputs"]
    ys = data["outputs"]

    # Create MLP model
    model = MLP(3, [4, 4, 1])

    # Forward pass
    predictions = [model(x) for x in xs]
    losses = [(y_pred - y_true) ** 2 for y_pred, y_true in zip(predictions, ys)]

    # Compute loss
    total_loss = sum(losses, start=Value(0.0))
    print("Total loss:", total_loss.data)

if __name__ == "__main__":
    test_mlp()
