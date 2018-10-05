from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def form():
    return render_template(
        'form.html',
        favicon_url=url_for('static', filename='favicon.ico'),
    )


if __name__ == "__main__":
    app.run()
