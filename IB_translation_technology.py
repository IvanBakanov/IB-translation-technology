from PIL import Image
from pynput import keyboard
from tkinter import filedialog
from colorama import Back, Style
from pyautogui import screenshot, position
from pytesseract import pytesseract, image_to_string
from google_trans_new import google_translator, LANGUAGES

# text_frame_width/2, text_frame_height/2
tfw, tfh = 150, 30 

# (!)
pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
translator=google_translator()

print(Back.BLUE+'https://github.com/IvanBakanov/IB-translation-technology')
print(Style.RESET_ALL+'version 0.02\n')

dest_lang = input('Destination language: ')

dir_name = filedialog.askdirectory()
screenshot_path = dir_name+'\\screenshot.png'

def on_press_func(key):
    try:
        if key.char == 't':
            screenshot(screenshot_path)
            image = Image.open(screenshot_path)
            x_pos, y_pos = position().x, position().y
            cropped = image.crop((x_pos-tfw, y_pos-tfh, x_pos+tfw, y_pos+tfh))
            cropped.save(screenshot_path)
            text = image_to_string(Image.open(screenshot_path))
            for word in text.split():
                src_lang = translator.detect(word)[0]
                result = translator.translate(word, lang_src=src_lang, lang_tgt=dest_lang)
                print('\n'+word+' -> '+result)
    except: pass

if dest_lang in LANGUAGES.keys() and dir_name:      
    listener = keyboard.Listener(on_press=on_press_func)
    listener.start()
    listener.join()
else:
    print('\nOperation failed :(')
    input()
