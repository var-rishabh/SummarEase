# SummarEase : Text Summarization Web Application

Welcome to SummarEase, your go-to web application for effortless text summarization powered by advanced machine learning.


![Python](https://img.shields.io/badge/Python-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-black.svg?style=for-the-badge&logo=Flask&logoColor=white)
![HTML](https://img.shields.io/badge/html5-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css3-blue.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)


## Overview

SummarEase offers a user-friendly interface for inputting paragraphs and receiving concise summaries. The machine learning model employs the TextRank Algorithm, providing effective text processing capabilities and contributing to the dynamic field of natural language processing.

## Key Features

- **User-Centric Design:** Intuitive interface for seamless interaction.
- **Machine Learning Model:** TextRank Algorithm for effective summarization.
- **Datasets:**
  - *BBC News Summary:* Ensuring robust summarization capabilities.
  - *Glove6B:* Enhancing the model's ability to understand and process textual content.
- **Libraries:** 
  - numpy: For numerical operations and array handling.
  - pandas: For data manipulation and analysis.
  - NLTK (Natural Language Toolkit): For natural language processing tasks.
  - networkx: Used for graph-based algorithms, essential for TextRank.
  - ROUGE: A package for automatic evaluation of summaries.


## Algorithm Used
The summarization algorithm employed in this project is the TextRank Algorithm. This algorithm is known for its effectiveness in identifying key sentences and phrases within a given text, forming the basis for the generated summaries.

## How to Run

```
1. Clone this repository

$ git clone https://github.com/var-rishabh/SummarEase.git
```
```
2. Navigate to the project directory

$ cd SummarEase
```
```
1. Navigate to the project directory

$ pip install -r requirements.txt
```
```
4. Run the Flask application

$ python app.py (Non Debug Mode)

or

$ flask --app app.py --debug run (Debubg Mode)
```

## Usage

- Input the text or paragraphs or link you want to summarize.
- Choose the number of lines of the output.
- Click the "Summarize" button.
- Receive a concise summary based on the TextRank Algorithm.

## Additional Information

For any questions, issues, or contributions, feel free to open an issue. 
Your feedback and collaboration are highly valued.

> Enjoy summarizing text effortlessly with our machine learning-powered web application!