from tkinter import *
from tkinter import messagebox
import base64
import os


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text_1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        label_3 = Label(screen1, text="Encrypt", font=("Arial", 12), fg="white", bg="#ed3833")
        label_3.place(x=10, y=0)

        text_2 = Text(screen1, font=("Arial", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_2.place(x=10, y=40, width=380, height=150)

        text_2.insert(END, encrypt)

    else:
        messagebox.showerror('Error')




def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text_1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        label_3 = Label(screen2, text="Decrypt", font=("Arial", 12), fg="white", bg="#00bd56")
        label_3.place(x=10, y=0)

        text_2 = Text(screen2, font=("Arial", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_2.place(x=10, y=40, width=380, height=150)

        text_2.insert(END, decrypt)

    else:
        messagebox.showerror('Error')


def main_screen():

    global code
    global screen
    global text_1

    screen = Tk()
    screen.geometry("375x398")
    #image_icon = PhotoImage(file=)
    #screen.iconphoto(False, image_icon)
    screen.title("Message Encryption App")

    def reset():
        code.set("")
        text_1.delete(1.0, END)


    label_1 = Label(text="Enter text for encryption and decryption", fg="black", font=("Arial", 14))
    label_1.place(x=20, y=10)

    text_1 = Text(font=("Arial", 14), bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_1.place(x=20, y=50, width=335, height=100)

    label_2 = Label(text="Enter the secret key for\nencryption and decryption", fg="black", font=("Arial", 14))
    label_2.place(x=20, y=170, width=335, height=40)

    code = StringVar()
    entry = Entry(textvariable=code, width=19, bd=0, font=("Arial", 14), show="*")
    entry.place(x=20, y=220, width=335)


    btn_1 = Button(text="Encrypt", height=2, width=15, bg="light blue", bd=0, font=("Arial", 12, "bold"), command=encrypt)
    btn_1.place(x=20, y=270)

    btn_2 = Button(text="Decrypt", height=2, width=15, bg="light green", bd=0, font=("Arial", 12, "bold"), command=decrypt)
    btn_2.place(x=200, y=270)

    btn_2 = Button(text="Reset", height=2, width=33, bg="pink", bd=0, font=("Arial", 12, "bold"), command=reset)
    btn_2.place(x=20, y=330)

    screen.mainloop()


main_screen()

