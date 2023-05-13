from core.extract import extract
from core.transform import transform
from core.load import load

def main():
    # Extract the information
    df = extract()
    # Transform
    df = transform(df)
    # Load
    load(df)

main()