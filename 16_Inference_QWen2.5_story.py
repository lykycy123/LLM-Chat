from transformers import AutoModelForCausalLM, AutoTokenizer

from cosyvoice.cli.cosyvoice import CosyVoice
from cosyvoice.utils.file_utils import load_wav
import torchaudio

import pygame
import time

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)  # 等待音频播放结束
        print("播放完成！")
    except Exception as e:
        print(f"播放失败: {e}")
    finally:
        pygame.mixer.quit()

model_name = r"E:\2_PYTHON\Project\GPT\QWen\Qwen2.5-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

system = r'你是一个小说的角色分类模型，可以根据输入将小说文本内容划分为1-5个角色，其中非角色说话的内容为“解说”，角色仅赋予其说话内容，处理“”内信息。按照顺序设定为角色1、角色2等。输出按照“角色”：“内容”的形式，输出顺本遵循文本输入顺序。输出格式举例：解说：“”， 角色1：“”，解说：“”， 角色2：“”，等等。输入为：'
prompt = r"腥咸的海风拂过战场，五位主神与七位人类天花板，几乎全部丧失战斗力，众多身影在血色的海面上浮沉，除了那披着泥泞袈裟屹立在海面的身影，【门之钥】的身前空无一人。“所以说，你们根本挡不住我。”【门之钥】注视着那张面孔，缓缓开口，“哪怕人类的顶级战力齐聚于此，连拖延我三分钟都没做到……人类，已经没有希望了。”，“是吗？这就是你看到的未来吗？”面对【门之钥】的威压，宿命和尚并没有丝毫退却，平静的回答，“如果人类真的没有希望……你又为什么这么着急的要杀了我们，毁掉安卿鱼的灵魂？你这么着急……是在忌惮谁？”【门之钥】的眉头微微皱起。“人类并非没有希望，你早就看到了，那个有着一线可能的未来……你想将这个未来掐灭在摇篮中，因为越往后拖，你的胜算就越低。”宿命和尚停顿片刻，“而在我说这些话的时候……你的胜算，又低了几成呢？”，“我承认，你很聪明，甚至可以窥探到我的想法……但这改变不了什么。”【门之钥】缓缓开口，“安卿鱼的灵魂，已经快被我彻底磨灭了，至于你……我不会在这里浪费时间杀你，你就在这里亲眼看着，我覆灭人类吧。”，“浪费时间杀我？”宿命和尚嗤笑一声，“你是怕浪费时间……还是不敢杀我？”"
messages = [
    {"role": "system", "content": "你是一个小说的角色分类模型，可以根据输入将小说文本内容划分为1-5个角色，其中非角色说话的内容为“解说”，角色仅赋予其说话内容，处理“”内信息。按照顺序设定为角色1、角色2等。输出按照“角色”：“内容”的形式，输出顺本遵循文本输入顺序。输出格式举例：解说：“”， 角色1：“”，解说：“”， 角色2：“”，等等。"},
    {"role": "user", "content": system+prompt},
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("Input:", prompt)
print("Answer:", response)
