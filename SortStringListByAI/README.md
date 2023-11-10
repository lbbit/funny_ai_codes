# SortStringListByAI

本项目演示如何使用OpenAI的GPT-3.5-turbo语言模型以语义方式对字符串列表进行排序。提供的代码使用OpenAI API执行排序操作。

## 安装

要运行本项目中的代码，您需要安装以下依赖项：

- Python 3.7或更高版本
- OpenAI Python库（`openai`）

您可以使用pip安装所需的依赖项：

```
pip install openai
```

## 使用方法

1. 获取OpenAI API密钥

   在运行代码之前，您需要从OpenAI获取一个API密钥。访问[OpenAI网站](https://www.openai.com)创建帐户并生成API密钥。

2. 设置API密钥

   将代码中`api_key`变量中的占位符值`"sk-xxx"`替换为您实际的OpenAI API密钥。

3. 运行代码

   执行包含提供的代码的Python脚本。它将以语义方式对给定的章节列表进行排序。

   ```python
   python main.py
   ```

   排序后的章节将作为输出显示。

## 功能

本项目的主要功能在`semantic_sort`函数中实现。它接受一个章节标题的列表作为输入，并使用GPT-3.5-turbo语言模型对它们进行有意义的排序。该函数将排序后的章节作为列表返回。

`semantic_sort`函数使用OpenAI API进行完成请求，其中包含章节标题的提示。API的响应包含排序后的章节，然后提取并返回这些章节。

## 限制

- 本项目提供的代码假定您拥有有效的OpenAI API密钥并具有访问GPT-3.5-turbo模型的必要权限。
- `semantic_sort`函数使用OpenAI API的默认设置。您可以根据需要修改参数，如`model`、`max_tokens`和`temperature`，以自定义排序行为。
- 代码不处理在API请求期间可能发生的异常或错误。建议添加适当的错误处理和异常管理，使代码更加健壮。
