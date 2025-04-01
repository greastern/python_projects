import time
import torch
from rich.console import Console
from rich.progress import track
from rich.table import Table

console = Console()

# 🔢 XP Calculation using GPU-compatible float32
def calculate_experience_points_gpu(level, batch_size=10_000_000):
    if not torch.backends.mps.is_available():
        raise RuntimeError("MPS (Metal Performance Shaders) is not available on this machine.")

    xp = torch.tensor(0.0, dtype=torch.float32, device="mps")
    start = 1

    total_batches = (level - 1) // batch_size + 1
    console.print(f"\n🔢 Calculating XP for Level {level:,} using GPU...\n")

    for _ in track(range(total_batches), description="🚀 Batching XP calculations..."):
        end = min(start + batch_size, level)
        indices = torch.arange(start, end, dtype=torch.float32, device="mps")
        xp += (indices * 5).sum()
        start = end

    return xp.item()

# 📊 Render summary table
def render_results_table(xp, level, duration):
    table = Table(title=f"📊 XP Calculation Summary for Level {level:,}")

    table.add_column("Level", justify="right")
    table.add_column("Total XP", justify="right")
    table.add_column("Duration (s)", justify="right")

    table.add_row(f"{level:,}", f"{int(xp):,}", f"{duration}")
    console.print(table)

# 🏁 Main
if __name__ == "__main__":
    torch_device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    console.print(f"\n🎮 Using device: {torch_device}\n")

    try:
        level = 10000000000000 # ✅ Can still go quintillion+
        start_time = time.time()
        xp = calculate_experience_points_gpu(level)
        duration = round(time.time() - start_time, 2)

        render_results_table(xp, level, duration)

    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {e}")
