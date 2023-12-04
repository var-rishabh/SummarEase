from flask import Flask, render_template, request
from summarizer import get_summarized_text

app = Flask(__name__)


def summarizedText(text):
    return get_summarized_text(text, type=1, lines=10)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        text = request.form.get("text")
        return render_template("summarize.html", summary=summarizedText(text))
    else:
        return render_template("summarize.html")


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8080,
        debug=True,
    )
