import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/erfan/Downloads/archive(2)/comptagesvelo2015.csv')
df.tail(40)

print(df.columns)