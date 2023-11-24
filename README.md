# 阿里云、百度、腾讯云翻译支持
    已无需手动安装

 |  [English](#1-baidutranslateapi-install) | [中文教程](#comfyui-提示词翻译插件) | [视频教程](https://www.bilibili.com/video/BV1qw411Q7U9/?share_source=copy_web&vd_source=09df7e2da9d48d5fb9dcfe4ed69f071b) | [更新内容](#历史更新内容) |
# ComfyUI Prompt Translate to English
    introduction:
    1. I created two translation nodes, which can be both installed or only one of them can be used；
    2. first one is `BaiduTranslateApi`, it's used BaiduTranslate developer account 
       on the official website of Baidu Translator, which can be used for a long time by oneself;
    3. second is `BaiduTranslate`, Connected to the Api of Baidu Translate， Need install requirements；
    4. unable to preview the prompt words in Comfyui, i dont know how to do it. If you have any good ideas, Let me know!
    5. I didn't use Google Translate because I need to use it in China.
## 1. `BaiduTranslateApi` install
1. Download **Baidutranslate** zip，Place in `custom_nodes` folder, Unzip it；
2. Go to ‘[Baidu Translate Api](https://fanyi-api.baidu.com/?fr=pcHeader)’ and register a developer account，get your `appid` and `secretKey`；
3. Open the file `BaiduTranslate.py` in Notepad/other editors;
4. Fill your `apiid` in quotation marks of `appid = ""` at line 11；
4. Fill your `secretKey` in quotation marks of `secretKey = ""` at line 11；
6. Save file.
## 2. `BaiduTranslate` install
1. If you are using your own deployed Python environment and Comfyui, not use author's integration package，run `install.bat`；
2. If you are using the author compressed Comfyui integration package，run `embedded_install.bat`；

## 3. `PreviewText` Nodes
1. Preview translate result。

## 4. How to use
1. Nodes in Prompt translate list，if you use own Api, use `翻译Api auto to English`；
2. you can install both, whatever use.
![节点使用演示](./img/BaiduTranslate.png)
-----
# ComfyUI 提示词翻译插件
    简介：
    1. 有两个版本，一个是`BaiduTranslateApi`，这个需要去百度翻译官网注册开发者账号，可以自己长久使用。
    2. 第二个版本是`BaiduTranslate`，我爬了百度翻译的接口，不被百度反爬也可以长期使用。
    3. 暂时没法在comyfui中预览到提示词和修改，涉及到知识盲区，若大家有好的想法可以提出来！
## 1. `BaiduTranslateApi`的安装教程
1. 下载 **Baidutranslate** 压缩包，放到`custom_nodes`文件夹中；
2. 先去百度翻译，在上面点开 ‘[翻译API](https://fanyi-api.baidu.com/?fr=pcHeader)’ 注册一个开发者账号，获得你的`appid`和`secretKey`；
3. 记事本/其他编辑器打开文件`BaiduTranslate.py`；
4. 第11行 `appid = ""` **引号**之中填写你的百度翻译`apiid`；
5. 第12行`secretKey = ""`  **引号**之中填写你的百度翻译 `secretKey`；
6. 保存文件.
## 2. `BaiduTranslate`的安装教程
1. 如果使用的是 自己部署的python环境和Comfyui，不是下载的作者的整合包，则运行`install.bat`；
2. 如果使用的是 作者压缩的Comfyui整合包，则运行`embedded_install.bat` --- 大多数都是这个！！；

## 3. `PreviewText` 节点
1. 预览翻译的结果；
2. 感谢B站网友给的建议，以及B站用户【阿米吉】提供的代码与思路。

## 4. 使用教程
1. 节点在Prompt translate列表中，如果用自己的Api，直接用`翻译Api auto to English`；
2. 也可以两个都安装，随便用一个，本质上没啥区别。
![节点使用演示](./img/BaiduTranslate.png)

# 历史更新内容
### 2023-9-01
1. 更新了文本预览节点

### 2023-09-14
1. 更新 可以在翻译节点内，选择翻译成语言，这样可以用作反推提示词。

### 2023-10-05
1. 更新了文本预览的实现方式，看看还有没有 冻结的问题。
