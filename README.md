# pyazure
pyazure is python api for microsoft azure

## Usage

### Speech API
~~~~
speech = Speech("your_api_key")
speech.text_to_speech(language, name, text)

# you can get wave from speech
speech.wave

# save
speech.save("path")
~~~~

language series, gender, and name is decided by MicroSoft.

please see this site: [reference](https://docs.microsoft.com/ja-jp/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput)
