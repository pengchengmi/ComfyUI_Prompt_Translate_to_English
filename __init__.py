# 2023年12月3日 修复 阿里云导入失败，但还可以使用百度云的问题。
try:
    from .nodes.aliapi import NODE_CLASS_MAPPINGS as aliapi_c, NODE_DISPLAY_NAME_MAPPINGS as aliapi_n
except ImportError:
  print('阿里云API导入失败')
  aliapi_c = {}
  aliapi_n = {}

from .nodes.baiduapi import NODE_CLASS_MAPPINGS as baidu_c, NODE_DISPLAY_NAME_MAPPINGS as baiduapi_n
from .nodes.baidu import NODE_CLASS_MAPPINGS as baiduapi_c, NODE_DISPLAY_NAME_MAPPINGS as baidu_n
from .nodes.previewtext import NODE_CLASS_MAPPINGS as preview_c, NODE_DISPLAY_NAME_MAPPINGS as preview_n

NODE_CLASS_MAPPINGS = {
    **aliapi_c,
    **baidu_c,
    **baiduapi_c,
    **preview_c
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **aliapi_n,
    **baiduapi_n,
    **baidu_n,
    **preview_n
}

import os
import __main__
import shutil

# 获取js的文件路径
BaiduTS_js_dir_path = os.path.dirname(os.path.relpath(__file__))
BaiduTS_js_path = os.path.join(BaiduTS_js_dir_path, 'js')

# 获取 web的文件夹路径 ---拼合 web -----获取文件夹路径 ----获取当前Comfyui的路径
Comfyui_web_dir_path = os.path.join(os.path.dirname(os.path.relpath(__main__.__file__)), 'web')
Comfyui_js_path = os.path.join(Comfyui_web_dir_path, 'extensions')

# 节点名称
Translate_Nodes_Name = '提示词翻译'
Translate_Js_Name = 'BaiduTranslatePreview.js'


# 向主程序目录中，添加js文件 / 其他文件
def addFilesToFolder(webJsDir, BaiduTsjsDir, nodes):
    webJsFileDir = os.path.join(webJsDir, Translate_Js_Name)
    print(webJsFileDir)
    BaiduTranslateJsDir = os.path.join(BaiduTsjsDir, Translate_Js_Name)
    print(BaiduTranslateJsDir)

    # 要是文件中 存在这个 文件，则删掉，重新复制
    if os.path.exists(webJsFileDir):
        os.remove(webJsFileDir)

    # 复制文件到 web的js目录中
    shutil.copy(BaiduTranslateJsDir, webJsFileDir)


def addComfyUINodesToCanvas(nodes):
    pass


# 向主程序中 安装 Nodes
def installNodes():
    # 调用 添加js文件 进 web文件夹中的 函数
    addFilesToFolder(Comfyui_js_path, BaiduTS_js_path, Translate_Nodes_Name)

    __all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
    # 调用检查模块 的函数

    # 调用添加 Nodes 到 画布之中。
    # addComfyUINodesToCanvas(Translate_Nodes_Name)

# 调用Js文件
installNodes()
