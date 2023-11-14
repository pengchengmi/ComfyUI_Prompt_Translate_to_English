import requests
import sys
import subprocess
try:
    import execjs
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pyexecjs'])
    import execjs
import os

# 读取百度翻译的加盐算法
js_file_path = os.path.dirname(__file__) + '/js/BaiduTranslate_sign.js'
with open(js_file_path, 'r', encoding='utf-8') as f:
    sign_js = execjs.compile(f.read())

class BaiduTranslate:
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
    FUNCTION = "baidutranslation"  # 必须和下面的函数同名。
    CATEGORY = "Prompt Translate"

    def baidutranslation(self, choose_to_language, text):

        From = 'auto'
        To = choose_to_language

        token = '012cd082bf1f821bb7d94981bf6d477a'
        url = 'https://fanyi.baidu.com/v2transapi'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'cookie': 'BIDUPSID=3641572D5E0DB57A2F20F8F3373E302C; PSTM=1687090179; '
                      'BAIDUID=3641572D5E0DB57AF59F1D83EEBC5D2B:FG=1; BAIDUID_BFESS=3641572D5E0DB57AF59F1D83EEBC5D2B:FG=1; '
                      'ZFY=sGU1ho9nxRf2CX2bcYMVcfSXr9y2:BmKBeBdv7CDGhUs:C; '
                      'BDUSS'
                      '=tXaEJQVkxBeVBHMllBWWh1aTVZLXlhcVVqTWNCOXJGfmwzUUJmaHphWm1zZGRrSVFBQUFBJCQAAAAAAAAAAAEAAADWpvEyzqiwrsTjtcTQocPXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYksGRmJLBkam; BDUSS_BFESS=tXaEJQVkxBeVBHMllBWWh1aTVZLXlhcVVqTWNCOXJGfmwzUUJmaHphWm1zZGRrSVFBQUFBJCQAAAAAAAAAAAEAAADWpvEyzqiwrsTjtcTQocPXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYksGRmJLBkam; newlogin=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=00aka5a12g80a10g25a52l0g1ie1gm11p; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; delPer=0; H_PS_PSSID=36550_39112_39226_39222_39097_39039_39198_39207_26350_39138_39225_39094_39137_39101; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1692451747; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1692451747; ab_sr=1.0.1_ZmQ3OWYzODRjZGNkOTYxOWI4ZTVhYjRmNTAwNjYyYTUwYmI3OGY2NTViMzhkNWYzM2IxZTVhNjAwNjdkMTU0ODE4Yzc2YmI3OGRmNTY3Y2QxMzZiZDRmZDIwMGIwYmQ2NGI5M2QzZWFlNmNkODBhZjllZDcxNGFkMTEyNmY0NGNhZGZjMTlmOGQ2YjIxNzNhMmUxNDJkMDhlZTM1NjhiZjkyMDc2MmQxN2Q5ODg3NDBkZGViNTEzMDU2NDQzNGEy'}

        # sign = execjs.compile(js).call("e", q)
        sign = sign_js.call('e', text)
        data = {'from': From,
                'to': To,
                'query': text,
                'transtype': 'realtime',
                'simple_means_flag': 3,
                'sign': sign,
                'domain': 'common',
                'token': token}

        try:
            baidutranslate = requests.post(url, headers=headers, data=data).json()
            translate_result = baidutranslate['trans_result']['data'][0]['dst']
            print("翻译结果如下—————————————————————————————————————")
            print('翻译结果是--' + translate_result)
            print("Translate results on the top———————————————————")
        except Exception as e:
            print(e)
            translate_result = "Translate failed"

        return (translate_result,)

# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BaiduTranslate": BaiduTranslate
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BaiduTranslate": "百度翻译"
}
