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
    

    

# --------------------------------------------------------------
# Butterworth lowpass filter
# --------------------------------------------------------------


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