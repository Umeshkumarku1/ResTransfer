import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the data
data_path = r"C:\Users\Lenovo\Desktop\Mutation tool\Gene_Counts.xlsx"
df = pd.read_excel(data_path)

# Prepare features and target
features = df.drop(columns=["Category", "Total_Score"])  # Drop target and non-feature columns
target = df["Category"]

# Convert non-numerical columns to numerical
for col in features.columns:
    if features[col].dtype == 'object':
        print(f"Converting column '{col}' to numerical values.")
        le = LabelEncoder()
        features[col] = le.fit_transform(features[col])

# Encode the target variable
target_mapping = {
    "High chance for antibiotic resistance gene transfer": 2,
    "Moderate chance for antibiotic resistance gene transfer": 1,
    "Low chance for antibiotic resistance gene transfer": 0
}
target_encoded = target.map(target_mapping)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target_encoded, test_size=0.3, random_state=42)

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature importance (optional)
feature_importances = pd.DataFrame(rf_model.feature_importances_, index=features.columns, columns=["Importance"]).sort_values("Importance", ascending=False)
print("\nFeature Importances:\n", feature_importances)

# Save the model (optional)
import joblib
model_path = r"C:\Users\Lenovo\Desktop\Mutation tool\random_forest_model.pkl"
joblib.dump(rf_model, model_path)
print(f"Model saved at {model_path}")
