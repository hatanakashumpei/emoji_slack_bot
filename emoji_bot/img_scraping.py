import requests
import urllib.request
import time
import json

from PIL import Image, ImageDraw, ImageFilter

import io
from io import BytesIO

def scraping(url, max_page_num):
    # ページネーション実装
    page_list = get_page_list(url, max_page_num)
    # 画像URLリスト取得
    all_img_src_list = []
    for page in page_list:
        try:
            img_src_list = get_img_src_list(page)
            all_img_src_list.extend(img_src_list)
        except:pass
    return all_img_src_list


def get_img_src_list(url):
    # 検索結果ページにアクセス
    response = requests.get(url)
    webtext = response.text

    # 元の記事ではBeatifulsoupを使っていたのですが、画像が取れなかったので、変更しています。
    start_word='<script>__NEXT_DATA__ = '
    start_num = webtext.find(start_word)
    webtext_start = webtext[start_num + len(start_word):]
    end_word = ';__NEXT_LOADED_PAGES__='

    end_num = webtext_start.find(end_word)
    webtext_all = webtext_start[:end_num]
    web_dic = json.loads(webtext_all)
    img_src_list = [img['original']['url'] for img in web_dic["props"]["initialProps"]["pageProps"]["algos"]]

    return img_src_list


def get_page_list(url, max_page_num):
    img_num_per_page = 1 #ここを変えるとダウンロード数が変わります。
    page_list = [f'{url}{i*img_num_per_page+1}' for i in range(max_page_num)]
    return page_list


def edit_img(src):
    """画像を整形してbyte型返す
    """
    time.sleep(1)
    try:
        img_read = urllib.request.urlopen(src).read() # 画像を取得
        img_bin = io.BytesIO(img_read) # メモリに保持してディレクトリ偽装見たくする
        pil_img = Image.open(img_bin) # PILで読み込む
        pil_img = crop_max_square(pil_img)
        img = io.BytesIO() # 空のインスタンス生成
        pil_img.save(img, "JPEG") # 空のインスタンスに保持する
        deit_img = img.getvalue() # バイナリデータを取得する (open().read()状態)

        return deit_img

    except:
        return 0

"""
def img2byte(path):
    # 保存した画像をバイナリ化する
    
    try:
        # バイナリにしたい画像を読み込み
        tmpimg = Image.open(path)
        img = ''

        with io.BytesIO() as output:
            tmpimg.save(output, format = "PNG")
            img = output.getvalue() # get byte
            # print(img)
        
        return img

    except:
        return 0



def download_img(src, dist_path):
    # 画像を正方形に切り取って保存する
    
    time.sleep(1)
    try:
        with urllib.request.urlopen(src) as data:
            img_byte = data.read()
            img = Image.open(BytesIO(img_byte))
            img = crop_max_square(img)
            print(type(img))
            print(f'saving img : {dist_path}')
            img.save(dist_path) # 保存
            # print(type(img))
            img.close()
    except:
        pass
    
"""


def expand2square(pil_img, background_color):
    """余白を追加して正方形にする
    """
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

def crop_center(pil_img, crop_width, crop_height):
    """正方形を切り出す
    """
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    """最大サイズの正方形を切り出す関数を定義
    """
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def img_scraping_main(search_words):
    """
    スクレイピングした画像を整形した上でバイナリデータと名前のタプルの配列を返す
    """
    output = []

    for num, search_word in enumerate(search_words):
        url = f"https://search.yahoo.co.jp/image/search?p={search_word[0]}&ei=UTF-8&b="
        max_page_num = 1
        all_img_src_list = scraping(url, max_page_num)
        # print(len(all_img_src_list))

        # 画像ダウンロード
        for i, src in enumerate(all_img_src_list):

            if i < 3:    
                # print(src)
                # download image
                # path = f'./img/{search_word[1]}_{i}.jpg'
                # download_img(src, path)
                img_byte = edit_img(src)

                # print(src,img_byte)

                # img_byte = img2byte(path)
                img_name = f'{search_word[1]}_{i}'

                if img_byte != 0:
                    output.append((img_byte, img_name))
                else:
                    continue
    
    return output



if __name__ == '__main__':
    # 検索したいワードとファイル名のタプルをリストで渡します。
    search_words = [("TUYU","tuyu"),("ずっと真夜中でいいのに。","ZTMY")]
    print(img_scraping_main(search_words))

