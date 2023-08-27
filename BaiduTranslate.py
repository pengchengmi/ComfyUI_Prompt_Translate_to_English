import http.client
import hashlib
import urllib
import random
import json
import requests
import execjs

# BaiduTranslateApi version 使用API需要修改的地方
####################################
appid = '20230817001784543'  # 填写你的appid | fill in your appid
secretKey = 'M9Pttk4NhFX5ypGr0g8O'  # 填写你的密钥 | fill in your secretKey
httpClient = None
myurl = '/api/trans/vip/translate'


class BaiduTransApi:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {"text": ("STRING", {"multiline": True})},
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "translationapi"
    CATEGORY = "Prompt Translate"

    def translationapi(self, text):
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

class BaiduTranslate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {"text": ("STRING", {"multiline": True})},
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "translation"  # 必须和下面的函数同名。
    CATEGORY = "Prompt Translate"

    def translation(self, text):

        From = 'auto'
        To = 'en'

        token = '012cd082bf1f821bb7d94981bf6d477a'
        url = 'https://fanyi.baidu.com/v2transapi'
        headers = {
            'cookie': 'BIDUPSID=3641572D5E0DB57A2F20F8F3373E302C; PSTM=1687090179; '
                      'BAIDUID=3641572D5E0DB57AF59F1D83EEBC5D2B:FG=1; BAIDUID_BFESS=3641572D5E0DB57AF59F1D83EEBC5D2B:FG=1; '
                      'ZFY=sGU1ho9nxRf2CX2bcYMVcfSXr9y2:BmKBeBdv7CDGhUs:C; '
                      'BDUSS'
                      '=tXaEJQVkxBeVBHMllBWWh1aTVZLXlhcVVqTWNCOXJGfmwzUUJmaHphWm1zZGRrSVFBQUFBJCQAAAAAAAAAAAEAAADWpvEyzqiwrsTjtcTQocPXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYksGRmJLBkam; BDUSS_BFESS=tXaEJQVkxBeVBHMllBWWh1aTVZLXlhcVVqTWNCOXJGfmwzUUJmaHphWm1zZGRrSVFBQUFBJCQAAAAAAAAAAAEAAADWpvEyzqiwrsTjtcTQocPXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYksGRmJLBkam; newlogin=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=00aka5a12g80a10g25a52l0g1ie1gm11p; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; delPer=0; H_PS_PSSID=36550_39112_39226_39222_39097_39039_39198_39207_26350_39138_39225_39094_39137_39101; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1692451747; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1692451747; ab_sr=1.0.1_ZmQ3OWYzODRjZGNkOTYxOWI4ZTVhYjRmNTAwNjYyYTUwYmI3OGY2NTViMzhkNWYzM2IxZTVhNjAwNjdkMTU0ODE4Yzc2YmI3OGRmNTY3Y2QxMzZiZDRmZDIwMGIwYmQ2NGI5M2QzZWFlNmNkODBhZjllZDcxNGFkMTEyNmY0NGNhZGZjMTlmOGQ2YjIxNzNhMmUxNDJkMDhlZTM1NjhiZjkyMDc2MmQxN2Q5ODg3NDBkZGViNTEzMDU2NDQzNGEy'}

        js = '''var i = "320305.131321201"
        function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var a = o.charAt(t + 2);
                a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a), a = "+" === o.charAt(t + 1) ? r >>> a : r << a, r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
            }
            return r
        }


        function e(r) {
            var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
            if (null === o) {
                var t = r.length;
                t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
            } else {
                for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++) "" !== e[C] && f.push.apply(f, a(e[C].split(""))), C !== h - 1 && f.push(o[C]);
                var g = f.length;
                g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
            }
            var u = void 0, l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
            u = null !== i ? i : (i = window[l] || "") || "";
            for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                var A = r.charCodeAt(v);
                128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)), S[c++] = A >> 18 | 240, S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224, S[c++] = A >> 6 & 63 | 128), S[c++] = 63 & A | 128)
            }
            for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++) p += S[b], p = n(p, F);
            return p = n(p, D), p ^= s, 0 > p && (p = (2147483647 & p) + 2147483648), p %= 1e6, p.toString() + "." + (p ^ m)
        }
        '''
        q = text

        sign = execjs.compile(js).call("e", q)
        data = {'from': From,
                'to': To,
                'query': q,
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
            translate_result = "translate failed"

        return (translate_result,)


# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BaiduTransApi": BaiduTransApi,
    "BaiduTranslate": BaiduTranslate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BaiduTransApi": "翻译Api  Auto to English",
    "BaiduTranslate": "翻译  Auto to English",
}

