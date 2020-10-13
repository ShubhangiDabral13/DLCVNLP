"""
Ques:
Charts to plot:
1. Create a pie chart presenting the male/female proportion
2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
"""

#PLOT -1
#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'

data = pd.read_csv(url)
sizes = [data.sex.value_counts()]
labels = ["Male","Female"]

explode = (0, 0)
colors = ['yellowgreen', 'lightcoral']
fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels,colors = colors, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('equal')

plt.show()


############
#PLOT-2

sns.scatterplot(data=data, x="fare", y="age", hue="sex", style="sex")
