import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

class DecisionTreeModel:
    def __init__(self, file_path):
        """
        Initialize the DecisionTreeModel.

        :param file_path: Path to the CSV file containing the data.
        """
        self.file_path = file_path
        self.tree_model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.mae = None
        self.mse = None
        self.r2 = None

    def load_and_prepare_data(self):
        """
        Load and prepare the dataset for modeling.
        Extracts the target variable (y) and independent variables (X).
        """
        data = pd.read_csv(self.file_path)
        self.y = data["Total Deaths"]
        self.X = data.drop("Total Deaths", axis=1)

    def split_data(self, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets.

        :param test_size: The proportion of the dataset to include in the test split.
        :param random_state: Controls the randomness of the data splitting.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state
        )

    def build_and_evaluate_decision_tree(
        self, max_depth=5, min_samples_split=20, min_samples_leaf=10
    ):
        """
        Build a decision tree model and evaluate its performance.

        :param max_depth: The maximum depth of the tree.
        :param min_samples_split: The minimum number of samples required to split an internal node.
        :param min_samples_leaf: The minimum number of samples required to be at a leaf node.
        """
        self.tree_model = DecisionTreeRegressor(
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features="sqrt",
            random_state=42,
        )
        self.tree_model.fit(self.X_train, self.y_train)

        y_pred = self.tree_model.predict(self.X_test)

        self.mae = mean_absolute_error(self.y_test, y_pred)
        self.mse = mean_squared_error(self.y_test, y_pred)
        self.r2 = r2_score(self.y_test, y_pred)

    def visualize_decision_tree(self):
        """
        Visualize the decision tree model.
        """
        plt.figure(figsize=(20, 10))
        plot_tree(
            self.tree_model,
            filled=True,
            feature_names=self.X.columns.tolist(),  # Convert Index to list
            max_depth=3,
            fontsize=10,
        )
        plt.title("Decision Tree Visualization")
        plt.show()

    def print_evaluation_metrics(self):
        """
        Print the evaluation metrics of the decision tree model.
        """
        print(f"Mean Absolute Error: {self.mae}")
        print(f"Mean Squared Error: {self.mse}")
        print(f"Coefficient of Determination (R2 Score): {self.r2}")
