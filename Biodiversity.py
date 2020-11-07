import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
print(os.getcwd())
print(os.listdir())
pd.set_option('max_columns', None)

species = pd.read_csv('/home/jackie/PycharmProjects/Matplotlib/biodiversity/species_info.csv')
print(species.head())

#How many different species in the df?
species_count = species['scientific_name'].nunique()
print(species_count)

# What are the different values of category in the DataFrame species?
species_type = species.category.unique()
print(species_type)

#What are the different values of conservation_status?
conservation_statuses = species.conservation_status.unique()
print(conservation_statuses)

#count how many scientific_name falls into each conservation_status criteria
conservation_counts = species.groupby(['conservation_status'])['scientific_name'].nunique().reset_index()
print(conservation_counts)

#replace NaN in our DataFrame with 'No Intervention'
species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print(conservation_counts_fixed)

#Barchart: conservation statuses by species
protection_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index().sort_values(by='scientific_name')

plt.figure(figsize=(10,4))
ax = plt.subplot()
plt.bar(range(5), protection_counts['scientific_name'], color='blue')
ax.set_xticks(range(5))
ax.set_xticklabels(protection_counts['conservation_status'])
plt.ylabel('Number of Species')
#plt.show()

#Investigating Endangered Species
species['is_protected'] = species.conservation_status != 'No Intervention'
category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()
category_pivot.columns = ['category', 'not_protected', 'protected']

#Are certain types of species more likely to be endangered?
category_pivot['percent_protected'] = category_pivot['protected']*100 / (category_pivot['not_protected'] + category_pivot['protected'])
print(category_pivot)

#Chi square test Mammal & Bird
from scipy.stats import chi2_contingency
contingency = [[30, 146],[75, 413]]
print(chi2_contingency(contingency))

#Chi square test Mammal & Reptile
contingency1 = [[30, 146],[5, 73]]
print(chi2_contingency(contingency1))

#Observations dataframe
observations = pd.read_csv('observations.csv')
print(observations.head())

#Create a new column in species called is_sheep which is True if the common_names contains 'Sheep', and False otherwise.
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
species_is_sheep = species[species.is_sheep]

#Many of the results are actually plants. Select the rows of species where is_sheep is True and category is Mammal.
sheep_species = species[(species['is_sheep']) & (species.category == 'Mammal')]

#merge sheep_species with observations to get a DataFrame with observations of sheep
sheep_observations = pd.merge(sheep_species, observations)
print(sheep_observations.head())

#How many total sheep sightings (across all three species) were made at each national park?
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print(obs_by_park)

plt.figure(figsize=(16,4))
ax = plt.subplot()
plt.bar(range(4), obs_by_park.observations)
ax.set_xticks(range(4))
ax.set_xticklabels(obs_by_park.park_name)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()


