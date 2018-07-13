from flask import Flask, render_template
import github_api

app = Flask(__name__, template_folder='.')

@app.route('/')
def stars_ieducar():
    stars = github_api.get_stars_github()
    return render_template('simple-page.html', value=stars)

if __name__ == "__main__":
    app.run(debug = True)