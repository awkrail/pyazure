import urllib
import request
import uuid

class Speech():
    HOST = "https://speech.platform.bing.com"
    USER = "SpeechAPI"
    UNIQUE_ID = str(uuid.uuid4()).replace("-", "")

    def __init__(self, api_key):
        self.instance_id = self.__generate_id()
        self.token = ""
        self.authorize(api_key)
    
    def authorize(self, api_key):
        url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
                "Ocp-Apim-Subscription-Key":api_key
                }
        response = request.post(url, headers=headers)
        if response.ok:
            self.token = str(response)[2:-1]
        else:
            response.raise_for_status()

    # if you want to select only lang, gender, name,
    # and text, please use this method
    def text_to_speech(self, text):
        template = """
        <speak version='1.0' xml:lang={0}>
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
        name = self.get_name(lang, female)
        data = template.format(lang, "Female" if female else "Male", name, text)
        
        response = request.post(url, data=data, headers=headers)

        if response.ok:
            return response.content
        else:
            raise response.raise_for_status()

    # TODO: あとでやる
    @classmethod
    def get_name(cls, lang, female):
        pass

    @classmethod
    def __generate_id(cls):
        return str(uuid.uuid4()).replace("-", "")
