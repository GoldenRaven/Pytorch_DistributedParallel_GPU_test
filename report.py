import pandas as pd
import matplotlib.pyplot as plt

# from matplotlib import rc
# rc('font',**{'family':'serif','serif':['Times']})
# rc('text', usetex=True)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
time_consume = [223, 111, 97, 55, 49, 30]
xlabels = ['nodes=1,\n per_gpu=1',
           'nodes=1,\n per_gpu=2',
           'nodes=2,\n per_gpu=1',
           'nodes=1,\n per_gpu=4',
           'nodes=2,\n per_gpu=2',
           'nodes=2,\n per_gpu=4']
plt.grid(axis='y', linestyle='--')
plt.bar(xlabels, time_consume, color='g', width=0.7)
plt.ylabel('seconds') #, fontsize=17)
plt.title('Time consumption of same Epochs(30) of same model on MNIST')
ax.text(2.8, 180, 'GPU: GeForce GTX 1080 Ti')
# plt.tight_layout()
plt.savefig('report.pdf')
