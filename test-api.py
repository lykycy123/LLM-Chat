from openai import OpenAI
import time

client = OpenAI(api_key="sk-3077c1c0c76e4cdbb3a31d55a34134cf", base_url="https://api.deepseek.com")

# 记录开始时间
start_time = time.time()

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

# 记录结束时间
end_time = time.time()

# 计算并打印API调用所花费的时间
api_call_time = end_time - start_time
print(f"API调用花费的时间: {api_call_time} 秒")

print(response.choices[0].message.content)