import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------
single_file_Acc= pd.read_csv('../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv')
single_file_Gyr= pd.read_csv('../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv')
# --------------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------
file = glob('../../data/raw/MetaMotion/*.csv')

len(file)

# --------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------f 

# Base data path
data_path = '../../data/raw/MetaMotion\\'

f = file[0]
g = file[1]
participant= f.split('-')[0].replace(data_path, '')
Label= f.split('-')[1]
category = f.split('-')[2].rstrip('123').rstrip('_MetaWear_2019')

df= pd.read_csv(f)
df[participant]=participant
df[Label]=Label
df[category]=category
# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------
file = glob('../../data/raw/MetaMotion/*.csv')

acc_df=pd.DataFrame()
gyr_df=pd.DataFrame()

acc_set=1
gyr_set=1

# Process each file
for f in file:
    participant= f.split('-')[0].replace(data_path, '')
    Label= f.split('-')[1]
    category = f.split('-')[2].rstrip('123').rstrip('_MetaWear_2019')
    
    df = pd.read_csv(f)
    
    # Add metadata as new columns
    df["participant"] = participant
    df["Label"] = Label
    df["category"] = category
        
    if "Accelerometer" in f:
        df["set"]=acc_set
        acc_set +=1
        acc_df=pd.concat([acc_df, df])
    
    if "Gyroscope" in f:
        df["set"]=gyr_set
        gyr_set +=1
        gyr_df=pd.concat([gyr_df, df])
    
#acc_df[acc_df["set"]==1]
# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------
gyr_df.info()

pd.to_datetime(df["epoch (ms)"], unit="ms")

acc_df.index=pd.to_datetime(acc_df["epoch (ms)"], unit="ms")
gyr_df.index=pd.to_datetime(gyr_df["epoch (ms)"], unit="ms")

del acc_df["epoch (ms)"]
del acc_df["time (01:00)"]
del acc_df["elapsed (s)"]

del gyr_df["epoch (ms)"]
del gyr_df["time (01:00)"]
del gyr_df["elapsed (s)"]



# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------
file = glob('../../data/raw/MetaMotion/*.csv')
data_path = '../../data/raw/MetaMotion\\'

def read_data_from_files(file):
    acc_df=pd.DataFrame()
    gyr_df=pd.DataFrame()

    acc_set=1
    gyr_set=1

    # Process each file
    for f in file:
        participant= f.split('-')[0].replace(data_path, '')
        Label= f.split('-')[1]
        category = f.split('-')[2].rstrip('123').rstrip('_MetaWear_2019')
        
        df = pd.read_csv(f)
        
        # Add metadata as new columns
        df["participant"] = participant
        df["Label"] = Label
        df["category"] = category
            
        if "Accelerometer" in f:
            df["set"]=acc_set
            acc_set +=1
            acc_df=pd.concat([acc_df, df])
        
        if "Gyroscope" in f:
            df["set"]=gyr_set
            gyr_set +=1
            gyr_df=pd.concat([gyr_df, df])
    
    pd.to_datetime(df["epoch (ms)"], unit="ms")

    acc_df.index=pd.to_datetime(acc_df["epoch (ms)"], unit="ms")
    gyr_df.index=pd.to_datetime(gyr_df["epoch (ms)"], unit="ms")

    del acc_df["epoch (ms)"]
    del acc_df["time (01:00)"]
    del acc_df["elapsed (s)"]

    del gyr_df["epoch (ms)"]
    del gyr_df["time (01:00)"]
    del gyr_df["elapsed (s)"]
    
    return  acc_df, gyr_df

acc_df, gyr_df=read_data_from_files(file)

# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------
data_merge= pd.concat([acc_df.iloc[:,:3], gyr_df], axis=1)
#rename the columns for ease
data_merge.columns= [
    "Acc_x",
    "Acc_y",
    "Acc_z",
    "Gyr_x",
    "Gyr_y",
    "Gyr_z",
    "participant",
    "Label",
    "category",
    "set"    
]


data_merge

# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------
sampling={
   "Acc_x":"mean",
    "Acc_y":"mean",
    "Acc_z":"mean",
    "Gyr_x":"mean",
    "Gyr_y":"mean",
    "Gyr_z":"mean",
    "participant" :"last",
    "Label"       :"last",
    "category"    :"last",
    "set"         :"last"
}

data_merge[:1000].resample(rule="200ms").apply(sampling)


# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------