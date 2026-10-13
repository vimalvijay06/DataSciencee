import pandas as pd
import os

base = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'TrustWave_Cleaned')
for f in ['accounts_clean.csv','complaints_clean.csv','transactions_clean.csv','customers_clean.csv']:
    path = os.path.join(base, f)
    df = pd.read_csv(path, nrows=2)
    total = len(pd.read_csv(path, usecols=[0]))
    print(f'--- {f} ({total} rows) ---')
    print(list(df.columns))
    print()
