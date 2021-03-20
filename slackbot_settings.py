import matplotlib

team_name = 'hackteam2workspace'
bot_name = 'custom-stamp-bot'

API_TOKEN = ''
cookie = ''

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
