import torch
from torch import nn
from utils import *

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.structure = nn.Sequential(
            nn.Flatten(0),
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
            nn.Softmax(0)
        )

    def forward(self, x):
        logits = self.structure(x)
        return logits
    
trained_model = NeuralNetwork()
parameters = torch.load('model\model.params')
trained_model.load_state_dict(parameters)
print(trained_model.eval())

def predict_digit(x):
    img = list()
    for i in range(len(x)):
        img.append([])
        for j in range(len(x[i])):
            sum = 0
            for k in range(3): sum += x[i][j][k]

            if draw_color == BLACK:
                img[i].append(1 - sum / (255 * 3))
            else:
                img[i].append(sum / (255 * 3))
    
    prediction = trained_model(torch.Tensor([img]))
    return prediction.argmax().item()

