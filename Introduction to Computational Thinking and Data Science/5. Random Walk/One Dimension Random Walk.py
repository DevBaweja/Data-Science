import pylab
import random
trials = 100

# random.seed(0)


def singleWalk(steps, options):
    cur = 0
    for _ in range(steps):
        cur += random.choice(options)
    return cur


options = [-1, 1]
steps = [10, 100, 1000, 10000]
means = []
for step in steps:
    vals = []
    for _ in range(trials):
        cur = singleWalk(step, options)
        vals.append(cur)
    vals = [abs(el) for el in vals]
    mean = round(sum(vals)/len(vals), 2)
    means.append(mean)

print(means)
pylab.plot(steps, means)
