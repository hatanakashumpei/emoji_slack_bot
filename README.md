# Slack emojibot
自動的に絵文字を作成する絵文字ぼっとです。
仕様としては
- テキストを絵文字化。
- yahoo画像検索の上位3件をそのままスタンプ化にする。

# セットアップ

```
git clone https://github.com/toshi17/emojibot.git
cd emojibot
pip install -r requirements.txt
```

以下の操作を終えたら、以下に示す*Cookieの設定*を行なってください。

- https://{teamname}.slack.com/customize/emojiを開く
- 開発者ツールを起動し、ネットワークタブを開く
- ページをリロードし、"name"が"emoji"の項目を開く
- 新たに開いたタブから"Headers"を選ぶ
- "Request-Headers"までスクロールし、"Cookie"の値をコピーし，slackbot_settings.pyに追加する

# 起動の前に
上記のセットアップを終えたら
WSのAppを追加でHubotを追加し、そのtokenをslackbot_settings.pyに追加する。
同様にWS名(teamname)もslackbot_settings.pyに追加する。

# 起動
slackbot_settings.pyの変数を修正したら
```
python run.py
```
で動きます。

# docker

dockerが入っている場合には上記のセットアップをしなくとも

```
docker build -t <img_name>
docker run -it --rm <img_name>
```
で動きます。


