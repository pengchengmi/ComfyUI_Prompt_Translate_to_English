class PreviewText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                },
        }

    RETURN_TYPES = ()
    INPUT_IS_LIST = True
    FUNCTION = "preview_text"
    OUTPUT_NODE = True
    CATEGORY = "提示词翻译"
    # OUTPUT_IS_LIST = True

    def preview_text(self, text):
        return {"ui": {"text": text}, "result": (text,)}

# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "PreviewText": PreviewText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PreviewText": "文本预览"
}
