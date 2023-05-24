import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translation = machinetranslation.translator.english_to_french(textToTranslate)
    return translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translation = machinetranslation.translator.french_to_english(textToTranslate)
    return translation

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    from flask import make_response, render_template
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html'),200,headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
