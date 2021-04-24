import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv(r'C:\Users\neili\OneDrive\Desktop\Data Analytics\Fifa20.csv',delimiter=',',sep=r', ')

sns.relplot(x='overall',y='value_eur',hue='age',palette = 'plasma',aspect=1.5,data=df)
plt.title('Overall Rating vs Value in Euros',fontsize = 20)
plt.xlabel('Overall Rating',fontsize = 10)
plt.ylabel('Value in Euros',fontsize = 10)
plt.show()