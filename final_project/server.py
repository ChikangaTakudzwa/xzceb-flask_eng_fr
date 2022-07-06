from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get(' ')
    # Write your code here
    french = print(translator.english_to_french(textToTranslate))
    return ("Translated text to French:", french)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get(' ')
    # Write your code here
    english = print(translator.french_to_english(textToTranslate))
    return ("Translated text to French:", english)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
