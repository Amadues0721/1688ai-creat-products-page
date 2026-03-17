import json
from openai import OpenAI

# 初始化 DeepSeek 客户端
client = OpenAI(
    api_key="sk-b7989723de754cec98cac4fbe8ba5303",
    base_url="https://api.deepseek.com"
)


def clean_json(text: str) -> str:
    """
    清理 DeepSeek 返回的 ```json 包裹
    """
    text = text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return text


def generate_product_info(keyword: str):
    """
    根据关键词生成商品信息
    """
    prompt = f"""
你是一个电商运营专家，请根据以下商品生成高质量商品信息：

商品：{keyword}

要求：
1. 生成一个吸引人的商品标题
2. 生成5个核心卖点（列表形式）
3. 生成详细商品描述（适合1688）
4. 给出合理建议价格（人民币）

必须返回JSON格式，不要加任何解释，也不要使用```！
格式如下：
{{
  "title": "",
  "selling_points": [],
  "description": "",
  "price": ""
}}
"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你必须只返回JSON，不能使用```"},
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content

        # ✅ 清理 JSON
        content = clean_json(content)

        try:
            return json.loads(content)
        except Exception as e:
            print("第一次解析失败，尝试修复...", e)

            # 🔥 二次清理（保险）
            content = content.replace("```json", "").replace("```", "").strip()

            try:
                return json.loads(content)
            except Exception as e:
                print("最终解析失败：", e)
                print(content)
                return None

    except Exception as e:
        print("API调用失败：", e)
        return None