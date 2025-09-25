# 🎬 Movie Recommender System

A content-based movie recommender system built using **Python, Machine Learning, and Streamlit**.  
This project suggests movies based on similarity scores and provides quick access to trailers.  

🔗 **Live Demo**: [Movie Recommender System](https://movie-recommender-system-icyneyuzfrjdf7bmm5pk6u.streamlit.app/)

---

## 📌 Features
- ✅ Recommend top similar movies using **cosine similarity**  
- ✅ Fetch and display movie **posters** via TMDB API  
- ✅ Direct **YouTube trailer links** for recommended movies  
- ✅ Simple, interactive, and user-friendly **Streamlit web app**  
- ✅ Ready to deploy and share — no setup required for end users  

---

## 🛠️ Tech Stack
- **Python 3**
- **Pandas, NumPy, Scikit-learn**
- **Pickle** (for model storage)
- **Streamlit** (for UI & deployment)
- **TMDB API** (for movie posters)

---

## 🚀 Deployment
The app is deployed on **Streamlit Cloud**.  
You can run it locally with:  

```bash
# Clone the repository
git clone https://github.com/your-username/Movie-Recommender-System.git

# Navigate into project folder
cd Movie-Recommender-System

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
