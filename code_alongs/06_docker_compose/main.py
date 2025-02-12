from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
print(pd.__version__)

data_path = Path(__file__).parent / "data"
print(data_path / "prog_book.csv")

df = pd.read_csv(data_path / "prog_book.csv")
print(df.head())

print(df.info())
df.head().to_csv(data_data / "prog_book_head.csv")



