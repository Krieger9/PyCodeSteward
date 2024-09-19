import gradio as gr
from CsFunctionGenerator import CsFunctionGenerator

generator = CsFunctionGenerator()

def SendMessage(message):
    result = generator.ExtractFunctionRequirements(message)
    return result.RequestedClarifications

interface = gr.Interface(
    fn=SendMessage, 
    inputs=gr.Textbox(lines=2, placeholder="Type Instructions..."), 
    outputs=gr.Textbox(lines=10, placeholder="Type Instructions...")
)

if __name__ == "__main__":
    interface.launch(show_api=False, server_port=8082, server_name="0.0.0.0", share=True)