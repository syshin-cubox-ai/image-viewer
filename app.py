import base64

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def view_img():
    img_url = request.args.get('img_url')
    if img_url is None:
        return '<h1>img_url 파라미터를 전달해주세요.</h1>'
    else:
        img_url = base64.urlsafe_b64decode(img_url.encode()).decode()
        return render_template('view.html', img_url=img_url)


@app.route('/debug')
def debug():
    return render_template('debug.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
