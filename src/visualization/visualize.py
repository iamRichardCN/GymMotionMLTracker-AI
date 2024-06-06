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
category_df=df.query("Label =='squat'").query("participant== 'A'").reset_index(drop=True)

fig, ax=plt.subplots()
category_df.groupby("category")["Gyr_y"].plot()
ax.set_ylabel("Gyr_y")
ax.set_xlabel("samples")
plt.legend()

# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------
participant_df=df.query("Label =='bench'").sort_values("participant").reset_index(drop=True)

fig, ax=plt.subplots()
participant_df.groupby("participant")["Gyr_y"].plot()
ax.set_ylabel("Gyr_y")
ax.set_xlabel("samples")
plt.legend()

# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------

# Define the label
label = "squat"
# Define the participant
participant = "A"
# Query the DataFrame for rows where the label is 'squat' and the participant is 'A'
All_axis_df = df.query(f"Label == '{label}'").query(f"participant == '{participant}'").reset_index(drop=True)


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------


# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------


# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------
