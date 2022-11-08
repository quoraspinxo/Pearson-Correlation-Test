import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import matplotlib.patheffects as path_effects

# Read Data
database = pd.read_excel(r'C:\Users\Ratih Pratama\Documents\Cost Recovery Project\Data_Cost Recovery_Revised.xlsx', sheet_name='Cost_Recovery')
database2 = pd.read_excel(r'C:\Users\Ratih Pratama\Documents\Cost Recovery Project\Data_Cost Recovery_Revised.xlsx', sheet_name='Oil_Price')

# Data Calculation
costrec = database['Unrecovered Other Costs'] + database['Current Year Operating Costs'] + database['Depreciation - Prior Year Assets'] + database ['Depreciation - Current Year Assets']  
database['Total Cost Recovery'] = costrec

# Calculate Pearson Test
pearson = pearsonr(database2['Lifting Oil'],costrec)
# pearson = pearsonr(database2['Lifting Oil'],costrec)
pearson = pearson[0]
pea = np.round(pearson,4)
pear = str(pea)
print('Pearsons correlation: ' , pear)

# Plotting using Scatter Chart
b = database2['Lifting Oil']
plt.figure(figsize=(20, 10))
plt.scatter(x = b, y = costrec, color = 'blue')
z = np.polyfit(b, costrec, 1)
p = np.poly1d(z)
plt.plot(b, p(b))
plt.show()

# Value Card
fig, ax= plt.subplots(figsize=(3, 1.5))
text = fig.text(0.5, 0.5, pear,
                ha='center', va='center', size=20)
text.set_path_effects([path_effects.Normal()])
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
fig.show()
