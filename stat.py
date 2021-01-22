import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CalciumBP.csv")

treated = df.loc[df['Treatment'] == "Calcium"]
untreated = df.loc[df['Treatment'] != "Calcium"]
treatment = df['Treatment']
decrease = df['Decrease']

plt.bar("Decrease",treated.mean(),width=5)
plt.bar("Decrease",untreated.mean())
plt.show()
