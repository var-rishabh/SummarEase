# Import necessary modules from Flask
from flask import Flask, render_template, request

# Import the get_summarized_text function from the summarizer module
from summarizer import get_summarized_text

# Create a Flask web application
app = Flask(__name__)


# Define a helper function to generate summarized text
def summarizedText(text, summarizeType=1, length=10):
    return get_summarized_text(text, summarizeType=summarizeType, length=length)


# Define the main route of the web application
@app.route("/")
def main():
    return render_template("main.html")


# Define a route for text summarization
@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        text = request.form.get("text")
        summarizeType = int(request.form.get("type"))
        length = int(request.form.get("length"))

        return render_template(
            "summarize.html", summary=summarizedText(text, summarizeType, length)
        )
    else:
        return render_template("summarize.html")


# Define a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Run the Flask web application if the script is executed directly
if __name__ == "__main__":
    app.run()
