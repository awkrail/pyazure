import urllib
import requests
import uuid
import json

class Speech():
    HOST = "https://speech.platform.bing.com"
    USER = "SpeechAPI"
    UNIQUE_ID = str(uuid.uuid4()).replace("-", "")

    def __init__(self, api_key):
        self.instance_id = self.__generate_id()
        self.token = ""
        self.authorize(api_key)
        self.wave = b""
    
    def authorize(self, api_key):
        url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
                "Ocp-Apim-Subscription-Key":api_key
                }
        response = requests.post(url, headers=headers)
        if response.ok:
            self.token = str(response.content)[2:-1]
        else:
            response.raise_for_status()

    # if you want to select only lang, gender, name,
    # and text, please use this method
    def text_to_speech(self, lang,  name, text):
        template = """
        <speak version='1.0' xml:lang='{0}'>
            <voice xml:lang='{0}' xml:gender='{1}' name='{2}'>
                {3}
            </voice>
        </speak>
        """
        url = self.HOST + "/synthesize"
        headers = {
                "Content-type": "application/ssml+xml",
                "X-Microsoft-OutputFormat":"riff-16khz-16bit-mono-pcm",
                "Authorization": "Bearer " + self.token,
                "X-Search-AppId": self.UNIQUE_ID,
                "X-Search-ClientID": self.instance_id,
                "User-Agent": self.USER
                }
        head_tmp, gender = self.get_head_template_and_gender(lang, name)
        data = template.format(lang, gender, head_tmp, text)
        response = requests.post(url, data=data, headers=headers)

        if response.ok:
            self.wave = response.content
        else:
            raise response.raise_for_status()

    def text_to_speech_with_ssml(self, ssml):
        url = self.POST + "/synthesize"
        headers = {
                "Content-Type": "application/ssml+xml",
                "X-Microsoft-OutputFormat":"riff-16khz-16bit-mono-pcm",
                "Authorization": "Bearer " + self.token,
                "X-Search-AppId": self.UNIQUE_ID,
                "X-Search-ClientID": self.instance_id,
                "User-Agent": self.USER
                }
        response = requests.post(url, data=data, headers=headers)

        if response.ok:
            self.wave = response.content
        else:
            raise response.raise_for_status()

    def save(self, path):
        with open(path, "wb") as f:
            f.write(self.wave)

    @classmethod
    def get_head_template_and_gender(cls, lang, name):
        template = "Microsoft Server Speech Text to Speech Voice ({0}, {1})"
        with open("data/voice.json", "r") as f:
            voice = json.load(f)

        if lang in voice["langs"]:
            # nameで同様のことをする
            index = voice["langs"].index(lang)
            target_dict = voice["voices"][index]
            if name in target_dict["name"]:
                gender_i = target_dict["name"].index(name)
                gender = target_dict["gender"][gender_i]
                return template.format(lang, name), gender
            else:
                raise ValueError("this name is wrong")
        else:
            raise ValueError("this input language is not supported")

    @classmethod
    def __generate_id(cls):
        return str(uuid.uuid4()).replace("-", "")
