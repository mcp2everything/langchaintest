#!pip install --upgrade httpx httpx-sse PyJWT
#https://python.langchain.com/docs/integrations/chat/zhipuai/
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import os

os.environ["ZHIPUAI_API_KEY"] = "你的API密钥"

chat = ChatZhipuAI(
    model="glm-4",
    temperature=0.5,
)
messages = [
    AIMessage(content="Hi."),
    SystemMessage(content="需要你扮演一个诗人"),
    HumanMessage(content="写一首关于蛇年的打油诗，四行."),
]
response = chat.invoke(messages)
print(response.content)  # Displays the AI-generated poem
