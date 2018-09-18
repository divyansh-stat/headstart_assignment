import json
import os
import csv
import numpy as np

json_file = open("/Users/div/Documents/GitHub/headstart_assignment/cleaned_issues_list.json")
json_data = json.load(json_file)
 
total_count = []
plus_1 = []
minus_1 = []
confused = []
heart = []
hooray = []
laugh = []
title = []
comments = []

for i in xrange(1,len(json_data)):
	total_count.append(json_data[i]['reactions']['total_count'])
	plus_1.append(json_data[i]['reactions']['+1'])
	minus_1.append(json_data[i]['reactions']['-1'])
	confused.append(json_data[i]['reactions']['confused'])
	heart.append(json_data[i]['reactions']['heart'])
	hooray.append(json_data[i]['reactions']['hooray'])
	laugh.append(json_data[i]['reactions']['laugh'])
	title.append(json_data[i]['title'])
	comments.append(json_data[i]['comments'])

data = list(zip(title,comments,total_count,plus_1,minus_1,confused,heart,hooray,laugh))

np.savetxt("/Users/div/Documents/GitHub/headstart_assignment/visualization/issues.csv", data, delimiter=",", fmt='%s')