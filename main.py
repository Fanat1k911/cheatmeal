from flask import Flask, render_template, request

app = Flask(__name__)

# from app import routes


@app.route('/')
def hello_world():
    user = {'username': 'Alex'}
    return render_template(
        'index.html',
        title='Home',
        user=user,
    )


if __name__ == '__main__':
    app.run()