import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\neili\OneDrive\Desktop\Data Analytics\Fifa20.csv',delimiter=',',sep=r', ')

plt.figure(figsize =(15,32))
sns.countplot(y = df.nationality, palette = "Set3", order = df['nationality'].value_counts().index)
plt.xlabel('Player Count')
plt.ylabel('Nationality')
plt.title('Players by Country',fontsize = 20)
plt.interactive(False)
