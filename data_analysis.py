# data analysis
import os
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
#%matplotlib inline


# Load data
dir_data = './data/'

train_file = os.path.join(dir_data, 'train.csv')
test_file = os.path.join(dir_data, 'test.csv')

print('Path of read in data: %s' % (train_file))
train_df = pd.read_csv(train_file)

# A quick look at data
print('\nData summary:')
print(train_df.describe())
print('\n')
print(train_df.head())

print('\nData columns:\n %s' % (train_df.columns))

print('\nData types:\n %s' % (train_df.get_dtype_counts()))
