import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

mpg_data = sns.load_dataset("mpg")
pd.set_option('display.max_columns', None)
dts = mpg_data.head(12)

name = dts['name'].tolist()
horsepower = dts['horsepower'].tolist()

plt.bar(name, horsepower, color='purple',edgecolor='black')
plt.grid(alpha=0.3)
plt.title('Сomparative statistics of car capacities')
plt.xlabel('Car model')
plt.ylabel('hp')
plt.xticks(rotation=315,size=7)
plt.show()

pie = plt.pie(horsepower,labels=name, autopct='%1.1f%%')
plt.show()