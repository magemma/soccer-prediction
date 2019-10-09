import pandas as pd

def apply_time_limits(df, start=0, end=100):
    res = df.query('time > {}'.format(str(start)))
    res = res.query('time < {}'.format(str(end)))
    return res