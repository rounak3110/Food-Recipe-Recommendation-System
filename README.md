<img width="1878" height="937" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/cc489980-f9f9-46c9-b37e-6fce1b9a14ae" /># 🥗 Food Recipe Recommendation System

A smart web-based system that recommends delicious recipes based on nutritional input and ingredients using machine learning. Built with 💻 Python, Flask, and HTML/CSS in a soft pastel theme.

---

## 📸 Preview

![App Screenshot](<img width="1878" height="937" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/3212a968-6562-4b66-9bfa-9d5aacb70480" />
)



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
