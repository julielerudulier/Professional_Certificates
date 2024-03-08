import csv
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Import csv file into a DataFrame called 'df' using Pandas library:
    df = pd.read_csv(filename)
    
    # Convert each month into integers:
    df["Month"] = df["Month"].replace(["Jan"], 0)
    df["Month"] = df["Month"].replace(["Feb"], 1)
    df["Month"] = df["Month"].replace(["Mar"], 2)
    df["Month"] = df["Month"].replace(["Apr"], 3)
    df["Month"] = df["Month"].replace(["May"], 4)
    df["Month"] = df["Month"].replace(["June"], 5)
    df["Month"] = df["Month"].replace(["Jul"], 6)
    df["Month"] = df["Month"].replace(["Aug"], 7)
    df["Month"] = df["Month"].replace(["Sep"], 8)
    df["Month"] = df["Month"].replace(["Oct"], 9)
    df["Month"] = df["Month"].replace(["Nov"], 10)
    df["Month"] = df["Month"].replace(["Dec"], 11)
    
    # Convert string or object variables into binary integers:
    df["VisitorType"] = df["VisitorType"].replace(["Returning_Visitor"], 1)
    df["VisitorType"] = df["VisitorType"].replace([["New_Visitor"], ["Other"]], 0)
    
    df["Weekend"] = df["Weekend"].replace([True], 1)
    df["Weekend"] = df["Weekend"].replace([False], 0)

    df["Revenue"] = df["Revenue"].replace([True], 1)
    df["Revenue"] = df["Revenue"].replace([False], 0)
    
    # Assign 'Revenue' values to a list of labels:
    labels = list(df["Revenue"])
    
    # Remove 'Revenue' column from the DataFrame:
    df = df.drop("Revenue", axis=1)
    
    # Assign all other variables to a list of evidence:
    evidence = []
    for i in range(len(df)):
        evidence.append(list(df.loc[i]))
    evidence[0]
    
    # Return tupple (evidence, labels):
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Initialize KNeighbors Classifier:
    classifier = KNeighborsClassifier(n_neighbors=1)

    # Fit classifier on training data:
    classifier.fit(evidence, labels)

    # Return classifier
    return classifier


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # Count total target values in training data, depending on their value:
    total_pos_labels = labels.count(1)
    total_neg_labels = labels.count(0)

    # Initialize sensitivity and specificity variables:
    sensitivity = 0
    specificity = 0

    # Iterate over each prediction:
    for i in range(len(predictions)):

        # If prediction matches label, add count to sensitivity:
        if predictions[i] == labels[i]:
            if predictions[i] == 1:
                sensitivity += 1

            # Otherwise, add count to specificity:
            elif predictions[i] == 0:
                specificity += 1

    # Calculate rate:
    sensitivity /= total_pos_labels
    specificity /= total_neg_labels

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
