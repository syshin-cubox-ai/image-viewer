from flask import Flask, render_template
import base64

app = Flask(__name__)


@app.route('/')
def blank():
    return '파라미터가 없습니다.'


@app.route('/<img_link>')
def view_img(img_link):
    img_link = base64.urlsafe_b64decode(img_link.encode()).decode()
    return render_template('view.html', img_link=img_link)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
