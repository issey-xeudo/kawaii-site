from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Данные, которые мы будем передавать в шаблон
    title = "Мой сайт"
    description = "Это сайт с динамическим контентом!"
    return render_template('index.html', title=title, description=description)

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)