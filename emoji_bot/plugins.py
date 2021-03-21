from io import StringIO
import re
import getopt
from urllib import request
import urllib
from slackbot.bot import respond_to
from slackbot.bot import default_reply

import emojilib

from emoji_bot.upload import do_upload
from emoji_bot.errors import FormatError, AlreadyExistsError, UploadError
from emoji_bot.img_scraping import img_scraping_main
from slackbot_settings import bot_name, default_style, DEFAULT_REPLY, colors, fonts

import requests

@respond_to('help', re.IGNORECASE)
def help(message):
    try:
        print('got command help')
        message.send(DEFAULT_REPLY)
    except Exception as e:
        error_message=" :question: 不明なエラー :question: \n\n"+\
            "再度入力してください :man-bowing:"
        message.reply(error_message)
        print(e)

@respond_to('add_img ([^ ]+) ([-\w]+)$')
def add_img(message, text, emoji_name):
    try:
        print('got command add_img')
        message.reply("画像を取得中です・・・")
        # print('msg:{},text:{},emojiname:{}'.format(message,text,emoji_name))
        search_words = [(text, emoji_name)]
        emojiLists = img_scraping_main(search_words)
        message.reply("スタンプ登録中・・・")
        for index, emojiList in enumerate(emojiLists):
            if index < 3:        
                img = emojiList[0]
                img_name = emojiList[1]
                print(img_name)
                do_upload(img, img_name)
                message.reply("\n\n（´･ω･)╮)）－＝≡ :{}:  `:{}:`".format(img_name, img_name))
    except:
        pass
        


@respond_to('add ([^ ]+) ([-\w]+)$')
@respond_to('add ([^ ]+) ([-\w]+) (-.*)$')
def add(message, text, emoji_name, option=None):
    try:
        style = {
            'color': default_style['color'],
            'back_color': default_style['back_color'],
            'size_fixed': default_style['size_fixed'],
            'disable_stretch': default_style['disable_stretch'],
            'align': default_style['align'],
            'font': default_style['font'],
            'format': default_style['format']
        }

        if option:
            set_style(option, style)
        add_to_slack(message, text, emoji_name, style)
    except FormatError as e:
        error_message=" :man-bowing::man-bowing::man-bowing: 構文エラー!!! :man-bowing::man-bowing::man-bowing: \n\n"+\
            "  "+str(e)+": 入力フォーマットは以下の通りです！\n" +\
            "  - `add <テキスト> <スタンプの名前> [オプション]`\n" +\
            "  - `add_img <画像検索する名前> <スタンプの名前>`\n" +\
            "  詳しくは `help` コマンドで確認！\n"
        message.reply(error_message)
    except UploadError as e:
        error_message=" :no_entry: アップロードエラー  :no_entry: \n\n"+\
            "  アクセストークンが不正です。"
        message.reply(error_message)        
    except AlreadyExistsError as e:
        error_message=" :exclamation: アップロードエラー  :exclamation: \n\n"+\
            "   `:"+emoji_name+":`は既に :"+emoji_name+": で使用されています！\n別の名前を指定して下さい！"
        message.reply(error_message)
    except Exception as e:
        error_message=":question: 不明なエラー :question: \n\n"+\
            "再度入力してください :man-bowing:"
        message.reply(error_message)
        print(e)

@respond_to('colors', re.IGNORECASE)
def color(message):
    print('got command colors')
    color_message = "\n  _Colors_  \n"
    for color_name, color_code in colors.items():
        color_message += '   {}: {},\n'.format(color_name, '#'+color_code)
    message.reply(color_message)

@respond_to('fonts', re.IGNORECASE)
def font(message):
    print('got command fonts')
    font_message = "\n  _Fonts_  \n"
    for index, font_name, in enumerate(fonts.items()):
        font_message += '   {}: :ABC{}:,\n'.format(font_name[0], index+1)
    message.reply(font_message)

def add_to_slack(message, text, emoji_name, style):
    try:
        print('got command add')
        print(text, emoji_name)

        print('- uploading {}'.format(text))
        
        # print(encodenewline(text))
        # print(urllib.parse.quote(encodenewline(text)))

        #print(text)
        #stirngs = text.split("_", 1)
        #print(stirngs)
        #text = stirngs[0] + '\n' + strings[1]

        color = style['color']
        background_color=style['back_color']
        font = style['font']
        # print(font)

        
        img = requests.get(f"https://emoji-gen.ninja/emoji_download?align=center&back_color={background_color}&color={color}&font={font}&locale=ja&public_fg=true&size_fixed=false&stretch=true&text=" + urllib.parse.quote(encodenewline(text)), stream=True)

        """
        data = emojilib.generate(
            text=text.replace('\\n', '\n'),
            width=128,
            height=128,
            color=style['color'],
            background_color=style['back_color'],
            size_fixed=style['size_fixed'],
            disable_stretch=style['disable_stretch'],
            align=style['align'],
            typeface_file=style['font_path'],
            format=style['format']
        )
        """
        # upload to slack
        print("upload to slack")
        do_upload(img.content, emoji_name)

        message.reply("\n\n（´･ω･)╮)）－＝≡ :{}:  `:{}:`".format(emoji_name, emoji_name))
    except Exception as e:
        print(e)
        raise

def set_style(option, style):
    # repatter = re.compile('-([a-z]+) ([^ ]+)')
    # result = repatter.findall(option)
    opts, args = getopt.getopt(option.split(), "c:b:f:", ["color=", "back=", "font="])
    if len(args) > 0:
        raise FormatError('invalid option format')
    else:
        for opt in opts:
            if not opt[1]:
                raise FormatError('invalid option format')      
            elif opt[0] in ('-c', '--color'):
                color_code = get_color_code(opt[1])
                style['color'] = color_code
            elif opt[0] in ('-b', '--back'):
                color_code = get_color_code(opt[1])
                style['back_color'] = color_code
            elif opt[0] in ('-f', '--font'):
                font_path = get_font_path(opt[1])
                style['font'] = font_path

def get_color_code(text):
    text = text.replace('#', '')
    repatter = re.compile('^([\da-fA-F]{6}|[\da-fA-F]{3})$')
    result = repatter.match(text)
    if result:
        color_code = result.group()
        if (len(color_code) == 3):
            color_code = color_code * 2
        return color_code+'FF'
    elif text in colors.keys():
        return colors[text].replace('#','') +'FF'
    else:
        raise FormatError('invalid color format')

def get_font_path(text):
    if text in fonts.keys():
        return fonts[text]
    else:
        raise FormatError('invalid font format')


def encodenewline(text):
    strings = text.split('_')
    newstr = ''
    for index in range(len(strings)):
        if index != len(strings) - 1:
            newstr += strings[index]
            newstr += '\n'
        else:
            newstr += strings[index]
    return newstr