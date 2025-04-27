import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV dataset and prints its dimensions.

    Parameters
    ----------
    path : str
        Path to the CSV file.

    Returns
    -------
    """
    if not path.endswith(".csv"):
        print("Document must be a 'CSV' file")
        return None
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
