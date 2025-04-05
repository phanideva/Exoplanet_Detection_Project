# ML Model Module

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run():
    print("Training a mock ML model on synthetic features...")
    np.random.seed(0)
    X = np.random.rand(100, 3)
    y = np.random.randint(0, 2, size=100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    with open("models/ml_results.txt", "w") as f:
        f.write(f"Model accuracy: {acc}")
    print(f"Model accuracy saved to models/ml_results.txt")
