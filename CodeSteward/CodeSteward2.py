import gradio as gr
from CsFunctionGenerator import CsFunctionGenerator

generator = CsFunctionGenerator()

def process_description(message):

    result = generator.ExtractFunctionRequirements(message)
    suggestions = ""
    return result.RequestedClarifications, suggestions    

def generate_code(context):
    # Generate code based on final context
    return final_code

with gr.Blocks() as interface:
    gr.Markdown("## Code Generation Interface")
    
    with gr.Row(equal_height=True):
        with gr.Column():
            description = gr.Textbox(label="Describe the Function", lines=15, placeholder="Enter your function description here...")
            submit_description = gr.Button("Submit")
        with gr.Column():
            clarifications = gr.Textbox(label="Requested Clarifications", lines=12)
            suggestions = gr.Textbox(label="Code Suggestions", lines=5)
            with gr.Row():
                accept_suggestion = gr.Button("Accept")
                decline_suggestion = gr.Button("Decline")    
    
    submit_description.click(process_description, inputs=[description], outputs=[clarifications, suggestions])    

if __name__ == "__main__":
    interface.launch(show_api=False, server_port=8082, server_name="0.0.0.0", share=True)
