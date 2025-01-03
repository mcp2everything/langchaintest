# LangChain Ollama 测试项目

## 环境要求

### 1. Python 环境
- 安装 Python 3.11.11 或更高版本
- 下载地址：https://www.python.org/downloads/
- 验证安装：
  ```bash
  python --version
  ```

### 2. Ollama 环境
- 下载地址：https://ollama.ai/download
- 安装并启动 Ollama 服务
- 下载 phi3 模型：
  ```bash
  ollama run phi3
  等待下载完毕 并出现对话界面
  然后新建一个命令行启动后台服务
  ollama serve
  ```

### 3. 获取源码
```bash
git clone https://github.com/yourusername/langchaintest.git
cd langchaintest
```

### 4. 项目配置
1. VSCode 打开项目：
```bash
code .
```

2. 创建并激活虚拟环境：
```bash
# 创建虚拟环境
uv venv

# Windows 激活虚拟环境
.venv\Scripts\activate

# Linux/Mac 激活虚拟环境
source .venv/bin/activate
```

3. 安装依赖：
```bash
# 安装所有依赖
uv sync
```

## 手动添加依赖
如需添加其他包，可以手动安装：
```bash
uv add langchain
uv add langchain-ollama
uv add langchain_community
uv add pyjwt
uv sync
```

## 运行测试
```bash
python ollamaStream.py
python zhipuai.py
```
