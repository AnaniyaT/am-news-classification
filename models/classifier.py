import torch
import torch.nn as nn

from sklearn.feature_extraction.text import TfidfVectorizer
from torch.utils.data import TensorDataset, DataLoader

class Lambda(nn.Module):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def forward(self, x):
        return self.func(x)


def resize(x):
    return x.view(x.size(0), -1)


class AmNewsClassifier(nn.Module):
    def __init__(self, input_size: int, hidden_sizes: list[int], output_size: int):
        super().__init__()
        self.net = nn.Sequential(
            Lambda(resize),
            nn.Linear(input_size, hidden_sizes[0]),
            nn.ReLU(),
            *[
                nn.Sequential(
                    nn.Linear(hidden_sizes[i], hidden_sizes[i + 1]), nn.ReLU()
                )
                for i in range(len(hidden_sizes) - 1)
            ],
            nn.Linear(hidden_sizes[-1], output_size),
        )
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, x):
        return self.net(x)

    def predict(self, x):
        with torch.no_grad():
            return torch.argmax(self.forward(x), dim=1)

    def fit(
        self,
        train_loader: DataLoader,
        val_loader: DataLoader,
        epochs: int,
        lr: float,
        verbose: bool = False,
    ) -> tuple[list[float], list[float]]:
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        train_loss_history = []
        val_loss_history = []
        for epoch in range(epochs):
            self.train()
            tot_loss = 0
            for X, y in train_loader:
                loss = self.loss_fn(self.forward(X), y)
                tot_loss += loss.item()
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()

            self.eval()
            tot_loss /= len(train_loader)
            with torch.no_grad():
                val_loss = sum(
                    self.loss_fn(self.forward(X), y) for X, y in val_loader
                ) / len(val_loader)
                if verbose:
                    print(f"Epoch {epoch + 1} Train Loss: {tot_loss}, Val Loss: {val_loss}")
                    
            train_loss_history.append(tot_loss)
            val_loss_history.append(val_loss)

        return train_loss_history, val_loss_history
    
    def evaluate(self, X, y) -> float:
        self.eval()
        with torch.no_grad():
            y_pred = self.predict(X)
            accuracy = (y_pred == y).float().mean().item()
        return accuracy


class SavedModel:
    def __init__(self, model: AmNewsClassifier, mapping: dict[int, str]):
        self.model = model
        self.mapping = mapping

    def predict(self, text: str, vectorizer: TfidfVectorizer) -> str:
        vector = torch.Tensor([vectorizer.transform([text]).toarray()])
        res = self.model.predict(vector)
        return self.mapping[res[0].item()]

        
def load_dataset(X: any, y: any, batch_size: int = 32, shuffle: bool = True) -> DataLoader:
    X, y = torch.tensor(X).float(), torch.tensor(y).long()
    dataset = TensorDataset(X, y)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

