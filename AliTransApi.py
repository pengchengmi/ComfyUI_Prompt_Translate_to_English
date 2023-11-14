import json
import sys
import subprocess
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'requests'])
    import requests
try:
    from alibabacloud_alimt20181012.client import Client as alimt20181012Client
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'alibabacloud_alimt20181012'])
    from alibabacloud_alimt20181012.client import Client as alimt20181012Client
try:
    from alibabacloud_tea_console.client import Client as ConsoleClient
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'alibabacloud_tea_console'])
    from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alimt20181012 import models as alimt_20181012_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

# 使用阿里API需要修改的地方
####################################
ALIBABA_CLOUD_ACCESS_KEY_ID = ""
ALIBABA_CLOUD_ACCESS_KEY_SECRET = ""


class AlibabaTransApi:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "choose_to_language": (["en", "zh"], {"default": "en"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "alitranslationapi"
    CATEGORY = "提示词翻译"

    def alitranslationapi(self, choose_to_language, text):
        access_key_id = ALIBABA_CLOUD_ACCESS_KEY_ID
        access_key_secret = ALIBABA_CLOUD_ACCESS_KEY_SECRET

        client = self.create_client(access_key_id, access_key_secret)

        translate_general_request = alimt_20181012_models.TranslateGeneralRequest(
            format_type='text',
            source_language='auto',
            target_language=choose_to_language,
            source_text=text,
            scene='general'
        )

        runtime = util_models.RuntimeOptions()
        try:
            resp = client.translate_general_with_options(translate_general_request, runtime)
            resp_json = json.dumps(resp, default=lambda o: o.__dict__, ensure_ascii=False)
            resp_dict = json.loads(resp_json)
            translate_result = resp_dict['body']['data']['translated']
            #translate_result = resp.Data.Translated
            print("翻译结果如下—————————————————————————————————————")
            print(translate_result)
            print("Translate results on the top———————————————————")
        except Exception as e:
            print(e)
            translate_result = "Translate failed"

        return translate_result,

    @staticmethod
    def create_client(access_key_id, access_key_secret):
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret
        )
        config.endpoint = 'mt.aliyuncs.com'
        return alimt20181012Client(config)

NODE_CLASS_MAPPINGS = {
    "AlibabaTransApi": AlibabaTransApi
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AlibabaTransApi": "阿里翻译Api"
}