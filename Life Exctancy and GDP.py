import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


import os
print(os.getcwd())
print(os.listdir())
pd.set_option('max_columns', None)

df = pd.read_csv('/home/jackie/PycharmProjects/Matplotlib/Life Expectancy and GDP Capstone/all_data.csv')

#General info:
countries = df['Country'].unique()
years = df['Year'].unique()
no_years = df['Year'].nunique()
df.rename(columns={'Life expectancy at birth (years)':'LEABY'}, inplace=True)
print(df.head())
print(countries)
print(years)
print(no_years)

#China GDP
max_china = df[df['Country'] == 'China'].GDP.max()
min_china = df[df['Country'] == 'China'].GDP.min()
#print(max_china/min_china)

#USD GDP
max_usa = df[df['Country'] == 'United States of America'].GDP.max()
min_usa = df[df['Country'] == 'United States of America'].GDP.min()
#print(max_usa/min_usa)


#CHART_1
ax = plt.figure(figsize=(50, 40))
ax = sns.barplot(data=df, x="Country", y="GDP", hue='Year')
plt.xticks(rotation=90)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.show()

#CHART_2
ax1 = plt.figure(figsize=(50, 40))
ax1 = sns.barplot(data=df, x='Country', y='LEABY', hue='Year')
plt.xticks(rotation=90)
plt.ylabel('Life expectancy at births in years')
plt.show()

#CHART_3
plt.figure(figsize=(12, 10))
sns.set_style('darkgrid')
sns.barplot(data=df, x='Country', y='GDP')
plt.xlabel(None)
plt.ylabel('GDP in Trillions of US Dollars')
plt.show()
plt.savefig('Average GDP over the period')

#CHART_4
group_leaby = df.groupby('Country')['LEABY'].mean().reset_index()
plt.figure(figsize=(12, 10))
sns.set_style('darkgrid')
leaby_chart = sns.barplot(data=group_leaby, x='Country', y='LEABY')
for index, row in group_leaby.iterrows():
    leaby_chart.text(row.name, row.LEABY, round(row.LEABY, 2), color='black', ha="center")
plt.ylabel('Average LEABY')
plt.xlabel(None)
plt.show()
plt.savefig('Average LEABY')

#EACH COUNTRY GRAPH:
#Chile
chile = df[df['Country'] == 'Chile']
print(chile['LEABY'].median())
ax1 = plt.subplot()
plt.plot(range(16), chile['GDP'])
ax1.set_xticks(range(16))
ax1.set_xticklabels(chile['Year'], rotation=45)
#plt.show()

ax2 = plt.subplot()
plt.plot(range(16), chile['LEABY'])
ax2.set_xticks(range(16))
ax2.set_xticklabels(chile['Year'], rotation=45)
#plt.show()

#China
china = df[df['Country'] == 'China']
print(china['LEABY'].median())
ax3 = plt.subplot()
plt.plot(range(16), china['LEABY'])
ax3.set_xticks(range(16))
ax3.set_xticklabels(china['Year'], rotation=45)
plt.show()
ax4 = plt.subplot()
plt.plot(range(16), china['GDP'])
ax4.set_xticks(range(16))
ax4.set_xticklabels(china['Year'], rotation=45)
#plt.show()

#Germany
germany = df[df['Country'] == 'Germany']
print(germany['LEABY'].median())
ax5 = plt.subplot()
plt.plot(range(16), germany['GDP'])
ax5.set_xticks(range(16))
ax5.set_xticklabels(germany['Year'], rotation=45)
#plt.show()

ax6 = plt.subplot()
plt.plot(range(16), germany['LEABY'])
ax6.set_xticks(range(16))
ax6.set_xticklabels(germany['Year'], rotation=45)
#plt.show()

#USA
usa = df[df['Country'] == 'United States of America']
print(usa['LEABY'].median())
ax7 = plt.subplot()
plt.plot(range(16), usa['LEABY'])
ax7.set_xticks(range(16))
ax7.set_xticklabels(usa['Year'], rotation=45)
#plt.show()

ax8 = plt.subplot()
plt.plot(range(16), usa['GDP'])
ax8.set_xticks(range(16))
ax8.set_xticklabels(usa['Year'], rotation=45)
#plt.show()

#mexico
mexico = df[df['Country'] == 'Mexico']
print(mexico['LEABY'].median())
ax9 = plt.subplot()
plt.plot(range(16), mexico['LEABY'])
ax9.set_xticks(range(16))
ax9.set_xticklabels(mexico['Year'], rotation=45)
#plt.show()

ax10 = plt.subplot()
plt.plot(range(16), mexico['GDP'])
ax10.set_xticks(range(16))
ax10.set_xticklabels(mexico['Year'], rotation=45)
#plt.show()

#zimbabwe
zimbabwe = df[df['Country'] == 'Zimbabwe']
print(zimbabwe['LEABY'].median())
max_z= df[df['Country'] == 'Zimbabwe'].LEABY.max()
min_z = df[df['Country'] == 'Zimbabwe'].LEABY.min()
#print(max_z)
#print(min_z)
ax11 = plt.subplot()
plt.plot(range(16), zimbabwe['GDP'])
ax11.set_xticks(range(16))
ax11.set_xticklabels(zimbabwe['Year'], rotation=45)
plt.show()

ax12 = plt.subplot()
plt.plot(range(16), zimbabwe['LEABY'])
ax12.set_xticks(range(16))
ax12.set_xticklabels(zimbabwe['Year'], rotation=45)
#plt.show()

#scatter_plot
graph = sns.FacetGrid(df, col='Year',  hue='Country')
graph.map(plt.scatter, 'GDP', 'LEABY', edgecolor ="w").add_legend()
plt.show()


#CHART_5 violinplot
sns.set_style('darkgrid')
sns.set_palette('pastel')
sns.violinplot(data=df, y='Country', x='LEABY')
plt.show()