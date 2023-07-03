import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

average_calories = np.mean(calorie_stats)
#print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
#print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
#print(median_calories)

#print np.percentile(calorie_stats, 25)
#print np.percentile(calorie_stats, 12)
#print np.percentile(calorie_stats, 6)
#print np.percentile(calorie_stats, 3)
print np.percentile(calorie_stats, 4)

nth_percentile = 4

more_calories = 100-nth_percentile
print(more_calories)

calorie_std = np.std(calorie_stats)
print(calorie_std)