import statistics
import random
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)

#fig = ff.create_distplot([dice_result], ["Result"], show_hist = False)
#fig.show()

std_dev = statistics.stdev(data)
#print(std_dev)

first_std_dev_start,first_std_dev_end = mean-std_dev, mean+std_dev
list_of_data_within_1_std_dev = [result for result in data if result > first_std_dev_start < first_std_dev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(data)))

second_std_dev_start,second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
list_of_data_within_2_std_dev = [result for result in data if result > second_std_dev_start < second_std_dev_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(data)))

third_std_dev_start,third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)
list_of_data_within_3_std_dev = [result for result in data if result > third_std_dev_start < third_std_dev_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(data)))


