# 🏡 House Price Prediction App

An AI-powered web application built with Streamlit that allows users to:
- Predict house prices based on features like square footage, number of bedrooms, etc.
- Explore housing price trends across Indian cities using an interactive map.

---

## 🚀 Features

- 🔮 **House Price Predictor**:
  - Predicts prices using **Linear Regression** and **Random Forest** models.
  - Accepts custom input features.
  - Supports file upload for bulk predictions.

- 🗺️ **Interactive Map Tool**:
  - Visualizes average and median prices by city.
  - Provides quick insights with tooltips and filtering.

---

## 🧠 Technologies Used

| Technology     | Purpose                          |
|----------------|----------------------------------|
| Streamlit      | Web app framework                |
| Pandas         | Data manipulation                |
| Scikit-learn   | Machine Learning models          |
| Matplotlib     | Data visualization (charts)      |
| Pydeck         | Interactive geographic mapping   |
| Seaborn        | Data visualization (optional)    |

---
# ⚙️ How to Run Locally
## 1. Clone the repo
git clone https://github.com/yourusername/house-price-app.git
cd house-price-app

## 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## 3. Install dependencies
pip install -r requirements.txt

## 4. Run the app
streamlit run main_app.py


## 📁 Folder Structure

```plaintext
house-price-app/
│
├── main_app.py                     # Main homepage for app
├── model1.py                       # Contains preprocessing & ML logic
├── data.csv                        # Sample dataset for testing and mapping
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview
├── .gitignore                      # Git ignore file
└── pages/
    ├── 1_House_Price_Predictor.py  # UI for prediction tool
    └── 2_Interactive_Map.py        # UI for the map visualization
```
## TO CHANGE IN WEBSITE RUN BELOW CODE AFTER CHANGING IN VS CODE
git add .
git commit -m "Describe your change here"
git push


---
# 👨‍💻 Author
Developed by @cyberKrish[Krish Kumar]
