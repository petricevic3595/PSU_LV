import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('C:\\PAJTON\\mtcars.csv')

sorted_df = mtcars.sort_values(by='cyl')

grouped = sorted_df.groupby('cyl')['mpg'].mean()

x = grouped.index  
y = grouped.values  


plt.bar(x, y)
plt.title('Prosječna potrošnja po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Prosječni MPG')
plt.show()
