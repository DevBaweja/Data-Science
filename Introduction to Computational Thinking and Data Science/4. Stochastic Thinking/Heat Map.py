

import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

# data = np.random.randint(low=1,high=100,size=(10,10))
# print(data)
# sn.heatmap(data=data)


# data = pd.read_csv('BirthData.csv')

# sn.heatmap(data=data)
# print(data)

fileData = pd.read_csv('BirthData.csv')

groupData = fileData.groupby('year')
yearData = groupData.groups.keys()

days = 31
months = 12
def getStats(data):
    info = np.zeros((days, months))
    for el in data:
      year, month, day, week, birth = el
      info[day-1][month-1] = birth
    return info

columns = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

for year in yearData:
  data = groupData.get_group(year)
  data = data.to_numpy()
  info = getStats(data)
  info = np.flip(info, 0)
  heatmap = pd.DataFrame(info, columns=columns).set_axis(range(days,0, -1), axis='index')
  sn.heatmap(data=heatmap, linewidths=1, cmap='Blues')
  plt.show()

     
