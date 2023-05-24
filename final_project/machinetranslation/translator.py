"""This module does translation"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def translate(text, model_id='en-fr'):
    '''Translates a text input into another language based on model_id provided'''
    return language_translator.translate(
        text=text,
        model_id=model_id).get_result()

translation = translate('Hello, how are you today?')
print(json.dumps(translation, indent=2, ensure_ascii=False))


def english_to_french(englishText):
    '''Translates English to French'''
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return frenchText


print(english_to_french('Hello, how are you today?'))

def french_to_english(frenchText):
    '''Translates French to English'''
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return englishText


print(french_to_english('Bonjour, comment ça va?'))
