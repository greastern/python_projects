import torch
import time

size = (10000, 10000)

# CPU Test
a = torch.rand(size)
b = torch.rand(size)
start = time.time()
for _ in range(100):
    c = a @ b
print("CPU time:", time.time() - start)

# MPS Test
if torch.backends.mps.is_available():
    device = torch.device("mps")
    a = a.to(device)
    b = b.to(device)
    torch.mps.synchronize()
    start = time.time()
    for _ in range(100):
        c = a @ b
    torch.mps.synchronize()
    print("MPS time:", time.time() - start)
else:
    print("MPS not available")
