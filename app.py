from flask import Flask, render_template, request

app = Flask(__name__)


def summarizedText(text):
    return f"This is a summary of the {text}"


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "GET":
        return render_template("summarize.html")
    else:
        return render_template(
            "summarize.html", summary=summarizedText(request.form["text"])
        )


if __name__ == "__main__":
    app.run()
