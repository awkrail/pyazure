# pyazure
pyazure is python api for microsoft azure

## Usage

### Speech API
~~~~
speech = Speech("your_api_key")
wave = speech.text_to_speech(language, gender, name, text)
~~~~

language series, gender, and name is decided by MicroSoft.

please see this site: [reference](https://docs.microsoft.com/ja-jp/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput)
