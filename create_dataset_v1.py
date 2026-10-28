
import pandas as pd
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

df = pd.DataFrame({
    "name": ["Amit", "Sumit", "Rahul", "Priya", "Sneha"],
    "age": [21, 20, 22, 21, 20],
    "score": [85, 90, 78, 92, 88]
})

df.to_csv(data_dir / "raw_data.csv", index=False)

print("Dataset created successfully!")