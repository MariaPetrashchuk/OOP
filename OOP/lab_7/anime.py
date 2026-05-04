from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

@app.route('/')
def home():
    j = jikan.anime(54595, extension='episodes')
    a = ""
    
    for episode in j["data"]:
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}</p>"
    
    return a

@app.route('/season')
def season():
    data = jikan.seasons_now()
    result = ""
    
    for anime in data["data"][:10]:
        result += f"<p>{anime['title']} — оцінка: {anime['score']}</p>"
    
    return result

@app.route('/about')
def about():
    return "<h1>Про сайт</h1>"

if __name__ == '__main__':
    app.run(debug=True)