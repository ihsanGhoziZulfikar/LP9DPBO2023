# Saya Ihsan Ghozi Zulfikar NIM 2103303 mengerjakan soal Latihan Praktikum 9
# dalam mata kuliah DPBO untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "Rp.10000", 'img1.jpg'))
hunians.append(Rumah("Sekar MK", 5, 2, "Rp.20000", 'img2.jpeg'))
hunians.append(Indekos("Bp. Romi", "Cahya", "Rp.5000", 'img3.jpg'))
hunians.append(Rumah("Satria", 1, 4, "Rp.2500", 'img4.jpg'))
hunians.append(Apartemen("Ihsan Ghozi Zulfikar", 4, 2, "Rp.20000", 'img5.webp'))

root = Tk()
root.title("Praktikum DPBO Python")
imgList = []        # menampung image

# frame detail
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    img = Image.open('assets/images/' + hunians[index].get_image()) 
    img = img.resize((200, 200)) 
    img = ImageTk.PhotoImage(img)
    imgList.append(img)
    img_label = Label(d_frame, image=img)
    img_label.grid(row=1, column=0)

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

# frame home (halaman utama)
def home():
    global frame
    global opts
    landing_frame.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Back", command=landing)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# frame landing (awal)
def landing():
    global frame
    global opts
    if frame:
        frame.destroy()
    if opts:
        opts.destroy()

    global landing_frame
    landing_frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    landing_frame.pack(padx=100, pady=50)

    home_button = Button(landing_frame, text="Start", command=home)
    home_button.grid(row=0, column=0)

    b_exit = Button(landing_frame, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

frame = None
opts = None
landing()

root.mainloop()
