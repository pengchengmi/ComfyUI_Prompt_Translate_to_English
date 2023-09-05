import { app } from "../scripts/app.js";
import { ComfyWidgets } from "../scripts/widgets.js";

app.registerExtension({
  name: "Comfy.BaiduTranslateNode",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === "PreviewText") {
      const onNodeCreated = nodeType.prototype.onNodeCreated;

      nodeType.prototype.onNodeCreated = function () {
        const r = onNodeCreated
          ? onNodeCreated.apply(this, arguments)
          : undefined;

        let PreviewTextNode = app.graph._nodes.filter(
            (wi) => wi.type === "PreviewText"
          ),
          nodeName = `PreviewText_${PreviewTextNode.length}`;

        console.log(`Create PreviewText: ${nodeName}`);

        ComfyWidgets.STRING(
          this,
          nodeName,
          [
            "STRING",
            {
              default: "",
              placeholder: "翻译结果 / Translate results in here",
              multiline: true,
            },
          ],
          app
        );


        this.onDrawBackground = function () {
          const output = app.nodeOutputs[this.id + ""];
          if (output && output.string) {
            this.widgets[0].inputEl.value = output.string[0];
          }
        };
        return r;
      };
    }
  },
});
