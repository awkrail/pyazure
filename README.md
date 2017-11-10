# pyazure
pyazure is python api for microsoft azure.

I am going to develop python wrapper simple azure api as many as possible.

## Usage

### Speech API
```python
speech = Speech("your_api_key")
speech.text_to_speech(language, name, text)

# you can get wave from speech
speech.wave

# save
speech.save("path")
```

language series, gender, and name is decided by MicroSoft.

please see this site: [reference](https://docs.microsoft.com/ja-jp/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput)
