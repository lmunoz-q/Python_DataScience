import pandas as pd

def load(path: str) -> pd.core.frame.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error : {e}")

    return None
