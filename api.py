from random import random
from math import floor
from urllib import parse
from Crypto.Cipher import AES
import base64
import requests

# encodeURIComponent 等价于python的 urllib.parse.quote_plus
# unescape 等价于 urllib.parse.unquote
# 定义填充
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

# 定义headers
headers = {}
headers['Accept'] = '*/*'
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
headers['Connection'] = 'keep-alive'
headers['Content-Length'] = '476'
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Cookie'] = 'mail_psc_fingerprint=4dc0a6bec766f59a4210418296cbfb6c; _iuqxldmzr_=32; _ntes_nnid=75ed65570d4b76058675c00f8d08f844,1513832098682; _ntes_nuid=75ed65570d4b76058675c00f8d08f844; __utmz=94650624.1524319641.4.3.utmcsr=jskyzero.github.io|utmccn=(referral)|utmcmd=referral|utmcct=/2017/07/03/2-2_start/; usertrack=ezq0plr6d+19dvP4CpBlAg==; _ga=GA1.2.1710089623.1526364126; nts_mail_user=m15829090995@163.com:-1:1; WM_TID=UH4%2BZQsChNOTEWt3OJtPE4ZnEzpVpD0R; UM_distinctid=165a9dfa4db2d6-01d9b6547ab461-37664109-1fa400-165a9dfa4dc139; vinfo_n_f_l_n3=3f84dff8a623744c.1.0.1536153332210.0.1536153334555; __f_=1536757435087; hb_MA-BFF5-63705950A31C_source=www.baidu.com; P_INFO=15829090995|1536770594|0|study|00&99|null&null&null#gud&null#10#0#0|&0|null|15829090995; hb_MA-BFF5-63705950A31C_u=%7B%22utm_source%22%3A%20%22baidu%22%2C%22utm_medium%22%3A%20%22cpc%22%2C%22utm_campaign%22%3A%20%22affiliate%22%2C%22utm_content%22%3A%20%22SEM%22%2C%22utm_term%22%3A%20%22Brand_xsl%22%2C%22promotional_id%22%3A%20%22%22%7D; __remember_me=true; __utmc=94650624; __utma=94650624.806193322.1514903642.1538712447.1538719305.9; WM_NI=xZ7oER%2BXVUA6cfJAxF4ugUSFJ4ZT5QUa6ywaS9Eyjl7yVUAW6cWTf3wc7EZ7nehXvEBug5z1RASegXTSLHLTbgcLeMbOqxyeOBQ2kOkHbsG%2BUTTIGDc0ZVn3MjXe3mthRWI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee95d34e8babfcbaed41f48e8aa6d44f869b9ababc6f818bad90ef42b4a8fb96e22af0fea7c3b92abc86f990c85ae9889ab6c43ea1ba86a2fb4ef8aba9b6d24e8aec96b5b85b97bffa9af66b91e78b9ae968f5a79ab6c45df6bd99b5e539b5bdf9a6d93daebba8b9f54f82aba9d6f93b929f9d86e654988d84a9cf60a2b9adade847a291bf99fc6f8d9e9fd3ea45a998ae94c621978c9caac650a1f096b7ed398fb69886b267b8b89eb8cc37e2a3; MUSIC_U=c01dded3bdf059751f2d7065a3390c2c5053be85f4706fa6450033491a465c12e6405531f7f9d22e784650ce389e5d7f55bd365cb526c948305842396b5dfc01; __csrf=b9155c11b49c39eb97145536f9cdc1cd; playerid=20223119; JSESSIONID-WYYY=NlZS3ZIAv2xO7qHPGFHeTPtoY%2BHQ6c6%5COxU%5CAeygdBKEIZpeptDdGFduWkb5vVIsh38dYddA%2FlXMErARsagUtPNEUGsntcVDG8gIiQs6%2BEqe9jxaUyBfHuqkyllzkcoZZMFHSITs%2BVEEg0YrGVgFAhUk28H%2FmzhD7hB85cZNIQtQygP1%3A1538722845076'
headers['Host'] = 'music.163.com'
headers['Origin'] = 'https://music.163.com'
headers['Referer'] = 'https://music.163.com/'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

def add_to_16(text):
    """用以将明文补足16位"""
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)

def aes_encrypt(text, key, iv):
    # AES加密
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))
    aes_bytes = aes.encrypt(add_to_16(pad(text)))
    enctypted_text = str(base64.encodebytes(aes_bytes), encoding='utf-8').replace('\n', '')
    return enctypted_text

def b(p1, p2):
    iv = '0102030405060708'
    return aes_encrypt(p1, p2, iv)

def asrsea(a1, b1, c1, d1):
    h = {}
    i = 'XmOUgBvsVQM8WAyR'
    # i对应的RSA加密结果
    encSecKey = "b641f06320529f4505bc91c9d6136e110274964f5ac1ebfff97401da3b7cd20aacb084921acf68e258d0db4c748f21740395b18a58fc9c62913d3f657acc5e65d6f6f3da5bc9a0e9b95f3af0dfc9ec0ec1973fe42f612db02de0d220dcbf52dd24164625625c7407cd46e52e9e0fd57acc0b08106b84e128abb1787d80eb1d39"
    # 两次AES加密
    encText = b(a1, d1)
    encText = b(encText, i)
    return {'params': encText, 'encSecKey': encSecKey}

def getSongURL(songId):
    song_str = '{"ids":"[%d]","br":128000,"csrf_token":"b9155c11b49c39eb97145536f9cdc1cd"}' % songId
    p2 = '010001'
    p3 = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    p4 = '0CoJUm6Qyw8W8jud'
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token=b9155c11b49c39eb97145536f9cdc1cd'
    form_datas = asrsea(song_str, p2, p3, p4)
    rsp = requests.post(url, headers=headers, data=form_datas)
    return rsp.json()['data'][0]['url']

def downloadMusic(url, filename='default'):
    rsp = requests.get(url)
    with open('media/%s.mp3' % filename, 'wb') as f:
        f.write(rsp.content)