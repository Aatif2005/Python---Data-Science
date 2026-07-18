import matplotlib.pyplot as plt
import numpy as np

'''years   = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
kohli   = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag  = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
tendulkar = [2000, 1800, 1500, 1200, 900, 600, 300, 100, 0, 0]  # ✅ defined

plt.plot(years, kohli,     color='orange', linestyle='--',  label="Virat Kohli")
plt.plot(years, sehwag,    color='green',  linestyle='-.',  label="Virender Sehwag")
plt.plot(years, tendulkar, color='blue',   linestyle='-',   label="Sachin Tendulkar")'''

'''plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.legend()
plt.show()

plt.plot(years, kohli, 'ro--', label="Kohli")  # red circles with dashed lines
plt.plot(years, sehwag, 'g^:', label="Sehwag")  # green triangles dotted
plt.legend()
plt.show()'''

'''with plt.xkcd():
    plt.plot(years, kohli, label="Kohli")
    plt.plot(years, sehwag, label="Sehwag")
    plt.title("Epic Battle of the Batsmen")
    plt.legend()
    plt.show()'''

for i in range(50):
    plt.plot(np.random.rand(100), linewidth=1)

plt.title("Too Much Data Can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()