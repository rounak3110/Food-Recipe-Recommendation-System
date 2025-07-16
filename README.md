# 🥗 Food Recipe Recommendation System

A smart web-based system that recommends delicious recipes based on nutritional input and ingredients using machine learning. Built with 💻 Python, Flask, and HTML/CSS in a soft pastel theme.

---

## 📸 Preview
! [App Screenshot] ("C:\Users\rounak pathekar\OneDrive\Pictures\Screenshots\Screenshot (11).png")



---

## 🚀 Features

- 🧠 *Smart Recommendations* using K-Nearest Neighbors
- 🥕 Input-based on nutritional values (calories, fat, carbs, etc.)
- 🧂 Ingredient support to personalize results
- 🎨 Clean UI with pastel theme and foody design
- 📱 Responsive layout using Bootstrap

---

## 🔧 Tech Stack

- *Frontend:* HTML, CSS (Bootstrap 4)
- *Backend:* Python, Flask
- *ML Model:* Scikit-learn (KNeighborsClassifier, hstack, sparse features)
- *Data:* Nutritional and recipe data (CSV/JSON based)

---

## 🧪 How It Works

1. User fills in nutritional preferences and ingredients.
2. Features are preprocessed and combined using scipy.sparse.hstack.
3. A KNN model (sklearn.neighbors.NearestNeighbors) finds similar recipes.
4. The top recommendations are displayed beautifully on the webpage.
