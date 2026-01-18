import gradio as gr
import replicate
import os

# ملاحظة: يجب وضع مفتاح الـ API الخاص بك هنا
os.environ["REPLICATE_API_TOKEN"] = "ضع_مفتاح_الـ_API_هنا"

def start_dancing(person_image, motion_video):
    try:
        # استدعاء نموذج تحريك الصور (مثال: نموذج يشبه Animate Anyone)
        output = replicate.run(
            "lucataco/animate-anyone:4fef005", # اسم النموذج على السحابة
            input={
                "image": person_image,
                "video": motion_video
            }
        )
        return output # هذا سيعيد الفيديو الراقص
    except Exception as e:
        return str(e)

# بناء واجهة Latakiano AI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🕺 Latakiano AI Dance Studio")
    gr.Markdown("ارفع صورتك واختر فيديو الرقص (مثل رقصة بابا) لتحويل صورتك إلى فيديو متحرك.")
    
    with gr.Row():
        with gr.Column():
            source_img = gr.Image(type="filepath", label="صورتك الشخصية")
            target_vid = gr.Video(label="فيديو الحركة (Reference Dance)")
            submit_btn = gr.Button("توليد الرقصة الآن ✨", variant="primary")
        
        with gr.Column():
            result_video = gr.Video(label="النتيجة النهائية")

    submit_btn.click(
        fn=start_dancing,
        inputs=[source_img, target_vid],
        outputs=result_video
    )

if __name__ == "__main__":
    demo.launch()