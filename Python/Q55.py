import matplotlib.pyplot as plt
categories={'Food':3000,'Travel':2000}
plt.pie(categories.values(),labels=categories.keys())
plt.show()
