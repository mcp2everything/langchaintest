from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import sys

def main():
    try:
        print("初始化 Ollama connection...")
        
        # Initialize model with optimized parameters
        model = OllamaLLM(
            model="phi3:latest",
            temperature=0.7,
            num_ctx=512,  # 减小上下文窗口
            num_thread=4,  # 增加线程数
            stream=True,   # 启用流式输出
            timeout=10,    # 设置超时
            base_url="http://localhost:11434",
        )

        # Simplified prompt template
        template = "问题: {question}\n回答:"
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model

        # Stream the response
        print("\n发送问题 to model...")
        for chunk in model.stream("用中文告诉我什么是LangChain?"):
            print(chunk, end="", flush=True)
        print("\n")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()