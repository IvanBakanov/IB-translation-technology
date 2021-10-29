# IB translation technology

**Eng:** An easy-to-use program that implements the technology of instant translation of a word from a text or from an image from one language to another.

---

**Ru:** Простая в использовании программа, реализующая технологию мгновенного перевода слова из текста или с изображения с одного языка на другой.

### Main libraries
- PyAutoGUI
- PyTesseract (a wrapper for Tesseract-OCR Engine)
- google_trans_new

### User guide
1. Install Tesseract (Windows: https://github.com/UB-Mannheim/tesseract/wiki)
2. Write the full path to the Tesseract executable file in the code (!)
3. Run the program
4. Fill in the "destination language" field (a source language is detected automatically)
> See Languages.txt
5. Select a directory to store the intermediate file in
6. The setup is finished, you can minimize all the program windows

#### How to translate a word
Place the cursor in the center of the word, press the "t" button on the keyboard. The translation will be displayed in the program window.
