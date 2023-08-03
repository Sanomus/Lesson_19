import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset("penguins")
print(penguins.head())

fig, axs = plt.subplots(ncols=3)
fig.set_size_inches(16, 5)
sns.histplot(penguins['body_mass_g'], bins=10, ax=axs[0])
sns.kdeplot(penguins['body_mass_g'], fill=True, bw_adjust=.5, cut=0, ax=axs[1])
sns.violinplot(x='species', y='body_mass_g', data=penguins)
plt.show()