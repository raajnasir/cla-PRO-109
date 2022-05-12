import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

#calculating mean
mean = statistics.mean(data)

#calculating median
median = statistics.median(data)

#calculating mode
mode = statistics.mode(data)

print("Mean, Median and Mode of data is {}, {} and {} respectively".format(mean, median, mode))

#calculating standard deviation
std_deviation = statistics.stdev(data)

#calucating 1,2 and 3 start and end deviation
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean + std_deviation
third_std_deviation_start, thrid_std_deviation_end = mean-(3*std_deviation), mean + std_deviation

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]

print("{} % of data for data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{} % of data for data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{} % of data for data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))
