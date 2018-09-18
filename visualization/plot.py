import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/div/Documents/GitHub/headstart_assignment/visualization/issues.csv', names=['title','number_of_comments','total_reactions','thumbs_up','thumbs_down','confused','heart','hooray','laugh'])

sum_of_reactions = df.sum(axis=0)
sum_of_reactions = sum_of_reactions.iloc[3:]

plt.plot(sum_of_reactions)
plt.ylabel('Count of reactions')
plt.xlabel('Different types of reactions')
plt.title('Frequency of different emoji reactions')
plt.show()
plt.savefig('plot_1_freq_emoji')


comments_by_reactions = df.groupby(['number_of_comments'])['total_reactions'].agg('sum')
plt.plot(comments_by_reactions)
plt.ylabel('Count of reactions')
plt.xlabel('Number of comments')
plt.title('Frequency of reactions for different number of comments')
plt.show()
plt.savefig('plot_2_freq_emoji_by_comments')