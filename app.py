import gradio as gr
import replicate
import os

def dance_api(image, video):
    # استخدام المفتاح السري المخزن في الإعدادات
    client = replicate.Client(api_token=os.environ.get("REPLICATE_API_TOKEN"))
    
    # استدعاء نموذج تحريك الصور
    output = client.run(
        "lucataco/animate-anyone:4fef005",
        input={"image": image, "video": video}
    )
    return output

demo = gr.Interface(
    fn=dance_api,
    inputs=[gr.Image(type="filepath"), gr.Video()],
    outputs=gr.Video(),
    title="Latakiano AI Dance 🕺"
)

demo.launch()