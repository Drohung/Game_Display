import tkinter as tk
from PIL import ImageTk, Image
import time
import linecache
import os
import sys
import config


def main():
    args = sys.argv
    if len(args) < 2:
        print("Please use your encounter folder name and try again.")
        sys.exit(1)
    file_dir = f"Encounters/{args[1]}/"
    if not os.path.isdir(file_dir):
        print("The directory does not exist, please try again.")
        print(file_dir)
        sys.exit(1)
    root = tk.Tk()
    root.title(args[1])
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    canvas = tk.Canvas(root, bg='black')
    canvas.pack(fill=tk.BOTH, expand=True)
    phase_tk = tk.IntVar()
    phase_tk.set(1)
    image = Image.open(f"{file_dir}Phases/Phase_1.png")
    resized_image = image.resize((config.width, config.height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    background_image_ID = canvas.create_image(0, 0, image=bg_image, anchor="nw")
    root.update_idletasks
    rnd_index_tk = tk.IntVar()
    rnd_index_tk.set(1)
    text_id = canvas.create_text(config.center_w, config.text_h, text="", font=("Arial", 24), fill=config.text_color, anchor='c', tag="Text")
    text_id = canvas.create_text(20, 20, text=rnd_index_tk.get(), font=("Arial", 20), fill=config.round_color, anchor='nw', tag="Round")
    file = open(f"{file_dir}Phases/Phase_1.txt")
    full_text_tk = tk.StringVar()
    full_text_tk.set(file.readlines())
    txt_index_tk = tk.IntVar()
    txt_index_tk.set(0)
    keep_image = []

    def type_text(event, index=0):
        config.delay
        txt_index = txt_index_tk.get()
        full_text_fill = full_text_tk.get()
        full_text = full_text_fill.split(',')
        if len(full_text) < (txt_index + 1):
            txt_index_tk.set(0)
            txt_index = 0
        new_text = full_text[txt_index]
        text_to_input = new_text.replace('(', '').replace('"', '').replace(')', '').replace("'", '').strip("\\n")
        if index == len(text_to_input):
            txt_index += 1
            txt_index_tk.set(txt_index)
        if index < len(text_to_input):
            current_text = ""
            current_text += text_to_input[:index+1]
            canvas.itemconfigure("Text", text=current_text)
            canvas.after(config.delay, lambda: type_text(event, index+1))

    def phase_change(event, bg_image, keep_image):
        phase = phase_tk.get()
        phase += 1
        super_image = bg_image
        new_file_text = f"{file_dir}Phases/Phase_{phase}.txt"
        if os.path.exists(f"{file_dir}Phases/Phase_{phase}.txt"):
            phase_tk.set(phase)
            txt_index_tk.set(0)
            new_file = open(f"{file_dir}Phases/Phase_{phase}.txt")
            full_text_tk.set(new_file.readlines())
            image = Image.open(f"{file_dir}Phases/Phase_{phase}.png")
            resized_image = image.resize((config.width, config.height), Image.LANCZOS)
            new_bg_image = ImageTk.PhotoImage(resized_image)
            canvas.itemconfigure(background_image_ID, image=new_bg_image)
            keep_image.append(new_bg_image)
            bg_image = new_bg_image

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

    def rainbow_end_text(event, letter_index=3, index=0, color_index=0):
        root.unbind('<Return>')
        config.delay
        delay2 = 60
        if os.path.exists(f"{file_dir}Phases/rainbow_text.txt"):
            rainbow_txt = open(f"{file_dir}Phases/rainbow_text.txt")
            rainbow_list = rainbow_txt.readlines()
            rainbow_line = str(rainbow_list[0])
            rainbow_text = rainbow_line.replace('(', '').replace(')', '').replace("'", '').strip("\\n")
            color_list = ["red", "orange", "yellow", "lawn green", "green", "blue", "cyan", "indigo", "magenta2"]
            if index < len(rainbow_text):
                color = color_list[index % len(color_list)]
                canvas.itemconfigure("Text", text='')
                r_text = rainbow_text[index]
                text_id == canvas.create_text(config.r_text_point + ((index + 1) *60), config.text_h, text=r_text, fill=color, font=("DotumChe", 48, "bold"), anchor="c", tags=(index))
                canvas.after(config.delay, lambda: rainbow_end_text(event, letter_index, index+1, color_index+1))
            if index >= len(rainbow_text):
                if color_index >= len(color_list):
                    color_index = 0
                if (letter_index-2) > len(rainbow_text):
                    letter_index = 3
                if canvas.itemcget(index, 'text') == ' ':
                    letter_index += 1
                color2 = color_list[color_index]
                canvas.itemconfigure(letter_index + 1, fill=color2)
                canvas.after(delay2, lambda: rainbow_end_text(event, letter_index+1, index, color_index+1))
    
    def increase_round(event):
        current_round = rnd_index_tk.get()
        current_round += 1
        canvas.itemconfigure("Round", text=current_round)
        rnd_index_tk.set(current_round)

    def decrease_round(event):
        current_round = rnd_index_tk.get()
        current_round -= 1
        canvas.itemconfigure("Round", text=current_round)
        rnd_index_tk.set(current_round)

    def hide_round(event):
        current_round = rnd_index_tk.get()
        if canvas.itemcget("Round", 'text') == '':
            canvas.itemconfigure("Round", text=current_round)
        else:
            canvas.itemconfigure("Round", text='')

    def exit_event(event):
        sys.exit(0)  
    
    root.bind('<Tab>', commit_fullscreen)
    root.bind('<Return>', type_text)
    root.bind('<space>', lambda event: phase_change(event, bg_image, keep_image))
    root.bind('<Shift_L>', rainbow_end_text)
    root.bind('<Escape>', exit_event)
    root.bind('<Shift_R>', increase_round)
    root.bind('<BackSpace>', decrease_round)
    root.bind('<Control_R>', hide_round)
    
    root.mainloop()

if __name__ == "__main__":
    main()