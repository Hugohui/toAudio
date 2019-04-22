# 导入codecs模块，方便转换编码
import codecs
from aip import AipSpeech

# 获取文件文本
def get_txt():
    txt = ''
    with codecs.open('../input/1.txt', 'r', 'gbk') as f:
        txt += f.read()
    f.close()
    return txt

# 调用api文字转语音
def to_audio(txt):
    """ 你的 APPID AK SK """
    APP_ID = '16073617'
    API_KEY = '4GdT7gPHbHu6WtEN58yMX5T4'
    SECRET_KEY = 'FxryTPqkcjb8BpI0OxmlOI1k6TC6U7vx'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(txt, 'zh', 1, {
        'vol': 5, 'per': 4
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('../output/auido.mp3', 'wb') as f:
            f.write(result)

txt = get_txt()
to_audio(txt)