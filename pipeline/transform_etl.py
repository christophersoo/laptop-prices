import pandas as pd

def transform(mdict):
    df = pd.DataFrame(mdict)
    patterns = {
            'gb': r'(\d+)\s*GB',
            'cpu': r'(i\d|Ryzen \d)',
            }

    df['gb'] = df['name'].str.extract(patterns['gb'])
    df['cpu'] = df['name'].str.extract(patterns['cpu'])

    print(df)

def load():
    pass
