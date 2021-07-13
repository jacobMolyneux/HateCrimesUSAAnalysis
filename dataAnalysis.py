# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('./hate-crimes/hate_crimes.csv')
df = pd.DataFrame(data)

stateList = df['state']


# plt.plot(df['state'], df['hate_crimes_per_100k_sp'])
DataArray = {
    'fbiHateCrimesPer100k': df['avg_hatecrimes_per_100k_fbi'],
    'medHouseInc': df['median_household_income'],
    'pctSeasonalUnemployed': df['share_unemployed_seasonal'],
    'pctMetroPop': df['share_population_in_metro_areas'],
    'pctHighSchoolGrads': df['share_population_with_high_school_degree'],
    'pctNonCitizen': df['share_non_citizen'],
    'pctWhitePoverty': df['share_white_poverty'],
    'giniIndex': df['gini_index'],
    'pctNonWhite': df['share_non_white'],
    'pctTrumpVoters': df['share_voters_voted_trump'],
    'splcHateCrime100k': df['hate_crimes_per_100k_splc'],
}
i = 1
for x, y in DataArray.items():

    plt.scatter(y, df['avg_hatecrimes_per_100k_fbi'])
    plt.title(x + ' vs Number of Hate crimes per 100k')
    plt.show()

# %%
