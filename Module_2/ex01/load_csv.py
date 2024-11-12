import pandas as pd


def load(path: str) -> pd.DataFrame:
    """opens the dataset at the path passed as an argument,\
display the size and returns it"""
    try:
        dataset = pd.read_csv(path)
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame()
    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset
