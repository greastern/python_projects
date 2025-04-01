import torch

# Check if MPS (Metal Performance Shaders) is available
print(f"PyTorch version: {torch.__version__}")
print(f"Is MPS (Metal) available: {torch.backends.mps.is_available()}")
print(f"Is MPS built: {torch.backends.mps.is_built()}")

# Try to create a tensor on the MPS device
if torch.backends.mps.is_available():
    device = torch.device("mps")
    x = torch.ones(5, device=device)
    print(f"Tensor created on MPS device: {x}")
    print(f"Device: {x.device}")