import torch
import torch.nn as nn
import torch.optim as optim

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        return self.fc(x)

def train_model(model, data, epochs=100):
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(epochs):
        for x, y in data:
            optimizer.zero_grad()
            output = model(x)
            loss = criterion(output, y)
            loss.backward()
            optimizer.step()

def save_model(model, path="model.pth"):
    torch.save(model.state_dict(), path)

def load_model(path="model.pth"):
    model = SimpleModel()
    model.load_state_dict(torch.load(path))
    model.eval()
    return model
