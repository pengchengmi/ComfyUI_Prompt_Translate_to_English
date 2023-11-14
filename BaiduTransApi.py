import http.client
import hashlib
import urllib
import random
import json
import requests

# BaiduTranslateApi version 使用API需要修改的地方
####################################
appid = ''  # 填写你的appid | fill in your appid
secretKey = ''  # 填写你的密钥 | fill in your secretKey
httpClient = None
myurl = '/api/trans/vip/translate'

class BaiduTransApi:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "choose_to_language": (["en", "zh"], {"default": "en"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "baidutranslationapi"
    CATEGORY = "提示词翻译"

    def baidutranslationapi(self, choose_to_language, text):
        fromLang = 'auto'  # 原文语种，可以写auto，让百度自动识别
        toLang = choose_to_language  # 译文语种，固定为 english
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
            result = json.loads(result_all)['trans_result'][0]['dst']

            # print(result)
            print("翻译结果如下—————————————————————————————————————")
            print(result)
            print("Translate results on the top———————————————————")
            translate_result = result

        except Exception as e:
            print(e)
            httpClient.close()
            translate_result = q

        return (translate_result,)

# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BaiduTransApi": BaiduTransApi
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BaiduTransApi": "百度翻译Api"
}
