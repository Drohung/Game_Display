import tkinter as tk
from PIL import ImageTk, Image
import time
import linecache
import os


def main():
    root = tk.Tk()
    root.title("The Ruby Knight")
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    canvas = tk.Canvas(root, bg='black')
    canvas.pack(fill=tk.BOTH, expand=True)
    phase_tk = tk.IntVar()
    phase_tk.set(1)
    root.update_idletasks
    text_id = canvas.create_text(960, 540, text="", font=("Arial", 24), fill="white", anchor='c')
    file = open('phase1.txt')
    full_text_tk = tk.StringVar()
    full_text_tk.set(file.readlines())
    txt_index_tk = tk.IntVar()
    txt_index_tk.set(0)

    def type_text(event, index=0):
        delay = 100
        txt_index = txt_index_tk.get()
        full_text_fill = full_text_tk.get()
        full_text = full_text_fill.split(',')
        if len(full_text) < (txt_index + 1):
            txt_index_tk.set(0)
            txt_index = 0
        new_text = full_text[txt_index]
        text_to_input = new_text.replace('(', '').replace(')', '').replace("'", '').strip("\\n")
        if index == len(text_to_input):
            txt_index += 1
            txt_index_tk.set(txt_index)
        if index < len(text_to_input):
            current_text = ""
            current_text += text_to_input[:index+1]
            canvas.itemconfigure(text_id, text=current_text)
            canvas.after(delay, lambda: type_text(event, index+1))
            

    def phase_change(event):
        phase = phase_tk.get()
        phase += 1
        new_file_text = f"Phases/Phase_{phase}.txt"
        if os.path.exists(f"Phases/Phase_{phase}.txt"):
            phase_tk.set(phase)
            txt_index_tk.set(0)
            new_file = open(f"Phases/Phase_{phase}.txt")
            full_text_tk.set(new_file.readlines())
        else:
            full_text_tk.set('You have emerged victorious!')
    
    def key_press(event):
        lambda event: type_text(event, new_text, full_text)
    
    def exit_fullscreen(event):
        root.attributes('-fullscreen', False)

    def commit_fullscreen(event):
        if root.attributes('-fullscreen') == True:
            root.attributes('-fullscreen', False)
        if root.attributes('-fullscreen') == False:
            root.attributes('-fullscreen', True)
    
    root.bind('<Escape>', commit_fullscreen)
    root.bind('<a>', type_text)
    root.bind('<d>', phase_change)
    
    root.mainloop()


if __name__ == "__main__":
    main()





