import matplotlib

team_name = 'hatanakatestworkspace'
bot_name = 'custom-stamp-bot'

API_TOKEN = 'xoxb-1906935386592-1876356173590-yyQhvDf7d0HukaWK8wWpdWNF'
cookie = 'b=.8enqe1b21xghb8kmfpsv3ifa; G_ENABLED_IDPS=google; ssb_instance_id=535ff740-b48c-5fbc-8830-a6287a80cd22; shown_ssb_redirect_page=1; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1; G_AUTHUSER_H=2; d=W8K0vrlYdG6y2Ijn7z5g0XZKonX6XArW4DytkQBR1YS44O0%2FESDsmH%2FwR5pV8WV4dqBxbobC5wG92fK9EenOkDjP1vBnzVH%2BERU73300xMM%2Fy24riFVXPW6XqNKAnntk%2FuZrZUzayzSPGT2PWLE%2F%2FKG2Q%2Fpe%2BXS6A6Q%2B0aaxizfRJsGx2fA73JoxEw%3D%3D; d-s=1616870034; lc=1616870034; x=8enqe1b21xghb8kmfpsv3ifa.1616870034; utm=%7B%22utm_source%22%3A%22in-prod%22%2C%22utm_medium%22%3A%22inprod-link_app_settings-user_%22%7D; OptanonConsent=isIABGlobal=false&datestamp=Sun+Mar+28+2021+03%3A33%3A58+GMT%2B0900+(Japan+Standard+Time)&version=6.12.0&hosts=&consentId=2c1805d2-eed6-4ac3-9b16-b0b624b9742d&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false&geolocation=JP%3B14; OptanonAlertBoxClosed=2021-03-27T18:33:58.450Z'

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

DEFAULT_REPLY = "<@U01RSAG53HC>\nスタンプ作るよ:pig_nose:\n\n"+\
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
