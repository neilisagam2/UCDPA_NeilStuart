import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

df = pd.read_csv(r'C:\Users\neili\OneDrive\Desktop\Data Analytics\Fifa20.csv',delimiter=',',sep=r', ')

nations = ['England', 'Republic of Ireland']
df = df[df['nationality'].isin(nations)]

df['dob']= pd.to_datetime(df['dob'])
df['year'] = pd.DatetimeIndex(df['dob']).year
df['month'] = pd.DatetimeIndex(df['dob']).month
df['month_name'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df['day'] = pd.DatetimeIndex(df['dob']).day
df['dayofweek'] = pd.DatetimeIndex(df['dob']).weekday

for nation in nations:
  (df[df['nationality']== nation]['month'].value_counts(normalize=True)*100).sort_index().plot(color = 'gray')
  (df[df['nationality']=='Republic of Ireland']['month'].value_counts(normalize=True)*100).sort_index().plot()
plt.text(1,15,'Irish Players vs English Players by Birth Month', fontsize=16, fontweight=300)
plt.xlabel('Month')
plt.ylabel('Players')
