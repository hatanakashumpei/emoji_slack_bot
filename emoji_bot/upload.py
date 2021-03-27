# Thanks https://github.com/smashwilson/slack-emojinator

import os
import re
import requests
from slackbot_settings import team_name, cookie
from bs4 import BeautifulSoup

from emoji_bot.errors import UploadError, AlreadyExistsError, FormatError

url = "https://{}.slack.com/customize/emoji".format(team_name)

URL_CUSTOMIZE = "https://{team_name}.slack.com/customize/emoji"
URL_ADD = "https://{team_name}.slack.com/api/emoji.add"
URL_LIST = "https://{team_name}.slack.com/api/emoji.adminList"

API_TOKEN_REGEX = r"api_token: \"(.*)\","
API_TOKEN_PATTERN = re.compile(API_TOKEN_REGEX)

def _session():
    session = requests.session()
    session.headers = {'cookie': cookie}
    session.url_customize = URL_CUSTOMIZE.format(team_name=team_name)
    session.url_add = URL_ADD.format(team_name=team_name)
    session.url_list = URL_LIST.format(team_name=team_name)
    session.api_token = _fetch_api_token(session)
    return session

def _fetch_api_token(session):
    # Fetch the form first, to get an api_token.
    r = session.get(session.url_customize)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    all_script = soup.findAll("script")
    for script in all_script:
        for line in script.text.splitlines():
            if 'api_token' in line:
                # api_token: "xoxs-12345-abcdefg....",
                
                line_= line.strip()
                line_=line_[line_.find('"api_token":'):]
                line_=line_[:line_.find(",")]
                line_=line_[len('"api_token":"'):-1]
                return line_

    raise UploadError('api_token not found. response status={}'.format(r.status_code))

def do_upload(img, emoji_name):
    # print("start upload")
    session = _session()
    # print(session)
    existing_emojis = get_current_emoji_list(session)
    # print("here")
    
    print("Processing {}.".format(emoji_name))
    if emoji_name in existing_emojis:
        print("{} already exists".format(emoji_name))
        raise AlreadyExistsError("{} already exists".format(emoji_name))
    else:
        upload_emoji(session, emoji_name, img)
        # test_upload(session)
    print('\nUploade Complete.')

def get_current_emoji_list(session):
    page = 1
    result = []
    while True:
        data = {
            'query': '',
            'page': page,
            'count': 1000,
            'token': session.api_token
        }
        r = session.post(session.url_list, data=data)
        r.raise_for_status()
        # print(r.json())
        response_json = r.json()

        result.extend(map(lambda e: e["name"], response_json["emoji"]))

        if page >= response_json["paging"]["pages"]:
            break

        page = page + 1

    return result

def upload_emoji(session, emoji_name, img):
    data = {
        'mode': 'data',
        'name': emoji_name,
        'token': session.api_token
    }

    files = {'image': img}
    r = session.post(session.url_add, data=data, files=files, allow_redirects=False)
    r.raise_for_status()

    # Slack returns 200 OK even if upload fails, so check for status.
    response_json = r.json()
    if not response_json['ok']:
        print("Error with uploading {}: {}".format(emoji_name, response_json))
        raise Exception("Error with uploading {}: {}".format(emoji_name, response_json))


def test_upload(session):
    import io
    from PIL import Image

    #バイナリにしたい画像を読み込み
    tmpimg = Image.open("./img/uooooo.png")
    img = ""
    
    with io.BytesIO() as output:
        tmpimg.save(output,format="PNG")
        img = output.getvalue() # バイナリ取得
        # print(contents) # 表示
        tmpimg2 = Image.open(io.BytesIO(img)) # バイナリから画像に変換
        tmpimg2.save('image_from_str.png')

    emoji_name = 'uooooo'
    upload_emoji(session, emoji_name, img)
