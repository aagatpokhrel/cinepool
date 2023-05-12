from core.extract import extract
from core.transform import transform
from core.load import load

def main():
    # Extract
    df = extract()
    # Transform
    df = transform(df)
    # Load
    load(df)

main()