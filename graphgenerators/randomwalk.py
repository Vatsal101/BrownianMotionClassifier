from Brownianclass import Brownian
import matplotlib.pyplot as plt

b = Brownian()
for i in range(4):
    plt.plot(b.gen_random_walk(500))
plt.show() 