#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""deepseek-r1:1.5b by ollama

------------------------------------------------


------------------------------------------------
Filename	: dsr1_1b_ollama.py
Author		: gesong (gesong.nj@outlook.com)
Createtime	: 2025-03-03  13-47-44
------------------------------------------------
"""


import os
import time

import ollama

client = ollama.Client(host="http://localhost:11434")
models = client.list()
# print("Available models:", models)


def askme() -> None:
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())

    while True:
        print("please input your quest, or just input 'end' to exit:")
        quest = input()
        if quest == "end":
            break
        response = client.generate(model="deepseek-r1:1.5b", prompt=quest)

        output = response["response"]
        print("=" * 20, output, "#" * 20, sep="\n")

        # 生成文件名和路径,并记录
        filepath = os.path.join(os.getcwd(), "anser", "anser" + now + ".MD")
        with open(filepath, "a") as f:
            f.write("=" * 80)
            f.write("\n\n")
            f.write(quest)
            f.write("\n\n")
            f.write("-" * 80)
            f.write("\n\n")
            f.write(output)
            f.write("\n\n")
            f.write("-" * 80)
            f.write("\n\n")


if __name__ == "__main__":
    askme()
