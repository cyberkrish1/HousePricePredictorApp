# import streamlit as st
# from PIL import Image

# st.set_page_config(page_title="🏡 House Price App", layout="wide")
# st.title("🏡 Welcome to the House Price Prediction App")

# # --- Introduction Section ---
# st.markdown("""
#     <style>
#         .intro {
#             font-size: 18px;
#             line-height: 1.6;
#             margin-top: 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div class="intro">
#     Predict house prices with confidence using our AI-powered tool, or explore market trends across major Indian cities through our interactive map.
#     <br><br>
#     🔍 Use the sidebar to navigate between the <b>Prediction Tool</b> and the <b>Interactive Map</b>.
# </div>
# """, unsafe_allow_html=True)

# # --- Display Sample House Image ---
# st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c", caption="Modern Indian Home", use_container_width=True)

# # --- Highlight Features ---
# st.markdown("### ✨ Key Features")
# st.markdown("""
# - 📊 **Predict Prices** using Linear Regression and Random Forest models.
# - 🗺️ **Visualize Trends** with an interactive map showing city-wise average and median prices.
# - 📁 Upload your own CSV dataset to test predictions on custom data.
# """)

# # --- Quick Navigation Buttons ---
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("🔮 Go to House Price Predictor"):
#         st.switch_page("pages/1_House_Predictor.py")
# with col2:
#     if st.button("🗺️ Go to Interactive Map"):
#         st.switch_page("pages/2_Interactive_Map.py")

# # --- Footer ---
# st.markdown("""
# <hr>
# <center>
# Built with ❤️ using Streamlit
# </center>
# """, unsafe_allow_html=True)



import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="🏡 House Price App", layout="wide")

# --- Custom Background & Style ---
st.markdown("""
    <style>
        .stApp {
            background-color: rgb(14, 17, 23);
        }
        .intro {
            font-size: 18px;
            line-height: 1.6;
            margin-top: 10px;
            color: white;
        }
        .highlight {
            font-size: 20px;
            color: #1E90FF;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.02);
        }
        .img-icon-small {
            height: 100px;
            width: 100px;
            border-radius: 10px;
            object-fit: cover;
            margin-bottom: 10px;
        }
        .tool-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        footer {visibility: hidden;}
        h1, h3, h4, h5, h6, .stMarkdown { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- Title with Animation ---
st.title("🏡 Welcome to the House Price Prediction App")
with st.spinner("Loading page..."):
    time.sleep(0.5)

# --- Introduction Section ---
st.markdown("""
<div class="intro">
    Predict house prices with confidence using our AI-powered tool, or explore market trends across major Indian cities through our interactive map.
</div>
""", unsafe_allow_html=True)

# --- Display Sample House Image ---
# st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c", caption="Modern Indian Home", use_container_width=True)

# --- Highlight Features with Emojis ---
st.markdown("### ✨ Key Features")
st.markdown("""
- 📊 <span class="highlight">Predict Prices</span> using Linear Regression and Random Forest models.
- 🗺️ <span class="highlight">Visualize Trends</span> with an interactive map showing city-wise average and median prices.
- 📁 <span class="highlight">Upload your own CSV dataset</span> to test predictions on custom data.
""", unsafe_allow_html=True)

# --- Clickable Image Cards for Navigation ---
st.markdown("### 🚀 Explore Tools")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="tool-card">
        <img src="https://cdn-icons-png.flaticon.com/512/4341/4341139.png" width="100"/>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔮 Try House Predictor", use_container_width=True):
        st.switch_page("pages/1_House_Price_Predictor.py")

with col2:
    st.markdown("""
    <div class="tool-card">
        <img src="https://cdn-icons-png.flaticon.com/512/854/854878.png" width="100"/>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🗺️ Explore Map", use_container_width=True):
        st.switch_page("pages/2_Interactive_Map.py")

# --- Footer ---
st.markdown("""
<hr>
<center style="color:white">
Built with ❤️ using Streamlit
</center>
""", unsafe_allow_html=True)
