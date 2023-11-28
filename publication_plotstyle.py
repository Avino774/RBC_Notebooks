
import matplotlib.pyplot as plt

''' set plt for latex '''
plt.rc('text',usetex=True)
plt.rc('font',family='serif')
plt.rc('font',weight='bold')
plt.rc('font',size=20)
plt.rc('legend', fontsize = 18)
plt.rc('xtick',labelsize=18)
plt.rc('ytick',labelsize=18)
plt.rc('savefig', dpi=600)
plt.rc('figure',figsize=[6,6])
plt.rc('axes',labelsize = 18)
plt.rc('axes',titlesize = 18)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


'''
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
plt.rcParams.update(params)
'''

#matplotlib.style.use('default') for back to regular
