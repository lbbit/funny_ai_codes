import os

import openai
from openai import OpenAI

openai.api_key = "sk-xxx"

client = OpenAI(api_key=openai.api_key)

def semantic_sort(chapters):
  prompt = f"给定以下小说章节标题列表:\n{chapters}\n请按照合适的顺序对其进行排序,用换行分隔,不要输出额外信息:\n"

  try:
    response = client.completions.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        stream=False,
        n=1,
        stop=None,
        temperature=0.5,
    )
  except Exception as e:
    print(f"OpenAI API call failed: {e}") 
    return None

  sorted_chapters = response.choices[0].text.strip().split('\n')

  return sorted_chapters

chapters = ["第一章 启程","第三章 冲突","第四章 和解","第二章 邂逅"]

print(semantic_sort(chapters))