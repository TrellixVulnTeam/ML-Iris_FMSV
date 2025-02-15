# Check the versions of libraries

# Python version
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load the data
url = "./iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# The shape of the dataset (number of instances (rows) and attributes (columns))
print(dataset.shape)

# The first twenty rows of data
print(dataset.head(20))

# A description of each attribute
print(dataset.describe())

# The number of instances (rows) that belong to each class
print(dataset.groupby('class').size())
