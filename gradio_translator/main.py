import gradio as gr 
from transformers import pipeline

translation_pipeline = pipeline("translation_en_to_fr")

def translate_transformers(from_text):
    translated_results = translation_pipeline(from_text)
    return translated_results[0]

interface = gr.Interface(fn=translate_transformers, 
                         inputs=gr.inputs.Textbox(lines=2, placeholder="Text to translate"), 
                         outputs="text")
interface.launch()