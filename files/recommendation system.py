import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from tqdm import tqdm

# Features for users and jobs
user_features = ['age', 'gender', 'city', 'resume', 'description', 'role']
job_features = ['job_title', 'location', 'type_of_collaboration', 'job_description', 'salary', 'required_skills']

# Number of samples
n_samples = 500

# Generate synthetic dataset
features, labels = make_classification(
    n_samples=n_samples,
    n_features=len(user_features) + len(job_features),
    n_informative=len(user_features) + len(job_features) - 2,
    n_clusters_per_class=1,
    random_state=42
)

# Split features into user and job features
user_data = features[:, :len(user_features)]
job_data = features[:, len(user_features):]

# Create DataFrames for user and job data
user_df = pd.DataFrame(user_data, columns=user_features)
job_df = pd.DataFrame(job_data, columns=job_features)

# Combine user and job data into a single dataset
df = pd.concat([user_df, job_df], axis=1)

# Add a binary label (0 or 1) indicating whether a user would be interested in a job
df['label'] = labels

# Save the dataset to a CSV file
df.to_csv('job_recommendation_dataset.csv', index=False)

# Display a few rows of the generated dataset
print("Generated Dataset:")
print(df.head())

# Visualize relationships between features using a pair plot
sns.pairplot(df, hue='label', diag_kind='kde')
plt.show()

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Correlation Matrix")
plt.show()

# Load the generated dataset
df = pd.read_csv('job_recommendation_dataset.csv')

# Split the dataset into training and testing sets
X = df.drop('label', axis=1)  # Features
y = df['label']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Collaborative Filtering: Matrix Factorization (SVD)
svd = TruncatedSVD(n_components=10, random_state=42)  # Change n_components to the desired number

# Standardize features for collaborative filtering with SVD for training data
scaler_svd = StandardScaler()
X_train_svd = svd.fit_transform(scaler_svd.fit_transform(X_train))

# Apply the same transformation to the test data
X_test_svd = svd.transform(scaler_svd.transform(X_test))

# Train a logistic regression model for collaborative filtering with SVD
logreg_svd = LogisticRegression()
logreg_svd.fit(X_train_svd, y_train)

# Train a Random Forest model
rf_model = RandomForestClassifier(random_state=42)
with tqdm(total=rf_model.n_estimators, desc="Training Random Forest") as pbar:
    rf_model.fit(X_train, y_train)
    pbar.update(rf_model.n_estimators)

# Train a Support Vector Machine (SVM) model
svm_model = SVC(random_state=42)
with tqdm(desc="Training SVM") as pbar:
    svm_model.fit(X_train, y_train)
    pbar.update(1)

# Train a Gradient Boosting model
gb_model = GradientBoostingClassifier(random_state=42)
with tqdm(total=gb_model.n_estimators, desc="Training Gradient Boosting") as pbar:
    gb_model.fit(X_train, y_train)
    pbar.update(gb_model.n_estimators)

# Predictions
y_pred_svd = logreg_svd.predict(X_test_svd)
y_pred_rf = rf_model.predict(X_test)
y_pred_svm = svm_model.predict(X_test)
y_pred_gb = gb_model.predict(X_test)

# Evaluate Models
print("\nCollaborative Filtering (SVD):")
print(f"Accuracy: {accuracy_score(y_test, y_pred_svd):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_svd):.2f}")

print("\nRandom Forest:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_rf):.2f}")

print("\nSupport Vector Machine (SVM):")
print(f"Accuracy: {accuracy_score(y_test, y_pred_svm):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_svm):.2f}")

print("\nGradient Boosting:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_gb):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_gb):.2f}")

# Recommendation System

# Get user preferences
user_preferences = {}
print("\nEnter your preferences (values between 0 and 1):")
for feature in user_features:
    user_preferences[feature] = float(input(f"{feature}: "))

# Display category boundaries
print("\nCategory boundaries:")
for feature in user_features:
    print(f"{feature}: [0, 1]")

# Convert user preferences to DataFrame
user_preferences_df = pd.DataFrame([user_preferences])

# Predict interest for each job for the given user
user_preferences_svd = svd.transform(scaler_svd.transform(user_preferences_df))
user_interest_probabilities = svm_model.predict_proba(user_preferences_svd)[:, 1]

# Rank jobs based on predicted probabilities
recommendations = df[['job_title', 'job_description']].copy()
recommendations['predicted_interest'] = user_interest_probabilities
recommendations = recommendations.sort_values(by='predicted_interest', ascending=False)

# Display recommended jobs
print("\nRecommended Jobs:")
print(recommendations[['job_title', 'job_description', 'predicted_interest']].head())