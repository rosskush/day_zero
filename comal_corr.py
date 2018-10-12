import pandas as pd
import nwis_pull as nwis
from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt



siteid  =  '08169000'
station_nm = 'Comal Rv at New Braunfels, TX'
param_code = '00060'
df = nwis.pull_data.realtime(siteid,start_date='2018-07-01',end_date='2018-07-11',param_code=param_code)
df['Comal River'] = df[param_code]
del df[param_code]

siteid2 = '08168932'
station_nm2 = 'Comal Rv (nc) nr Landa Lk, New Braunfels, TX'
df2 = nwis.pull_data.realtime(siteid2,start_date='2018-07-01',end_date='2018-07-11',param_code=param_code)
df2['Comal Rv (nc)'] = df2[param_code]
del df2[param_code]

siteid3 = '08168913'
station_nm3 = 'Comal Rv (oc) nr Landa Lk, New Braunfels, TX'
df3 = nwis.pull_data.realtime(siteid3,start_date='2018-07-01',end_date='2018-07-11',param_code=param_code)
df3['Comal Rv (oc)'] = df3[param_code]
del df3[param_code]

df = df.merge(df2, left_index=True, right_index=True)
df = df.merge(df3, left_index=True, right_index=True)
print(df.head())


corr = df.corr()
print(corr)


fig, ax = plt.subplots()
scatter_matrix(df,alpha=.3)

# fig, ax = plt.subplots(figsize=(8.8,7))
# ax.plot(df.index,df[param_code])
# ax.set_ylabel('Discharge $\\frac{ft^3}{s}$',fontsize = 14)
# ax.grid()
# plt.title(station_nm)
# fig.autofmt_xdate()
# fig.tight_layout()
plt.show()



