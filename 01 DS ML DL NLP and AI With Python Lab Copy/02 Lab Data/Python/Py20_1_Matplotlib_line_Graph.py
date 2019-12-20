#import required packages
import matplotlib.pyplot as plt
#create two simple lists
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
#plot line graph
plt.plot(year, pop)
# Add title
plt.title("Year wise population")
# Add axis labels
plt.xlabel("Year")
plt.ylabel("Population")
# Definition of tick_val and tick_lab
tick_val = [1950, 1970, 1990, 2010]
tick_lab = ['1950year','1970year','1990year','2010year']
# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)
# Adapt the ticks on the Y-axis
plt.yticks([2,3,4,5,6,7],['2B', '3B','4B', '5B','6B', '7B'])
#show the graph
plt.show()