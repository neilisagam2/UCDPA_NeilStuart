import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\neili\OneDrive\Desktop\Data Analytics\Fifa20.csv',delimiter=',',sep=r', ')

nations = ['England', 'Argentina', 'Germany' ,'Spain', 'France']

df_nations = df.loc[df['nationality'].isin(nations) & df['height_cm']]

df['bmi'] = df['weight_kg'] / (df['height_cm'] / 100) ** 2

nations = ['England', 'Argentina', 'Germany' ,'Spain', 'France']


df_nations = df.loc[df['nationality'].isin(nations) & df['bmi']]

plt.rcParams['figure.figsize'] = (20, 10)
ax = sns.boxenplot(x = 'nationality', y = 'bmi', data = df_nations, palette = 'rocket')
ax.set_ylabel(ylabel = 'Distribution', fontsize = 15)
ax.set_xlabel(xlabel = 'Countries', fontsize = 15)
ax.set_title(label = 'Distribution of BMI in Countries Producing Most Players', fontsize = 20)
plt.xticks(rotation = 45)
plt.show()

df.iloc[df.groupby(df['nationality'])['bmi'].idxmax()][['long_name', 'nationality', 'bmi']]