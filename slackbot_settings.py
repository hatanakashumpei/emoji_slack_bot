import matplotlib

team_name = 'hackteam2workspace'
bot_name = 'custom-stamp-bot'

# API_TOKEN = 'xoxb-1852796949319-1869163680933-llmzwcIe3Yw9Q1Gmp5L1nviD'
API_TOKEN = 'xoxb-1852796949319-1861025033815-bzugBljoGKDXMHOtmuEpSnOm'
cookie = 'ssb_instance_id=535ff740-b48c-5fbc-8830-a6287a80cd22; _gcl_au=1.1.162791625.1612331039; _lc2_fpi=e00b11ac9c9b--01exk6pertpskhw7pwayfd8brr; _ga=GA1.2.1702706611.1612331039; b=.7krfakzwpe30ojrgo51e9yh45; shown_ssb_redirect_page=1; __qca=P0-1560665182-1613274121246; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1; d=hCpw%2BhkTibh63f6uVlElK3dzs3Gv2zdl3Zmh6Qi2OJG5XBin9V5srlYMGyiLY7zy5IBptCkJyy7J0zTCYmARAG6hjZ1I3gmaHvSQr8dNCIv%2FBRXbkw6%2BU5Q2phKhrQt5CZJ3qpbIPNhvRuymIIi8h6ysH9vJpmN9iFkwgzm9ntlXnWk5QpVkLAxGbw%3D%3D; d-s=1615965044; lc=1615965044; G_ENABLED_IDPS=google; utm=%7B%22utm_source%22%3A%22in-prod%22%2C%22utm_medium%22%3A%22inprod-link_app_settings-user_%22%7D; x=7krfakzwpe30ojrgo51e9yh45.1616044962; OptanonAlertBoxClosed=2021-03-18T05:25:08.966Z; OptanonConsent=isIABGlobal=false&datestamp=Thu+Mar+18+2021+14%3A25%3A09+GMT%2B0900+(Japan+Standard+Time)&version=6.12.0&hosts=&consentId=fbbc8ea3-fd0f-47b6-a8fb-5c907e2a5cbd&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false&geolocation=JP%3B14'

fonts = {
   'noto' : './assets/fonts/NotoSansMonoCJKjp-Bold.otf',
   'ipag' : './assets/fonts/ipag.ttf',
   'mplus' : './assets/fonts/ipag.ttf',
   'stick-regular' : './assets/fonts/Stick-Regular.ttf',
}

"""
colors = {
    'black': '000000',
 	'silver': 'c0c0c0', 
 	'gray': '808080',	 
 	'white': 'ffffff',	 
 	'maroon': '800000', 
 	'red': 'ff0000',
 	'purple': '800080',
 	'fuchsia': 'ff00ff',
 	'green': '008000',
 	'lime': '00ff00',
 	'olive': '808000',
 	'yellow': 'ffff00',
 	'navy': '000080',
 	'blue': '0000ff',
 	'teal': '008080',
 	'aqua': '00ffff'
}
"""

colors = matplotlib.colors.cnames

default_style = {
    'color': '000000FF',
    'back_color': 'FFFFFFFF',
    'size_fixed': 'false',
    'disable_stretch': 'false',
    'align': 'center',
    'font_path': fonts['noto'],
    'format': 'png'
}

PLUGINS = [
    'emoji_bot.plugins',
]

DEFAULT_REPLY = " :wave: :robot_face: @"+bot_name+"は文字列から絵文字を作成するbotです。 \n\n"+\
            "  _Commands:_  \n" +\
            "  - `@"+bot_name+" add <text> <emoji_name> [option]` -- 文字列を絵文字として登録します。\n" +\
            "       _Options:_\n" +\
            "       - `-c, --color <text_color>` -- 文字色の設定\n" +\
            "       - `-b, --back <back_color>` -- 背景色の設定\n" +\
            "       - `-f, --font <font>` -- フォントの設定\n" +\
            "       ※ 色はRGB値か文字列で指定可能。RGB値で指定する場合は6桁か3桁の16進数で記述してください。\n" +\
            "       ※ emoji_nameは英数字、ハイフン、アンダーバーで指定してください。\n" +\
            "       ※ 例：@"+bot_name+" add プロ pro -c=000 -bc=FFFFFF\n" +\
            "  - `@"+bot_name+" colors` -- 色一覧が確認できます。\n" +\
            "  - `@"+bot_name+" fonts` -- フォント一覧が確認できます。\n"
