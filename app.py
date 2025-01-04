import os 
import ollama
import gradio as gr

OLLAMA_MODEL = "llama3.2"

SYSTEM_MESSAGE = "You are a helpful assistant in a accessories store. You should try to gently encourage \
the customer to try items that are on sale.HandBags are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a Purse', \
you could reply something like, 'Wonderful - we have lots of Handbags - including several that are part of our sales evemt.'\
Encourage the customer to buy Handbags if they are unsure what to get."

def chat(message, history=[]):

    relevant_system_message = SYSTEM_MESSAGE
    keywords = ['discount', 'offer', 'promotion']  # Define words that imply customer is looking for a better deal

    if 'belt' in message.strip().lower():
        relevant_system_message += (
            " The store does not sell belts; if you are asked for belts, be sure to point out other items on sale."
        )
    elif any(word in message.strip().lower() for word in keywords):  # Use elif for clarity
        relevant_system_message += (
            " If the customer asks for more money off the selling price, the store is currently running 'buy 2 get one free' campaign, so be sure to mention this."
        )
    messages = [{"role": "system", "content": relevant_system_message}] + \
                history + \
                [{"role": "user", "content": message}]
    
    stream  = ollama.chat(
        model = OLLAMA_MODEL,
        messages = messages,
        stream = True,
    )

    response = ""

    for chunk in stream:
        response += chunk["message"]["content"] or ""
        yield response

with gr.Blocks(theme='shivi/calm_seafoam') as demo:
    
    gr.Markdown("<center><h1>AI Shopping Assistant</h2></center>")
    chatbot = gr.Chatbot(placeholder="<strong>Your Personal Shopping Assistant</strong>")
    gr.ChatInterface(fn=chat, type="messages", chatbot=chatbot)
   
    



# demo = gr.ChatInterface(
#     chat,
#     textbox=gr.Textbox(container=False,
#                        scale=7,
#                        title="Shopping Assistant")
# )
demo.launch(share=True)