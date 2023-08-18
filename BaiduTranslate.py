import http.client
import hashlib
import urllib
import random
import json

appid = ''  # 填写你的appid
secretKey = ''  # 填写你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'

class BaiduTranslate:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {"text": ("STRING", {"multiline": True})},
        }
        # return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", )}}

    RETURN_TYPES = ("STRING",)

    FUNCTION = "translation"

    CATEGORY = "Promat-translate"

    def translation(self, text):
        fromLang = 'auto'  # 原文语种
        toLang = 'en'  # 译文语种
        salt = random.randint(32768, 65536)
        q = text

        sign = appid + q + str(salt) + secretKey

        sign = hashlib.md5(sign.encode()).hexdigest()
        newmyurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')

        try:
            httpClient.request('GET', newmyurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            # print(result)
            print("翻译结果是" + result['trans_result'][0]['dst'])
            translate_result = result['trans_result'][0]['dst']

        except Exception as e:
            print(e)
            httpClient.close()
            translate_result = q

        return (translate_result,)



# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BaiduTranslate": BaiduTranslate
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BaiduTranslate": "百度翻译-中文-->英文"
}
