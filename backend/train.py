import os
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
from model import CNN

# ================= PATH =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "final_dataset.csv")

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

# ================= DROP NON-NUMERIC COLUMNS =================
drop_cols = [
    'Unnamed: 0',
    'Flow ID',
    'Src IP',
    'Dst IP',
    'Timestamp'
]
df = df.drop(columns=[c for c in drop_cols if c in df.columns])

print("After drop:", df.shape)

# ================= SAMPLE FIRST (CRITICAL) =================
df = df.sample(n=20000, random_state=42)
print("After sampling:", df.shape)

# ================= HANDLE INF / NAN =================
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

print("After cleaning:", df.shape)

# ================= SPLIT FEATURES / LABEL =================
X = df.drop("Label", axis=1).values
y = df["Label"].values

# ================= ENCODE LABELS =================
y = pd.factorize(y)[0]

# ================= SCALE =================
scaler = StandardScaler()
X = scaler.fit_transform(X)

# ================= TORCH =================
X = torch.tensor(X, dtype=torch.float32).unsqueeze(1)
y = torch.tensor(y, dtype=torch.long)

dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

# ================= MODEL =================
model = CNN(X.shape[2])
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# ================= TRAIN =================
print("Training started...")
for epoch in range(5):
    total_loss = 0
    for xb, yb in loader:
        optimizer.zero_grad()
        outputs, _ = model(xb)
        loss = criterion(outputs, yb)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"Epoch {epoch+1} | Loss: {total_loss:.4f}")

# ================= SAVE =================
SAVE_DIR = os.path.join(BASE_DIR, "..", "saved_model")
os.makedirs(SAVE_DIR, exist_ok=True)
torch.save(model.state_dict(), os.path.join(SAVE_DIR, "cnn_model.pth"))

print("✅ Training completed successfully")
