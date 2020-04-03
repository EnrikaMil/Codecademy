# CrunchieMunchies Project. Task: You work in marketing for a food company YummyCorps,
# which is developing a new kind of tasty, wholesome cereal called CrunchieMunchies.
# You want to demonstrate to consumers how healthy your cereal is in comparison to other
# leading brands, so youve dug up nutritional data on several different competitors.

# Conclusion: This little project helped me to adapt my stats skills using
# NumPy lib to a 'real life' example. Here I analyzed competitors products' data (calories)
# and compared it with our product. Used stats calculations like median, percentiles, stdev
# to find and found that Crunchie Munchies would be one of the healthiest choices due to
# low calorie amount compared with the rest of the market.

import codecademylib
import numpy as np
# Importing CSV file
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

# Average of calories
average_calories = np.mean(calorie_stats)
print(average_calories)

# Sorting
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# Median
median_calories = np.median(calorie_stats)
print(median_calories)

# Percentiles
twentiethpercentile = np.percentile(calorie_stats, 20)
print(twentiethpercentile)

# percentage of cereals that have more than 60 calories per serving
more_calories = np.mean(calorie_stats > 60)
print(more_calories)
calorie_std = np.std(calorie_stats)
print(calorie_std)

