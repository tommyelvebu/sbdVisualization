import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import seaborn as sns

sbd_df = pd.read_excel("sbd1.xlsx") #file containing workout progress

sbd_df.isna().sum() # checks if there are any missing values 

sns.set(style="whitegrid")

squat_df = sbd_df[sbd_df['Exercise'] == 'Squat'].set_index("Week")
bench_df = sbd_df[sbd_df['Exercise'] == 'Bench'].set_index("Week") #creates 3 new datafiles each containing their own lift (s,b,d)
deadlift_df = sbd_df[sbd_df['Exercise'] == 'Deadlift'].set_index("Week")

fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (12,4)) #creates 3 subplots

ax[0].set_ylim(175, 265) #Squat
ax[1].set_ylim(135, 225) #Bench  - settings the y axis range 
ax[2].set_ylim(195, 290) #Deadlift

squat_df.plot(kind = "line", ax = ax[0]).set_title("Squat", fontsize = 14)
bench_df.plot(kind = "line", ax = ax[1]).set_title("Bench", fontsize = 14)
deadlift_df.plot(kind = "line", ax = ax[2]).set_title("Deadlift", fontsize = 14)

plt.show()





#sbd_df.plot()
#plt.show()