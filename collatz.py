#  This will probably ruin my computer if run for too long

from __future__ import print_function
import statistics
import numpy as np
import pandas as pd
from scipy import stats
from collections import deque
import matplotlib.pyplot as plt


def collatz_concise(q):
        if q == 1:
            return [q]
        return [q] + collatz_concise(q / 2 if not q % 2 else q * 3 + 1)

'''Optional line for smaller ranges but I would advise against it'''
#  print(len(collatz_concise(63728127))-1)


n = 100
m = 100
result = deque(maxlen=m)
data = {}
big = 100000001
small = 2
array = list(range(small, big))
big_data = []
for i in range(small, big):
    c = len(collatz_concise(i))-1
    result.append(c)
    big_data.append(c)
    if i % n == 0:
        Max = round(max(result), 2)
        Min = round(min(result), 2)
        Mean = round(sum(result) / len(result))
        Median = round(statistics.median(result))
        Range = round(Max - Min, 2)
        Trim_Mean = round(stats.trim_mean(result, 0.1), 2)
        stat = np.array(result)
        Q1 = round(np.percentile(stat, 25), 2)
        Q3 = round(np.percentile(stat, 75), 2)
        data[i] = [Min, Q1, Median, Mean, Trim_Mean, Q3, Max]

N = 1000


def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)


p = plt.figure()
plt.plot(array, big_data, 'ro', markersize=1.0)
plt.plot(running_mean(big_data, N))
'''Uncomment these lines to create a histogram of sequence lengths.
   To do this, you must comment out the scatterplot and moving average
   calls just above this'''
#  v, bins, patches = plt.hist(big_data, 100, normed=1, facecolor='g', alpha=0.75)
#  plt.ylabel('Frequency')
#  plt.xlabel('Length of Collatz Sequence')
plt.ylabel('Length of Collatz Sequence')
plt.xlabel('Starting Number')
plt.grid = True
p.savefig("collatz_dist3.png")


Data = pd.DataFrame(data)
Data = pd.DataFrame.transpose(Data)
Data.columns = ['Min', 'Q1', 'Median', 'Mean', 'Trim_Mean', 'Q3', 'Max']


print('save csv, y/n?')
q1 = input('>>> ')
if q1 == 'y':
    with open('collatz_data5.csv', 'w') as f:
        Data.to_csv(f, sep=',')
else:
    pass


plt.show()















