from flask import Flask
from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession
from urllib.parse import unquote

app = Flask(__name__)
model = ChatModel("chat-bison")

@app.route('/prompt/<path:prompt>')
def get_ai_response(prompt):
    prompt = unquote(prompt)  # URL-decode the prompt
    response = model.chat([
      ChatSession(
        context="You are a normal AI bot",
        examples=[
          ChatExample(
            input=ChatMessage(content="1 + 1"),
            output=ChatMessage(content="2")
          )
        ],
        messages=[
          ChatMessage(author="USER", content=prompt),
        ],
      )
    ], temperature=0.2)

    return response.responses[0].candidates[0].message.content

if __name__ == '__main__':
    app.run(host='0.0.0.0')
