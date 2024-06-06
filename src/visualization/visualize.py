import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import display
# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------
df=pd.read_pickle("../../data/interim/01_data_processed.pkl")


# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------
set_df= df[df["set"]==1]
plt.plot(set_df["Acc_y"].reset_index(drop=True))

# --------------------------------------------------------------
# Plot all exercises
# --------------------------------------------------------------
for Label in df["Label"].unique():
    subset=df[df["Label"]==Label] #For each unique label value, it creates a subset of the DataFrame df containing only rows where the "Label" column matches the current label value
    fig, ax=plt.subplots()
    plt.plot(subset["Acc_y"].reset_index(drop=True), label=Label)
    plt.legend()
    plt.show()
    

# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------
mpl.style.use("seaborn-v0_8-deep")
mpl.rcParams["figure.figsize"] = (20, 5) # Set the figure size to (20, 5) inches
mpl.rcParams["figure.dpi"]= 100 # Set the figure DPI (dots per inch) to 100





# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------


# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------


# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------


# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------
