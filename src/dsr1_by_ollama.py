#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""deepseek-r1:Xxb by ollama

------------------------------------------------


------------------------------------------------
Filename	: dsr1_by_ollama.py
Author		: gesong (gesong.nj@outlook.com)
Createtime	: 2025-03-04  08-41-44
------------------------------------------------
"""


import os
import time

import ollama

# 列出可用模型
client = ollama.Client(host="http://localhost:11434")
models = client.list()
print("Available models:")
mlist = [m.get("model") for m in models.models]
print(mlist, "\n")


def askme(who=mlist[0]) -> None:
    """try"""

    # 选择模型
    role = input(f"Choice modle, Or the Default '{who}':")
    if role != "":
        who = role
    print(f"Now, {who} is here!")
    # 记录开始时间
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 进入连续问答
    while True:
        try:
            print("""please input your quest, or just input 'end' to exit:""")
            # 获取输入
            quest = input()
            if quest == "end":
                break
            # 推理并回答(计时)
            _stime = time.time()
            response = client.generate(
                model=who,
                prompt=quest,
            )
            _spend = round(time.time() - _stime)
            # 输出答案
            output = response["response"]
            print("=" * 20, output, "+" * 20, sep="\n")
            # 生成文件名和路径,并记录
            file = os.path.join(os.getcwd(), "anser", "anser" + now + ".MD")
            with open(file, "a") as f:
                f.write("+" * 60)
                f.write("  \n")
                f.write(f"Quest:{quest} \nTime:{_spend} S")
                f.write("  \n")
                f.write("-" * 60)
                f.write("  \n")
                f.write(output)
                f.write("  \n")
                f.write("-" * 60)
                f.write("  \n")
        except Exception as err:
            print(f"BUG:{err}")


if __name__ == "__main__":
    askme()
