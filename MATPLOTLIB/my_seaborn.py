import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 60])
y = np.sin(x)

sns.lineplot(x=x, y=y)
sns.set_theme(style="darkgrid")
plt.title('Beautiful Line Plot')
plt.show()