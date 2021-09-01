from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image

COLOR = "#FFE194"
SECOUND_COLOR = "#FFB319"
THIRD_COLOR = "#E8F6EF"
window = Tk()
window.title("Watermark placing")
window.config(bg=COLOR, padx=50, pady=50)
label_font = ""
check_box = 0
font=("Helvetica", 12)

def reset():
    print("hey")
    first_photo_entry.delete(first=0, last=40)
    first_photo_entry.insert(0, "Type the path of the image")
    secound_photo_entry.delete(first=0, last=40)
    secound_photo_entry.insert(0, "Type the path of the watermark image")
    first_photo_submit.config(state="enabled")
    secound_photo_submit.config(state="enabled")
    merged_button.grid_forget()
    save_button.grid_forget()
    save_entry.grid_forget()
    save_label.grid_forget()

def first_button():
    try:
        file_path = filedialog.askopenfile(mode="r").name
        first_photo_entry.delete(first=0,last=26)
        first_photo_entry.insert(0, str(file_path))
        print(file_path)
    except AttributeError:
        messagebox.showerror(title="No file", message="Please choose an image or type the file path.")

def secound_button():
    try:
        file_path = filedialog.askopenfile(mode="r").name
        secound_photo_entry.delete(first=0,last=36)
        secound_photo_entry.insert(0, str(file_path))
        print(file_path)
    except AttributeError:
        messagebox.showerror(title="No file", message="Please choose an image or type the file path.")

def first_submit():
    try:
        image = Image.open(first_photo_entry.get())
        region = image.resize((200, 200), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(region)
        photo_label.config(image=tk_image)
        photo_label.image = tk_image
        photo_label.grid(row=5, column=0)
        answer = messagebox.askquestion(title="Image", message="Is this the image you want to watermark? ")
        if answer:
            first_photo_submit.config(state="disabled")
    except FileNotFoundError:
        messagebox.showerror(title="FIle not found ", message="File not found, please insert a valid file path.")


def secound_submit():
    try:
        watermark = Image.open(secound_photo_entry.get())
        region = watermark.resize((200, 200), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(region)
        watermark_label.config(image=tk_image)
        watermark_label.image = tk_image
        watermark_label.grid(row=5, column=2, sticky="e")
        merged_button.grid(row=8, column=1)
        answer = messagebox.askquestion(title="Image", message="Is this the watermark you want to use? ")
        if answer:
            secound_photo_submit.config(state="disabled")

    except FileNotFoundError:
        messagebox.showerror(title="FIle not found ", message="File not found, please insert a valid file path.")

def merge_photos():
    try:
        photo = Image.open(first_photo_entry.get())
        watermark = Image.open(secound_photo_entry.get())
        width, height = photo.size
        smaller_watermark = watermark.resize((int(int(width)/10), int(int(height)/10)), Image.ANTIALIAS)
        photo.paste(smaller_watermark, (int((int(width)/10)*9), int((int(height)/10)*9)))
        photo.show()
        merged_button.grid_forget()
        save_button.grid(row=9, column=2,)
        save_label.grid(row=9,column=0, sticky="e")
        save_entry.grid(row=9,column=1)
    except FileNotFoundError:
        messagebox.showerror(title="Missing file path", message="Please insert file paths for both images. ")

def save_function():
    photo = Image.open(first_photo_entry.get())
    watermark = Image.open(secound_photo_entry.get())
    width, height = photo.size
    smaller_watermark = watermark.resize((int(int(width) / 10), int(int(height) / 10)), Image.ANTIALIAS)
    photo.paste(smaller_watermark, (int((int(width) / 10) * 9), int((int(height) / 10) * 9)))
    file_path = (first_photo_entry.get()).split("/")
    new_fp = ""
    try:
        for element in file_path[:len(file_path)-1]:
            new_fp = new_fp + element + "/"

        new_fp = new_fp + save_entry.get() + ".png"
        print(new_fp)
        photo.save(fp=new_fp)
        answer = messagebox.askyesno(title="Fiile saved", message=f"File saved at file path: {new_fp}.\n "
                                                                  f"Do you want to watermark another image? ")
        if answer:
            reset()
        else:
            window.destroy()
    except ValueError:
        messagebox.showerror(title="File name", message="Please insert a name for your new file.")


canvas_one = Canvas(width=600, height=100, highlightthickness=0, bg=COLOR)
canvas_one.grid(column=1, row=0, columnspan=2)
logo_img = PhotoImage(file="./img/logo.png")
canvas_logo = canvas_one.create_image(200, 40, image=logo_img)

first_photo_label = Label(text="Insert the photo you want to get watermarked:", width=34, bg=COLOR, font=font)
first_photo_label.grid(column=0, row=1, sticky="w")

first_photo_button = Button(text="Choose file", activebackground=SECOUND_COLOR,
                            bg=THIRD_COLOR,relief="groove", command=first_button, font=font)
first_photo_button.grid(row=1, column=1, sticky="w")

first_photo_submit = Button(text="Submit", activebackground=SECOUND_COLOR,
                            bg=THIRD_COLOR,relief="groove", command=first_submit, width=40, padx=20, font=font)
first_photo_submit.grid(row=4, column=0, columnspan=2, sticky="w")
pading_canvas = Canvas(width=20, height=20, highlightthickness=0, bg=COLOR)
pading_canvas.grid(row=3, column=0)

first_photo_entry = Entry( relief="groove", width=40, bg=THIRD_COLOR, font=font)
first_photo_entry.insert(0,"Type the path of the image")
first_photo_entry.grid(row=2, column=0, sticky="w")

photo_label = Label( bd = 0, height=200, width=200, font=font)


secound_photo_label = Label(text="Insert watermark image:", width=51, bg=COLOR, font=font)
secound_photo_label.grid(column=2, row=1, sticky="w")

secound_photo_entry = Entry( relief="groove", width=37, bg=THIRD_COLOR, font=font)
secound_photo_entry.insert(0,"Type the path of the watermark image")
secound_photo_entry.grid(row=2, column=2, sticky="e")

secound_photo_button = Button(text="Choose file", activebackground="#FFB319",
                              bg="#E8F6EF", relief="groove", command=secound_button, font=font)
secound_photo_button.grid(row=1, column=3, sticky="w")

secound_photo_submit = Button(text="Submit", activebackground=SECOUND_COLOR,
                            bg=THIRD_COLOR,relief="groove", command=secound_submit, width=42, padx=20, font=font)
secound_photo_submit.grid(row=4, column=2, columnspan=2, sticky="e")
pading_canvas_two = Canvas(width=20, height=20, highlightthickness=0, bg=COLOR)
pading_canvas.grid(row=3, column=1)

watermark_label = Label(bd = 0, height=200, width=200, font=font)


pading_canvas_three = Canvas(width=20, height=20, highlightthickness=0, bg=COLOR)
pading_canvas_three.grid(row=6, column=1)


merged_button = Button(text="Watermark photo",activebackground=SECOUND_COLOR,
                      bg=THIRD_COLOR,relief="groove", command=merge_photos, width=40, padx=20, font=font)

pading_canvas_four = Canvas(width=20, height=20, highlightthickness=0, bg=COLOR)
pading_canvas_four.grid(row=7, column=1)

save_label = Label(text="Type the name of your new file:", width=32, bg=COLOR, font=font)
save_entry = Entry(relief="groove", width=43, bg=THIRD_COLOR, font=font)

save_button = Button(text="Save photo",activebackground=SECOUND_COLOR,
                      bg=THIRD_COLOR,relief="groove", command=save_function, width=40, padx=20, font=font)





window.mainloop()
