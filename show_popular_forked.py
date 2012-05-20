import numpy as np
import matplotlib.pyplot as plt
import csv

bqReader = csv.reader(open('top50_popular_forked_js.csv'))
raw_csv = list(bqReader)
data = raw_csv[1:]

repos = []
forks = []
for d in data:
    repos.append(d[0])
    forks.append(int(d[1]))

arepos = np.array(repos)
aforks = np.array(forks)
x = np.arange(len(repos))
width = 0.5

plt.figure(figsize=(20,10))
plt.bar(x, aforks, width)
plt.xticks(x+width/2, repos, fontsize=9)
plt.ylabel('number of forks')
plt.title('Top 50 forked repository for JavaScript')
plt.setp(plt.gca().get_xticklabels(), rotation=60)
plt.grid(True)

plt.show()


