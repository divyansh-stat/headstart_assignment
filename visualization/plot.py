import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/div/Documents/GitHub/headstart_assignment/visualization/issues.csv', names=['title','number_of_comments','total_reactions','thumbs_up','thumbs_down','confused','heart','hooray','laugh'])

sum_of_reactions = df.sum(axis=0)
sum_of_reactions = sum_of_reactions.iloc[3:]

print type(sum_of_reactions)
plt.plot(sum_of_reactions)
plt.ylabel('Count of reactions')
plt.xlabel('Different types of reactions')
plt.title('Frequency of different of emoji reactions')
plt.show()




