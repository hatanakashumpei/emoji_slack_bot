import matplotlib
import os

team_name = os.environ['team_name']
bot_name = os.environ['bot_name']

API_TOKEN = os.environ['API_TOKEN']
cookie = 'b=.8enqe1b21xghb8kmfpsv3ifa; G_ENABLED_IDPS=google; ssb_instance_id=535ff740-b48c-5fbc-8830-a6287a80cd22; shown_ssb_redirect_page=1; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1; G_AUTHUSER_H=2; x=8enqe1b21xghb8kmfpsv3ifa.1616874403; d=aOnsslp5OBvbRJk2PV069evyqpWxgekEax0Ja%2BXNOuVSPVcFpzludeCt4IM1dbfm4RmiRS2ny0LL%2FPSbVQZJpxp81urRtZspZigD1sl4cRT9OYES9L5Kdq3DDYsozBOYLBz7SiUnUlTzwOfxcWl5%2Bx21hMgL38IMj2WNL%2FGRSky238LGN1ZXyF9itA%3D%3D; d-s=1616874424; lc=1616874424; OptanonAlertBoxClosed=2021-03-27T19:49:43.635Z; OptanonConsent=isIABGlobal=false&datestamp=Sun+Mar+28+2021+04%3A49%3A44+GMT%2B0900+(Japan+Standard+Time)&version=6.12.0&hosts=&consentId=44be9a0d-0662-4d9d-8748-4d7d2acd4274&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false'

fonts = {
        "mono":"notosans-mono-bold", 
        "m+1p":"mplus-1p-black", 
        "round":"rounded-x-mplus-1p-black", 
        "mincho":"ipamjm", 
        "aoyagi":"aoyagireisyoshimo", 
        "LinLiber":"LinLibertine_RBah"
}

colors = matplotlib.colors.cnames

default_style = {
    'color': '000000FF',
    'back_color': '00000000',
    'size_fixed': 'false',
    'disable_stretch': 'false',
    'align': 'center',
    'font': fonts['mono'],
    'format': 'png'
}

PLUGINS = [
    'emoji_bot.plugins',
]

DEFAULT_REPLY = "スタンプ作るよ:pig_nose:\n\n"+\
                " 使い方 その:one:：テキストからスタンプ\n"+\
                "- 基本コマンドは `add <テキスト> <スタンプの名前> [オプション]`\n"+\
                "- `<テキスト>`に改行を入れたい場合は `_` を入れてね!\n"+\
                "- オプションの指定は以下の3つ!\n"+\
                "   ・ `-c <text_color>` : 文字色の設定\n"+\
                "   ・ `-b <back_color>` : 背景色の設定\n"+\
                "   ・ `-f <font>` : フォントの設定\n\n"+\
                "\n"+\
                " 使い方 その:two:：画像からスタンプ\n"+\
                "- 基本コマンドは `add_img <画像検索する名前> <スタンプの名前> `\n"+\
                "- Yahoo画像検索結果から上位3枚を登録するよ!\n"+\
                "\n"+\
                " 使用例:\n" +\
                " `add それな sorena -c mediumvioletred` >> :sorena: `:sorena:`\n"+\
                " `add_img ぷーさん pooh` >> :pooh_0: `:pooh_0:`\n"+\
                "\n"+\
                " 補足:\n" +\
                "- 色の種類は `colors` で確認!\n"+\
                "- フォントの種類は `fonts` で確認!\n"+\
                "- `<スタンプの名前>` は英数字(小文字)、ハイフン、アンダーバーで書くこと！\n"
