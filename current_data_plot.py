import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("current_data.csv")

plt.plot(df["time_ms"]/1000, df["current_mA"])
plt.xlabel("Time (s)")
plt.ylabel("Current (mA)")
plt.title("Current change when button is pressed")
plt.grid(True)