import os
from os import system
from io import BytesIO
import base64
import requests
import json
from PIL import Image
js = 0
system('title flux绘图工具_By青松awa')
print('欢迎使用 flux绘图工具 & By 青松awa')
with open('setting.qs', 'r', encoding='utf-8') as file:
    content = file.read()
custom_path = content
while True:
    js = js + 1
    if content == '':
        path = input('第一次使用，请输入图片保存路径（注意：请使用绝对路径，保证路径一定存在，且末尾一定要有反斜杠!!!）：')
        with open('setting.qs', 'w', encoding='utf-8') as file1:
            file1.write(path)
        custom_path = content
        print('设置成功。如需要重新设置，请删除软件安装目录下的 setting.qs 文件后运行。')
    prompt = input('请输入图片生成提示词（不懂请自行百度）：')
    print('正在生成图片，请稍后...')
    url = "https://flux.qsawa.us.kg/api/image"
    headers = {
    "Authorization": "Bearer -yQc-JUM0pEVp0riqhod9KvW_s5rvhzTWl8delri",
    "Content-Type": "application/json"
    }
    data = {
    "messages": [{"role": "user", "content": prompt}],
    "model": "FLUX.1-Schnell-CF"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()
    base64_image_data = result['image']
    decoded_data = base64.b64decode(base64_image_data)
    img = Image.open(BytesIO(decoded_data))
    wjm = 'paint' + str(js) + '.png'
    c = custom_path + wjm
    img.save(c)
    print('绘画完成~请欣赏成品...')
    commend = 'start '+c
    os.system(commend)
    system('pause')
    system('')
    cho = input('当前任务执行成功！图片已保存到软件安装目录paint[num].png。输入e退出，输入o继续创作...\n')
    if cho == 'e':
        break
