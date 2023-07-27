import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Load the dataset from a source path
dataset_path = "C:/Users/jalaj/VsCodeLiter/PYs/Decision_tree_irisalgo/Iris.csv"
df = pd.read_csv(dataset_path)

# Separate the features and labels
X = df.iloc[:, 1:5]  # Features
y = df.iloc[:, -1]  # Labels

# Create an instance of the DecisionTreeClassifier and fit it to the data
classifier = DecisionTreeClassifier()
classifier.fit(X, y)

# Visualize the decision tree
fig, ax = plt.subplots(figsize=(12, 12))
tree.plot_tree(classifier, feature_names=X.columns.tolist(), class_names=classifier.classes_.tolist(), filled=True, ax=ax)
plt.show()

# Prompt the user for new data
new_data = []
sepal_length = float(input("Enter the Sepal Length (cm): "))
sepal_width = float(input("Enter the Sepal Width (cm): "))
petal_length = float(input("Enter the Petal Length (cm): "))
petal_width = float(input("Enter the Petal Width (cm): "))
new_data.append([sepal_length, sepal_width, petal_length, petal_width])

# Use the trained classifier to make predictions on the new data
predictions = classifier.predict(new_data)

# Print the predicted class
print("Predicted class:", predictions[0])
