from pathlib import Path
import pandas as pd
print(pd.__version__)

data_path = Path(__file__).parent / "data"
print(data_path / "prog_book.csv")
