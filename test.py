import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("log_dataset.csv")

X = data["log_text"]
y = data["label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train ML model
model = MultinomialNB()
model.fit(X_vec, y)

print("\n--- CYBER LOG AI (ML MODE) ---\n")

# Test with user input
user_log = input("Paste system log here: ")

user_vec = vectorizer.transform([user_log])
prediction = model.predict(user_vec)

print("AI Result:", prediction[0])
print("Explanation: Result predicted using machine learning model")

print("\n--- End ---\n")




