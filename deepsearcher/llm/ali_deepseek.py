import os
import requests
from typing import Dict, List
from deepsearcher.llm.base import BaseLLM, ChatResponse


class Ali_Deepseek(BaseLLM):
    """
    使用阿里云 DeepSeek API 实现的自定义 LLM
    """
    def __init__(self, model: str = "deepseek-v3", **kwargs):
        # 从 kwargs 或环境变量中获取 api_key 与 base_url
        self.model = model
        self.api_key = kwargs.pop("api_key", os.getenv("ALI_DEEPSEEK_API_KEY"))
        self.base_url = kwargs.pop("base_url", "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions")
    
    def chat(self, messages: List[Dict]) -> ChatResponse:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
        }
        response = requests.post(self.base_url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        # 按照返回结果结构解析内容与 token 数
        content = data["choices"][0]["message"]["content"]
        total_tokens = data.get("usage", {}).get("total_tokens", None)
        return ChatResponse(content=content, total_tokens=total_tokens)