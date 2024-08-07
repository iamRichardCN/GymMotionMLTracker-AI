import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DataTransformation import LowPassFilter, PrincipalComponentAnalysis
from TemporalAbstraction import NumericalAbstraction


# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------
df=pd.read_pickle("../../data/interim/02_outlier_removed_chauvenet.pkl")
predictor_columns=list(df.columns[:6])

#plot setting
plt.style.use("seaborn-v0_8-deep")
plt.rcParams["figure.figsize"] = (20, 5) # Set the figure size to (20, 5) inches
plt.rcParams["figure.dpi"]= 100 # Set the figure DPI (dots per inch) to 100

# --------------------------------------------------------------
# Dealing with missing values (imputation)
# --------------------------------------------------------------
for col in predictor_columns:
    df[col]=df[col].interpolate()

df.info()
# --------------------------------------------------------------
# Calculating set duration
# --------------------------------------------------------------
df[df['set']==25]['Acc_y'].plot()

duration=df[df['set']==1].index[-1]-df[df['set']==1].index[0]
duration.seconds

for s in df['set'].unique():
    Start= duration=df[df['set']==s].index[-1]
    stop= df[df['set']==s].index[0]
    duration = Start- stop
    df.loc[(df['set']==s), "duration"] = duration.seconds


df.tail()

duration_df= df.groupby(["category"])['duration'].mean()

duration_df.iloc[0]/5
duration_df.iloc[1]/10





# --------------------------------------------------------------
# Butterworth lowpass filter
#stopping to go do another project
#https://www.youtube.com/watch?v=N2Z8MEsxRpg&list=PL-Y17yukoyy0sT2hoSQxn1TdV0J7-MX4K&index=7
# --------------------------------------------------------------
df_lowpass=df.copy()
LowPass=LowPassFilter()
fs=1000/200
cutoff=1.2

df_lowpass = LowPass.low_pass_filter(df_lowpass,'Acc_y',fs,cutoff, order=5)

subset = df_lowpass[df_lowpass['set']==45]
print(subset["Label"][0])

for col in predictor_columns:
    df_lowpass=LowPass.low_pass_filter(df_lowpass,'Acc_y',fs,cutoff, order=5)
    
   


# --------------------------------------------------------------
# Principal component analysis PCA
# --------------------------------------------------------------


# --------------------------------------------------------------
# Sum of squares attributes
# --------------------------------------------------------------


# --------------------------------------------------------------
# Temporal abstraction
# --------------------------------------------------------------


# --------------------------------------------------------------
# Frequency features
# --------------------------------------------------------------


# --------------------------------------------------------------
# Dealing with overlapping windows
# --------------------------------------------------------------


# --------------------------------------------------------------
# Clustering
# --------------------------------------------------------------


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------