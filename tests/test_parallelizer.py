import pandas as pd
from loopalle import connate

def test_process_row():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    def process_row(row):
        return {"A": row["A"] * 2, "B": row["B"] + 1}

    result = connate(process_row, df)
    assert isinstance(result, pd.DataFrame)
    assert result.iloc[0]["A"] == 2
    assert result.iloc[0]["B"] == 5
