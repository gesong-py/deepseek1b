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

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="sk-0465b95032ed4e4dbad867b2c1aae67c",
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": """你是一个文本处理助手，以JSON形式输出。
            输出的JSON遵守以下格式：
            \n {\n  "question": <用户提问信息>,
            \n  "time": <当前时间，格式为 YYYY-mm-dd HH:MM:SS>,
            \n  "answer": <新闻内容总结>\n}""",
        },
        {
            "role": "user",
            "content": "江苏省的海岸侵蚀现状",
        },
    ],
)

print(completion.choices[0].message.content)
