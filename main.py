from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet


window=Tk()
window.title("Secret Notes")
window.minsize(width=300,height=700)
window.config()

img=PhotoImage(file="img.png")
canvas =Canvas(height=200,width=200)
canvas.create_image(100,100,image=img)
canvas.place(x=50,y=0)

key = Fernet.generate_key()
fernet = Fernet(key)


text_ent=Label(text="Enter your title")
text_ent.place(x=110,y=170)

ent_text=Entry(width=40)
ent_text.place(x=30,y=200)

tetx_secret=Label(text="Enter your secret")
tetx_secret.place(x=106,y=220)

text_mesaj=Text(width=30,height=15)
text_mesaj.place(x=30,y=250)

text_key=Label(text="Enter master key")
text_key.place(x=110,y=500)

ent_key=Entry(width=40)
ent_key.place(x=30,y=520)

list={}
def save():
    m_title=ent_text.get()
    m_text=text_mesaj.get("1.0",END)
    m_key=ent_key.get()

    encrypt(m_text,m_key)
    mesaj=encrypt(m_text,m_key)

    if len(m_text)==0 or len(m_key)==0 or len(m_title)==0:
        messagebox.showinfo(title="Error",message="Enter all info")
    else:
        try:
            with open("secret.txt","a") as data_file:
                data_file.write(f"\n{m_title}\n{mesaj}")
        except FileNotFoundError:
            with open("secret.txt","w") as data_file:
                data_file.write(f"\n{m_title}\n{mesaj}")
        finally:
            ent_text.delete(0,END)
            text_mesaj.delete("1.0",END)
            ent_key.delete(0,END)


def encrypt(data,key_t):
    enc_text=fernet.encrypt(data.encode())
    list[key_t]=enc_text
    return enc_text


def decrypto(key,data):
    for i in list.keys():
        if key == i:
           deenct=fernet.decrypt(data)
           return deenct

def yaz():
    m_text = text_mesaj.get("1.0", END)
    m_key = ent_key.get()

    if len(m_text) == 0 or len(m_key) == 0:
        messagebox.showinfo(title="Error", message="Enter all info")
    else:
        try:
            decrypto(key,m_text)
            k=decrypto(m_key,m_text)
            text_mesaj.delete("1.0",END)
            text_mesaj.insert("1.0",k)
        except:
            messagebox.showinfo(title="Error", message="Enter encrypted text")

but_save=Button(text="Save & Encrypt",command=save)
but_save.place(x=110,y=550)

but_denc=Button(text="Dencrypt",command=yaz)
but_denc.place(x=120,y=590)


window.mainloop()
