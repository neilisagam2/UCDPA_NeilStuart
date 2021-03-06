import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\neili\OneDrive\Desktop\Data Analytics\Fifa20.csv',delimiter=',',sep=r', ')

df['nationality'].value_counts().head(5)

nations = ['England', 'Argentina', 'Germany' ,'Spain', 'France']

df_nations = df.loc[df['nationality'].isin(nations) & df['age']]

plt.rcParams['figure.figsize'] = (20, 10)
ax = sns.boxenplot(x = 'nationality', y = 'age', data = df_nations, palette = 'plasma')
ax.set_ylabel(ylabel = 'Distribution', fontsize = 15)
ax.set_xlabel(xlabel = 'Countries', fontsize = 15)
ax.set_title(label = 'Distribution of Ages in Countries Producing Most Players', fontsize = 20)
plt.xticks(rotation = 45)
plt.show()
