from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack  # ✅ Sparse-safe feature stacking

app = Flask(__name__)

# 📄 Load dataset
data = pd.read_csv("recipe_final (1).csv")

# 🧂 Vectorize ingredient text
vectorizer = TfidfVectorizer()
X_ingredients = vectorizer.fit_transform(data['ingredients_list'])

# 📊 Normalize numerical features
scaler = StandardScaler()
X_numerical = scaler.fit_transform(
    data[['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']])

# 🧠 Combine both sets of features (sparse + dense)
X_combined = hstack([X_numerical, X_ingredients])

# 🔍 Train KNN model
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(X_combined)


# 📌 Truncate helper
def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    return text


# 🔁 Recommendation logic
def recommend_recipes(input_features):
    # Scale nutrition features
    input_features_scaled = scaler.transform([input_features[:7]])
    # Transform ingredient text
    input_ingredients_transformed = vectorizer.transform([input_features[7]])
    # Combine using sparse hstack
    input_combined = hstack([input_features_scaled, input_ingredients_transformed])
    # Get neighbors
    distances, indices = knn.kneighbors(input_combined)
    # Return recommended recipes
    recommendations = data.iloc[indices[0]]
    return recommendations[['recipe_name', 'ingredients_list', 'image_url']].head(5)


# 🌐 Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get user input
            calories = float(request.form['calories'])
            fat = float(request.form['fat'])
            carbohydrates = float(request.form['carbohydrates'])
            protein = float(request.form['protein'])
            cholesterol = float(request.form['cholesterol'])
            sodium = float(request.form['sodium'])
            fiber = float(request.form['fiber'])
            ingredients = request.form['ingredients']

            input_features = [calories, fat, carbohydrates, protein, cholesterol, sodium, fiber, ingredients]

            # Get recipe recommendations
            recommendations = recommend_recipes(input_features)

            return render_template('index.html', recommendations=recommendations.to_dict(orient='records'),
                                   truncate=truncate)
        except Exception as e:
            return f"Error occurred: {e}"

    return render_template('index.html', recommendations=[])


# ▶ Run app
if __name__ == '__main__':
    app.run(debug=True)