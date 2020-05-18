# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:56:46 2020

@author: 胡天行
"""


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('all_data.csv')
print(df.head(10))

# Data is from 2000 to 2015
# Chile, Mexico, China, Germany, Mexico, USA

print(df.head())

df.rename(columns = {'Life expectancy at birth (years)': 'LEABY'}, inplace = True)
df['Country'].replace('United States of America', 'USA', inplace = True)

print(df.head())

# Bar charts to compare average
ax1 = plt.subplots()
sns.barplot(data = df, x = 'Country', y = 'GDP')

ax2 = plt.subplots()
sns.barplot(data = df, x = 'Country', y = 'LEABY')

# a Violin plot to compare life expectancy distributions
fig = plt.subplots(figsize=(15, 10)) 
sns.violinplot(data = df, x = 'Country', y = 'LEABY')

# bar plots of GDP and life expectancy over time
f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data = df, x = 'Country', y = 'GDP', hue = 'Year')
plt.xticks(rotation = 90)
plt.ylabel('GDP in Trillions of U.S. Dollars')

f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data = df, x = 'Country', y = 'LEABY', hue = 'Year')
plt.xticks(rotation = 90)
plt.ylabel('Life Expectancy at birth in Years')
# f.savefig('123.jpg')


# scatterplots of GDP and Life expectancy data

# WORDBANK --- all column names

# "Year"
# "Country" 1
# "GDP" 1
# "LEABY" 1
# plt.scatter 1


# Uncomment the code below and fill in the blanks
g = sns.FacetGrid(df, col='Year', hue='Country', col_wrap=4, height=2)
g = (g.map(plt.scatter, 'GDP', 'LEABY', edgecolor="w").add_legend())

# Line plots for life expectancy --- isolate the change for GDP and life expectancy over time

# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())

# line plots for GDP

g4 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4, palette = 'muted')
g4 = (g4.map(plt.plot, "Year", "GDP").add_legend())
plt.show()