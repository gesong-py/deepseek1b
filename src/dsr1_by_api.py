#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""try deepseek-r1 by api

------------------------------------------------
my api-key:{"GESONG_bifrim_cn_20250310":"sk-0465b95032ed4e4dbad867b2c1aae67c"}

------------------------------------------------
Filename	: dsr1_by_api.py
Author		: gesong (gesong.nj@outlook.com)
Createtime	: 2025-03-10  09-12-30
------------------------------------------------
"""


from openai import OpenAI
import time
import os
import json


class DeepSeekChat:
    def __init__(
        self,
        api_key,
        base_url="https://api.deepseek.com/v1",
        model="deepseek-chat",
    ):
        self.client = OpenAI(
            api_key=api_key, base_url=base_url  # 设置 DeepSeek 的 API 端点
        )
        self.model = model
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_response(self, temperature=0.7, max_tokens=2048):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"API 请求失败: {str(e)}"


if __name__ == "__main__":
    # 配置参数
    API_KEY = "sk-0465b95032ed4e4dbad867b2c1aae67c"  # 替换为实际 API 密钥
    BASE_URL = "https://api.deepseek.com/v1"  # 确认实际 API 地址
    INITXT = """你是一个文本处理助手，以JSON形式输出。
            输出的JSON遵守以下格式：
            \n {\n  "question": <用户提问信息>,
            \n  "time": <当前时间，格式为 YYYY-mm-dd HH:MM:SS>,
            \n  "answer": <新闻内容总结>\n}"""

    # 启动并初始化
    chat = DeepSeekChat(api_key=API_KEY, base_url=BASE_URL)
    chat.add_message("assistant", INITXT)
    print("DeepSeek 对话助手（输入 exit 退出）")

    # 进入流输入
    while True:
        user_input = input("\n用户输入: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # 添加用户消息
        chat.add_message("user", user_input)

        # 获取回复
        response = chat.get_response()
        print(f"\nDeepSeek回答: {response}")

        # 添加助手回复到历史
        chat.add_message("assistant", response)

    # 记录答案到文件
    try:
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        file = os.path.join(os.getcwd(), "anser", "anser" + now + ".json")
        with open(file, "a", encoding="utf-8") as f:
            f.write(json.dumps(chat.history, ensure_ascii=False))
    except Exception as err:
        print(f"BUG:{err}")
