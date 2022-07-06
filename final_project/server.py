from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(englishText):
    textToTranslate = request.args.get(englishText)
    # Write your code here
    translation = translator.english_to_french(textToTranslate)
    french = print(json.dumps(translation,
    indent=2, ensure_ascii=False))
    return ("Translated text to French:", french)

# @app.route("/frenchToEnglish")
# def frenchToEnglish():
#     textToTranslate = request.args.get('textToTranslate')
#     # Write your code here
#     return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
