import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing our cancer dataset
dataset = pd.read_csv(‘cancer.csv')
X = dataset.iloc[:, 1:31].values
Y = dataset.iloc[:, 31].values
dataset.head()
print("Cancer data set dimensions : {}".format(dataset.shape))
Cancer data set dimensions : (569, 32)