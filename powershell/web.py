from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }

    all_movies = []
    
    # 1페이지부터 5페이지까지 총 100개의 영화 데이터를 불러옵니다.
    for page in range(1, 6):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            movies_data = response.json()
            all_movies.extend(movies_data['results'])

    return render_template('index.html', movies=all_movies)

if __name__ == '__main__':
    app.run(debug=True)