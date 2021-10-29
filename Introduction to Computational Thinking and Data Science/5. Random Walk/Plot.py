import pylab as pl

x = [1,2,3,4]
y1 = [1,2,3,4]
y2 = [1,7,3,5]

pl.plot(x, y1, 'b-', label = 'first')
pl.plot(x, y2, 'r--', label = 'second')
pl.legend()