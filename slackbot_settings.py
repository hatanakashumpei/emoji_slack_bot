import matplotlib

team_name = '100-un79027'
bot_name = 'custom-stamp-bot2'

API_TOKEN = 'xoxb-1346011685073-1882399324355-WOBRCrKXqRXsjWxJmKXmWdRC'
cookie = 'x=6jg4zm8buglzp5x8ftorlnpo8.1616261308; d=zjDgjLDEbqvwAS8npY+BrxI8Uws/gjqfu1wm93AcLyTUFe3+EDlWybBJ1aETtMm9OB+LqUpqAcO7IVKPPGMv69jyuLGGrjQUdCQ4KtsSbeF7KmtTnshlJTtF/sVh0Y+T7vp1L5hRVrBfyvaBkyBaZjLk26iluS39zYDkNMra2V/JEM7Fpb2HT0AFIg==; d-s=1616261332; lc=1616261332; b=.6jg4zm8buglzp5x8ftorlnpo8; OptanonAlertBoxClosed=2021-03-20T17:45:51.511Z; OptanonConsent=isIABGlobal=false&datestamp=Sun+Mar+21+2021+02:45:52+GMT+0900+(Japan+Standard+Time)&version=6.12.0&hosts=&consentId=b512173b-8fb5-4c4d-8d5a-f281a15cf2f6&interactionCount=1&landingPath=NotLandingPage&groups=C0004:1,C0002:1,C0003:1,C0001:1&AwaitingReconsent=false&geolocation=JP;14'

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

DEFAULT_REPLY = "<@U01RYBR9JAF>\nスタンプ作るよ:pig_nose:\n\n"+\
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
