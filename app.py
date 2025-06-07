import gradio as gr
from predict import predictPokemon  # your model's predict function

def process(image):
    return predictPokemon(image)

with gr.Blocks() as demo:
    gr.Markdown("# 💵 Currency Note Speaker")
    gr.Markdown("Upload a currency note image and hear what it is. Designed for visually impaired users.")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload Note Image")
        result = gr.Textbox(label="Prediction")

    with gr.Row():
        clear_btn = gr.Button("Clear")
        submit_btn = gr.Button("Submit")
        speak_btn = gr.Button("🔊 Speak")

    # Predict and display
    submit_btn.click(fn=process, inputs=image_input, outputs=result)

    # Speak result (client-side JavaScript)
    speak_btn.click(
        None,
        inputs=result,
        outputs=None,
        js="""
        (text) => {
            if (!text) return;
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'en-IN';
            window.speechSynthesis.cancel();  // stop previous
            window.speechSynthesis.speak(utterance);
        }
        """
    )

    # Clear inputs
    clear_btn.click(fn=lambda: (None, ""), inputs=None, outputs=[image_input, result])

demo.launch(share=True)
