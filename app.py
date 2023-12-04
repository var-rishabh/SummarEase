# Import necessary modules from Flask
from flask import Flask, render_template, request

# Import the get_summarized_text function from the summarizer module
from summarizer import get_summarized_text

# Create a Flask web application
app = Flask(__name__)


# Define a helper function to generate summarized text
def summarizedText(text, type=1, lines=10):
    return get_summarized_text(text, type=type, lines=lines)


# Define the main route of the web application
@app.route("/")
def main():
    return render_template("main.html")


# Define a route for text summarization
@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Get the input text, summarization type, and lines from the form
        text = request.form.get("text")
        summarizeType = request.form.get("type")
        lines = request.form.get("lines")
        # Render the summarize HTML template with the summarized text
        return render_template(
            "summarize.html", summary=summarizedText(text, summarizeType, lines)
        )
    else:
        # If the request method is GET, render the summarize HTML template without summarization
        return render_template("summarize.html")


# Define a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    # Render a custom 404.html template when a page is not found
    return render_template("404.html"), 404


# Run the Flask web application if the script is executed directly
if __name__ == "__main__":
    app.run()
