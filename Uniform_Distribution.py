"Uniform Disribution-It is made for probability(p)"
'Parameters-upper bound(a),lower bound(b),size(n)'
from numpy import random
a=random.uniform(size=(1000))
print(a)

#Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(a,kind="kde")
plt.show()