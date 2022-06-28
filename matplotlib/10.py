import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('10data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, ax = plt.subplots(nrows=2, ncols=1)

print(ax)

#    ax.plot(ages, py_salaries, label='Python')
#    ax.plot(ages, js_salaries, label='JavaScript')
#
#    ax.plot(ages, dev_salaries, color='#444444',
#             linestyle='--', label='All Devs')
#
#    ax.legend()
#
#    ax.set_title('Median Salary (USD) by Age')
#    ax.set_xlabel('Ages')
#    ax.set_ylabel('Median Salary (USD)')
#
#    plt.tight_layout()
#
#    plt.show()
