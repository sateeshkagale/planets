import glob
import numpy
import matplotlib.pyplot

filenames=glob.glob('data/inflammation*.csv')
filenames = filenames[0:3]
for f in filenames:
    print(f)
    data = numpy.loadtxt(fname=f, delimiter=',')
    print(data.shape)

if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
    print('Suspicious looking maxima!')
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
   axes1 = fig.add_subplot(1, 3, 1)
   axes2 = fig.add_subplot(1, 3, 2)
   axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()
