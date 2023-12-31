#Import Modules
from googletrans import Translator
import pyttsx3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip
from tkinter import messagebox
#-----------------------------------Translate-----------------------------------#
def translate():
    output_text.delete("1.0",END)
    inp = input_text.get("1.0",END)
    tr = Translator()
    try:
        translation = tr.translate(text=inp,src=input_lang.get(),dest=output_lang.get())
        output_text.insert("end-1c", translation.text)
    except ValueError:
        messagebox.showerror(title="error", message="Choose a language")
    except IndexError:
        messagebox.showerror(title="error", message="Nothing to translate")
    
#-----------------------------------Voice-----------------------------------#
def play_audio():
    voice = pyttsx3.init()
    voice.say(output_text.get("1.0",END))
    voice.runAndWait()
#-----------------------------------Copy-----------------------------------#
def copy():
    text = output_text.get("1.0",END)
    pyperclip.copy(text=text)
#-----------------------------------UI-----------------------------------#
root = ttk.Window(themename="cosmo")
root.title("Translator")
root.geometry("870x700")
# root.resizable(0,0)
# root.config(padx=50)

# label = ttk.Label(text="German to English",font=("Arial",25))
# label.grid(row=0,column=0,columnspan=2)

canavs = ttk.Canvas(width=256,height=256)
file = ttk.PhotoImage(file="logo.png")
canavs.create_image(128,128,image=file)
canavs.place(x=0,y=0)


input_lang = ttk.Combobox(width=23)
input_lang['values'] = ("German", "English")
input_lang.set("Choose language")
input_lang['state'] = "readonly"
input_lang.place(x=50,y=200)
input_text = ttk.Text(wrap=ttk.WORD,height=10,width=25)
input_text.place(x=50,y=250)

output_lang = ttk.Combobox(width=23)
output_lang['values'] = ("German", "English")
output_lang.set("Choose language")
output_lang['state'] = "readonly"
output_lang.place(x=500,y=200)
output_text = ttk.Text(wrap=WORD,height=10,width=25)
output_text.place(x=500,y=250)

search_img = ttk.PhotoImage(file="search_logo.png")
translate_btn = ttk.Button(text="Translate",image=search_img,compound=LEFT, bootstyle="primary",command=translate)
translate_btn.place(x=380,y=650)

#voice
image = ttk.PhotoImage(file="voice_logo.png")
voice_image = image.subsample(1,1)
voice_btn = ttk.Button(image=voice_image,bootstyle="primary",command=play_audio)
voice_btn.place(x=500,y=580)

#copy to clipboard
copy_image = ttk.PhotoImage(file="copy_logo.png")
copy_btn = ttk.Button(image=copy_image,bootstyle="primary",command=copy)
copy_btn.place(x=570,y=580)

root.mainloop()



