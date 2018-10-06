from flask import Flask, render_template, request

from typograph import get_processed_text

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    source_text = formatted_text = ''

    if request.method == 'POST':
        source_text = request.form['text']
        formatted_text = get_processed_text(source_text)

    return render_template(
        'form.html',
        source_text=source_text,
        formatted_text=formatted_text,
    )


if __name__ == "__main__":
    app.run()
