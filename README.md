# 项目简介

本项目参考开源代码https://github.com/ABexit/ASR-LLM-TTS
主要关注实时检测对话、自由打断、多模态-多语种问答、声纹识别、自由定制唤醒词、历史对话记忆、自由定制唤醒词等功能，打造语音对话助手，为后面的大语言模型移动机械臂做模块准备

# 框架
1.CosyVoice 多语言的大型语音生成模型,不仅支持多种语言的语音生成，还提供了从推理到训练再到部署的全栈能力。该模型在语音合成领域具有重要性，因为它能够生成自然流畅、接近真人的语音，适用于多种语言环境。 (https://github.com/FunAudioLLM/CosyVoice)

2.SenseVoice 是多语言音频理解模型，具有包括语音识别、语种识别、语音情感识别，声学事件检测能力。(https://github.com/modelscope/FunASR),
中文识别建议使用"paraformer-zh"模型，原项目使用CosyVoiceSmall作为模型运行识别出来为乱码

3.Qwen2.5作为大语言模型，具备自然语言理解、文本生成、视觉理解、音频理解、工具使用、角色扮演、作为AI Agent进行互动等多种能力。(https://github.com/QwenLM/Qwen2.5)

# 内容速览
## 文件介绍
多角色拟人小说朗读器：16_Inference_QWen2.5_story.py

实时检测对话、自由打断、多模态-多语种问答、声纹识别、自由定制唤醒词、历史对话记忆、自由定制唤醒词
无历史记忆：15.0_SenceVoice_kws_CAM++.py
有历史记忆：15.1_SenceVoice_kws_CAM++.py

pretrained_models是存放各个模型的地方
cosyvoice是项目主要框架
output是输出目录，存储语音识别结果的暂存wav文件
Test_QWen2_VL存储输出的语音文件，sft_tmp_{audio_file_count}.mp3为系统自身语音，sft_{audio_file_count}.mp3为大语言模型回答语音
SpeakerVerification_DIR\enroll_wav存储声纹模型

整体代码流程：语音录制 -> 语音保存 -> 语音识别 -> 文本处理 -> 大语言模型调用 -> 响应处理。

本项目主要关注15版本的各种功能，如关注其他功能，请参考原博主项目

## 15.1版本关键模块介绍
flag_KWS_used 唤醒词是否使用
flag_sv_used 声纹识别是否使用
def extract_chinese_and_convert_to_pinyin(input_string) 将识别转化成拼音有利于提高唤醒词识别率
def Inference(TEMP_AUDIO_FILE=f"{OUTPUT_DIR}/audio_0.wav") 推理部分，里面可以设置自己所需，speaker默认注释掉除中文外的其他语种


# 快速开始
根据框架，下载所需要的模型到pretrained_models中并更改代码中的model_dir
打开ASR-LLM-TTS-MASTER，以此为工作空间，安装所需要的包，`pip install -r requirements.txt`，不需要全部都安装好，遇到报错的先自行注释然后自行安装。然后选择0到16中自己感兴趣的版本，边运行边找出缺失的包进行安装
