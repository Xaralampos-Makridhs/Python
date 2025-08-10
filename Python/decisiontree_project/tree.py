# Import necessary libraries
import pandas as pd  
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn import tree

# Load the dataset from a CSV file
stud_data = pd.read_csv('Diabetes_Dataset.csv')

# Separate the features (X) and the target variable (y)
X = stud_data.drop(columns=['Gender'])  # features: drop the 'Gender' column (predictor variables)
y = stud_data['Gender']  # target: 'Gender' column (what we are predicting)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 20% of the data will be used for testing

# Initialize the Decision Tree model
model = DecisionTreeClassifier()

# Train the model with the training data
model.fit(X_train, y_train)

# Use the trained model to make predictions on the test set
predictions = model.predict(X_test)

# Calculate the accuracy of the model based on the predictions
score = accuracy_score(y_test, predictions)

# Print the accuracy score
print(score)  # prints the accuracy of the model. It gives the percentage of correct predictions made by the model

# Export the trained decision tree model to a .dot file for visualization
tree.export_graphviz(model, out_file='diabetes.dot', 
                     feature_names=X.columns,  # names of the input features
                     class_names=[str(i) for i in y.unique()],  # possible target classes (gender categories)
                     label='all',  # include labels for all nodes
                     rounded=True,  # round the corners of the nodes
                     filled=True)  # fill the nodes with colors
