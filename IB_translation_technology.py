from PIL import Image
from pynput import keyboard
from tkinter import filedialog
from colorama import Back, Style
from pyautogui import screenshot, position
from pytesseract import pytesseract, image_to_string
from google_trans_new import google_translator, LANGUAGES

# text_frame_width/2, text_frame_height/2
tfw, tfh=150, 30 

pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator=google_translator()

print(Back.BLUE+'© Bakanov Ivan\nhttps://github.com/IvanBakanov')
print(Style.RESET_ALL+'Version 0.01\n')

dest_language=input('Destination language: ')

dir_name=filedialog.askdirectory()
screenshot_path=dir_name+'\\screenshot.png'

def On_press_func(key):
    if key.char=='t':
        screenshot(screenshot_path)
        image=Image.open(screenshot_path)
        x_pos, y_pos=position().x, position().y
        cropped=image.crop((x_pos-tfw, y_pos-tfh, x_pos+tfw, y_pos+tfh))
        cropped.save(screenshot_path)
        text=image_to_string(Image.open(screenshot_path))
        for word in text.split():
            result=translator.translate(word, lang_tgt=dest_language)
            print('\n'+word+' -> '+result)

if dest_language in LANGUAGES.keys() and dir_name:      
    listener=keyboard.Listener(on_press=On_press_func)
    listener.start()
    listener.join()
else:
    print('\nOperation failed :(')
    input()