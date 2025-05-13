from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Данные, которые мы будем передавать в шаблон
    title = "Мой сайт"
    description = "Это сайт с динамическим контентом!"
    return render_template('index.html', title=title, description=description)

if __name__ == '__main__':
    app.run(host='192.168.100.16', port=5000, debug=True)