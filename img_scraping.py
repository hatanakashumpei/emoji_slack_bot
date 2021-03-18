import requests
import urllib.request
import time
import json

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
    img_num_per_page = 20 #ここを変えるとダウンロード数が変わります。
    page_list = [f'{url}{i*img_num_per_page+1}' for i in range(max_page_num)]
    return page_list

def download_img(src, dist_path):
    time.sleep(1)
    try:
        with urllib.request.urlopen(src) as data:
            img = data.read()
            with open(dist_path, 'wb') as f:
                f.write(img)
    except:
        pass


def main():
    search_words = ["橋本環奈"] #検索したいワードをリストで渡します。
    for num, search_word in enumerate(search_words):
        url = f"https://search.yahoo.co.jp/image/search?p={search_word}&ei=UTF-8&b="
        max_page_num = 20
        all_img_src_list = scraping(url, max_page_num)

        # 画像ダウンロード
        for i, src in enumerate(all_img_src_list):
            download_img(src, f'./img/image_{num}_{i}.jpg') #保存先は適当に変えてください


if __name__ == '__main__':
    main()
