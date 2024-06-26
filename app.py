import chainlit as cl
from src.llm import ask_order, messages
import json

@cl.on_message
async def main(message: cl.Message):
    user_msg = {"role":"user","content":message.content}
    messages.append(user_msg)
    response = ask_order(messages)
    assitant_msg = {"role":"user","content":response}
    messages.append(assitant_msg)

    json_res = json.dumps(response)

    await cl.Message(
        content = response
    ).send()