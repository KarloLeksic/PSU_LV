import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.datasets import load_boston

boston = load_boston()
X = boston.data
y = boston.target

print(boston.feature_names)
print(y)