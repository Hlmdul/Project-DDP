from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import converter as conv
import ttkbootstrap as ttkbs
from tkinter.font import nametofont
from PIL import ImageTk, Image


############################################################################################################
# Functions
# Button Press Functions

def disable():
  disable_list = [bin_entry, des_entry, okt_entry, hex_entry, conv_bin, conv_des, conv_okt, conv_hex, del_bin, del_des, del_okt, del_hex, clr_bin, clr_des, clr_okt, clr_hex]
  for i in disable_list:
    i.configure(state=tk.DISABLED)
  return

def enable():
  enable_list = [bin_entry, des_entry, okt_entry, hex_entry, conv_bin, conv_des, conv_okt, conv_hex, del_bin, del_des, del_okt, del_hex, clr_bin, clr_des, clr_okt, clr_hex]
  for i in enable_list:
    i.configure(state=tk.NORMAL)
  return

def output_entry():
  entry_list = [bin_entry, des_entry, okt_entry, hex_entry]
  for i in entry_list:
    i.configure(background='black', foreground='green', font=fontmedium)
      

# Biner-------------------------------------------------------------------------------------------------------------------
def bin_disable():
  disable_list = [des_entry, okt_entry, hex_entry, conv_des, conv_okt, conv_hex, del_des, del_okt, del_hex, clr_des, clr_okt, clr_hex]
  disable_list.extend(des_btn_list)
  disable_list.append(des0)
  disable_list.extend(okt_btn_list)
  disable_list.extend(hex_btn_list)
  for i in disable_list:
    i.configure(state=tk.DISABLED)
  return

def bin_enable():
  enable_list = [des_entry, okt_entry, hex_entry, conv_des, conv_okt, conv_hex, del_des, del_okt, del_hex, clr_des, clr_okt, clr_hex]
  enable_list.extend(des_btn_list)
  enable_list.append(des0)
  enable_list.extend(okt_btn_list)
  enable_list.extend(hex_btn_list)
  for i in enable_list:
    i.configure(state=tk.NORMAL)
  return

def bin_entry_button(text):
  bin_entry.insert(END, text)
  bin_disable()
  return

def bin_entry_convert():
  num = conv.Biner(bin_entry.get())
  des_entry_var.set(num.toDesimal())
  okt_entry_var.set(num.toOktal())
  hex_entry_var.set(num.toHexa())
  output_entry()
  bin_entry.configure(background='black', foreground='red', font=fontmedium)
  return

def delete_bin():
  bin_entry.delete(len(bin_entry.get())-1, END)
  return

def clear_bin():
  bin_entry.delete(0, END)
  enable()
  bin_enable()
  des_entry.delete(0, END)
  okt_entry.delete(0, END)
  hex_entry.delete(0, END)
  return

# ------------------------------------------------------------------------------------------------------------------------

# Desimal-----------------------------------------------------------------------------------------------------------------
def des_disable():
  disable_list = [bin_entry, okt_entry, hex_entry, conv_bin, conv_okt, conv_hex, del_bin, del_okt, del_hex, clr_bin, clr_okt, clr_hex]
  disable_list.extend(bin_btn_list)
  disable_list.extend(okt_btn_list)
  disable_list.extend(hex_btn_list)
  for i in disable_list:
    i.configure(state=tk.DISABLED)
  return

def des_enable():
  enable_list = [bin_entry, okt_entry, hex_entry, conv_bin, conv_okt, conv_hex, del_bin, del_okt, del_hex, clr_bin, clr_okt, clr_hex]
  enable_list.extend(bin_btn_list)
  enable_list.extend(okt_btn_list)
  enable_list.extend(hex_btn_list)
  for i in enable_list:
    i.configure(state=tk.NORMAL)
  return 

def des_entry_button(text):
  des_entry.insert(END, text)
  des_disable()
  return

def des_entry_convert():
  num = conv.Desimal(des_entry.get())
  bin_entry_var.set(num.toBiner())
  okt_entry_var.set(num.toOktal())
  hex_entry_var.set(num.toHexa())
  output_entry()
  des_entry.configure(background='black', foreground='red', font=fontmedium)
  return

def delete_des():
  des_entry.delete(len(des_entry.get())-1, END)
  return

def clear_des():
  des_entry.delete(0, END)
  enable()
  des_enable()
  bin_entry.delete(0, END)
  okt_entry.delete(0, END)
  hex_entry.delete(0, END)
  return

# ------------------------------------------------------------------------------------------------------------------------
  
# Octal-------------------------------------------------------------------------------------------------------------------
def okt_disable():
  disable_list = [bin_entry, des_entry, hex_entry, conv_bin, conv_des, conv_hex, del_bin, del_des, del_hex, clr_bin, clr_des, clr_hex]
  disable_list.extend(bin_btn_list)
  disable_list.extend(des_btn_list)
  disable_list.extend(hex_btn_list)
  disable_list.append(des0)
  for i in disable_list:
    i.configure(state=tk.DISABLED)
  return

def okt_enable():
  enable_list = [bin_entry, des_entry, hex_entry, conv_bin, conv_des, conv_hex, del_bin, del_des, del_hex, clr_bin, clr_des, clr_hex]
  enable_list.extend(bin_btn_list)
  enable_list.extend(des_btn_list)
  enable_list.extend(hex_btn_list)
  enable_list.append(des0)
  for i in enable_list:
    i.configure(state=tk.NORMAL)
  return

def okt_entry_button(text):
  okt_entry.insert(END, text)
  okt_disable()
  return

def okt_entry_convert():
  num = conv.Oktal(okt_entry.get())
  bin_entry_var.set(num.toBiner())
  des_entry_var.set(num.toDesimal())
  hex_entry_var.set(num.toHexa())
  okt_disable()
  output_entry()
  okt_entry.configure(background='black', foreground='red', font=fontmedium)
  return

def delete_okt():
  okt_entry.delete(len(okt_entry.get())-1, END)
  return

def clear_okt():
  okt_entry.delete(0, END)
  enable()
  okt_enable()
  bin_entry.delete(0, END)
  des_entry.delete(0, END)
  hex_entry.delete(0, END)
  return


# ------------------------------------------------------------------------------------------------------------------------
  
# Hexadesimal-------------------------------------------------------------------------------------------------------------
def hex_disable():
  disable_list = [bin_entry, des_entry, okt_entry, conv_bin, conv_des, conv_okt, del_bin, del_des, del_okt, clr_bin, clr_des, clr_okt]
  disable_list.extend(bin_btn_list)
  disable_list.extend(des_btn_list)
  disable_list.extend(okt_btn_list)
  disable_list.append(des0)
  for i in disable_list:
    i.configure(state=tk.DISABLED)
  return

def hex_enable():
  enable_list = [bin_entry, des_entry, okt_entry, conv_bin, conv_des, conv_okt, del_bin, del_des, del_okt, clr_bin, clr_des, clr_okt]
  enable_list.extend(bin_btn_list)
  enable_list.extend(des_btn_list)
  enable_list.extend(okt_btn_list)
  enable_list.append(des0)
  for i in enable_list:
    i.configure(state=tk.NORMAL)
  return

def hex_entry_button(text):
  hex_entry.insert(END, text)
  hex_disable()
  return

def hex_entry_convert():
  num = conv.Hexa(hex_entry.get())
  bin_entry_var.set(num.toBiner())
  des_entry_var.set(num.toDesimal())
  okt_entry_var.set(num.toOktal())
  hex_disable()
  output_entry()
  hex_entry.configure(background='black', foreground='red', font=fontmedium)
  return

def delete_hex():
  hex_entry.delete(len(hex_entry.get())-1, END)
  return

def clear_hex():
  hex_entry.delete(0, END)
  hex_enable()
  bin_entry.delete(0, END)
  des_entry.delete(0, END)
  okt_entry.delete(0, END)
  return

# ------------------------------------------------------------------------------------------------------------------------
  
# Others -----------------------------------------------------------------------------------------------------------------

def reset_button():
  des_entry.delete(0,END)
  bin_entry.delete(0,END)
  okt_entry.delete(0,END)
  hex_entry.delete(0,END)
  bin_entry['state'] = des_entry['state'] = okt_entry['state'] = hex_entry['state'] = bin_entry_button['state'] = des_entry_button['state'] = okt_entry_button['state'] = hex_entry_button['state'] =  tk.NORMAL
  return

# ------------------------------------------------------------------------------------------------------------------------

############################################################################################################


############################################################################################################
# Window Configure
window = tk.Tk()
window.title('Konverter Sistem Bilangan')
window.iconbitmap('Project DDP\\image\\kalku.ico')
# window.geometry('1200x600')
# window.resizable(0,0)
window.columnconfigure((0,1,2,3,4,5), weight = 1)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight = 1)
theme = ttkbs.Style(theme='sandstone')

############################################################################################################

############################################################################################################
# Style
fontsmall = ('Verdana', 11, 'bold')
fontmedium = ('Verdana', 14, 'bold')
fontlarge = ('Verdana', 25, 'bold')

style = ttk.Style()
style.configure('Green.TButton', foreground='green', font=fontsmall, relief='raised', background='green')
style.configure('Red.TButton', foreground='red', font=fontsmall, relief='raised', background='red', width=5, height=1)
style.configure('Green.Entry', foreground='green', font=fontsmall, relief='raised', background='green')
style.configure('Red.Entry', foreground='white', font=fontsmall, relief='raised', background='white', width=5, height=1)
style.configure('Button.TButton', foreground='black', font=fontsmall, relief='raised', background='black')

defaultfont = nametofont("TkDefaultFont")
defaultfont.configure(size=12, weight='bold')


############################################################################################################

############################################################################################################
# Frames

# Margin Frame =========================================================================================================
margin_top = tk.Frame(window, bg='black', height=10)
margin_top.grid(row=0, column=0, columnspan=6, sticky='nsew')

margin_left = tk.Frame(window, bg='black', width=10)
margin_left.grid(row=1, column=0, rowspan=3, sticky='nsew')

margin_right = tk.Frame(window, bg='black', width=10)
margin_right.grid(row=1, column=5, rowspan=3, sticky='nsew')

margin_bottom = tk.Frame(window, bg='black', height=10)
margin_bottom.grid(row=4, column=0, columnspan=6, sticky='nsew')

# Margin Frame End =====================================================================================================


# Frame Judul ==========================================================================================================
judul_frame = ttk.Frame(window, relief='raised', borderwidth=2)
judul_frame.grid(row=1, column=1, columnspan=4, sticky='nsew', padx=3, pady=10)
judul_frame.columnconfigure((0), weight = 1)

judul = ttk.Label(judul_frame, text='Konversi Bilangan', font=fontlarge, anchor='center', justify='center')
judul.pack()

# Frame Judul End ======================================================================================================


# Frame Biner ==========================================================================================================
bin_frame = ttk.Frame(window, width=300, height=400, relief='raised', padding=10)
bin_frame.grid(row=2, column=1, sticky='nsew', padx=3)
bin_frame.columnconfigure((0,1,2,3,4), weight = 1)
bin_frame.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1)

label_biner = ttk.Label(master=bin_frame, text='Biner', font=fontmedium, anchor='center', justify='center') #Label
label_biner.grid(row=0, column=1, columnspan=3, sticky='nsew')

bin_entry_var = tk.StringVar()
bin_entry = ttk.Entry(master=bin_frame, font=fontmedium, width=10, textvariable=bin_entry_var) #Entry
bin_entry.configure(background='black', foreground='red', font=fontmedium)
bin_entry.grid(row=2, column=1, columnspan=3, sticky='ew',pady=10, padx=5)

button_frame = tk.Frame(master=bin_frame, width=200, height=200) #Button Frame
button_frame.grid(row=3, column=1, columnspan=3, rowspan=4, sticky='nsew')
button_frame.columnconfigure((0,1), weight = 1)
button_frame.rowconfigure((0), weight = 1)

width_setter = tk.Frame(master=button_frame, width=300) #Width Setter
width_setter.grid(row=0, column=0, columnspan=3)

height_setter = tk.Frame(master=button_frame, height=175) #Height Setter
height_setter.grid(row=0, column=0, rowspan=4)

bin0 = ttk.Button(master=button_frame, text='0', command=lambda:bin_entry_button('0'), bootstyle='primary-outline', takefocus=False) #Button
bin0.grid(row=0, column=0, sticky='nsew', padx=5)

bin1 = ttk.Button(master=button_frame, text='1', command=lambda:bin_entry_button('1'), bootstyle='primary-outline', takefocus=False) #Button
bin1.grid(row=0, column=1, sticky='nsew', padx=5)

bin_btn_list = [bin0, bin1]

conv_bin = ttk.Button(master=bin_frame, text='Convert', command=bin_entry_convert, bootstyle='success', takefocus=False, width=4) #Button 
conv_bin.grid(row=9, column=3, pady=10, sticky='ew', padx=5)


del_clr_frame = tk.Frame(master=bin_frame, height=10) #Empty Frame
del_clr_frame.grid(row=9, column=1, columnspan=2, sticky='ew', padx=5)
del_clr_frame.columnconfigure((0,1), weight = 1)

del_bin = ttk.Button(master=del_clr_frame, text='Del', command=delete_bin, bootstyle='warning-outline', takefocus=False, width=2) #Button
del_bin.grid(row=9, column=0, pady=10, sticky='ew')

clr_bin = ttk.Button(master=del_clr_frame, text='Clear', command=clear_bin, bootstyle='danger-outline', takefocus=False, width=2) #Button
clr_bin.grid(row=9, column=1, pady=10, sticky='ew')


# Frame Biner End ======================================================================================================


# Frame Desimal ========================================================================================================
des_frame = ttk.Frame(window, width=300, height=400, relief='raised', padding=10)
des_frame.grid(row=2, column=2, sticky='nsew', padx=3)
des_frame.columnconfigure((0,1,2,3,4), weight = 1)
des_frame.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1)

label_desimal = ttk.Label(master=des_frame, text='Desimal', font=fontmedium, anchor='center', justify='center') #Label
label_desimal.grid(row=0, column=1, columnspan=3, sticky='nsew')

des_entry_var = tk.StringVar()
des_entry = ttk.Entry(master=des_frame, font=fontmedium, width=10, textvariable=des_entry_var) #Entry
des_entry.grid(row=2, column=1, columnspan=3, sticky='ew', pady=10)

button_frame = tk.Frame(master=des_frame, width=200, height=200, bg='dark grey') #Button Frame
button_frame.grid(row=3, column=1, columnspan=3,rowspan=4, sticky='nsew')
button_frame.columnconfigure((0,1,2), weight = 1)
button_frame.rowconfigure((0,1,2,3), weight = 1)
width_setter = tk.Frame(master=button_frame, bg='dark grey', width=300) #Width Setter
width_setter.grid(row=0, column=0, columnspan=3)
height_setter = tk.Frame(master=button_frame, bg='dark grey', height=150) #Height Setter
height_setter.grid(row=0, column=0, rowspan=4)

des1 = des2 = des3 = des4 = des5 = des6 = des7 = des8 = des9 = des0 = ttk.Button()
des_btn_list = [des1, des2, des3, des4, des5, des6, des7, des8, des9, des0]
for i in range (len(des_btn_list[:9])):
  des_btn_list[i] = ttk.Button(master=button_frame, text=str(i+1), command=lambda i=i: des_entry_button(str(i+1)),bootstyle='primary-outline', takefocus=False) #Num Button
  des_btn_list[i].grid(row=i//3, column=i%3, sticky='nsew', padx=5, pady=5)

des0 = ttk.Button(master=button_frame, text='0', command=lambda: des_entry_button('0'),bootstyle='primary-outline', takefocus=False) #Num Button
des0.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

conv_des = ttk.Button(master=des_frame, text='Convert', command=des_entry_convert, bootstyle='success', takefocus=False, width=4) #Button 
conv_des.grid(row=9, column=3, pady=10, sticky='ew', padx=5)


del_clr_frame = tk.Frame(master=des_frame, height=10) #Empty Frame
del_clr_frame.grid(row=9, column=1, columnspan=2, sticky='ew', padx=5)
del_clr_frame.columnconfigure((0,1), weight = 1)

del_des = ttk.Button(master=del_clr_frame, text='Del', command=delete_des, bootstyle='warning-outline', takefocus=False, width=2) #Button
del_des.grid(row=9, column=0, pady=10, sticky='ew')

clr_des = ttk.Button(master=del_clr_frame, text='Clear', command=clear_des, bootstyle='danger-outline', takefocus=False, width=2) #Button
clr_des.grid(row=9, column=1, pady=10, sticky='ew')



# Frame Desimal End ====================================================================================================


# Frame Octal ==========================================================================================================
okt_frame = ttk.Frame(window, width=300, height=400, relief='raised', padding=10)
okt_frame.grid(row=2, column=3, sticky='nsew', padx=3)
okt_frame.columnconfigure((0,1,2,3,4), weight = 1)
okt_frame.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1)

label_oktal = ttk.Label(master=okt_frame, text='Oktal', font=fontmedium, anchor='center', justify='center') #Label
label_oktal.grid(row=0, column=1, columnspan=3, sticky='nsew')

okt_entry_var = tk.StringVar()
okt_entry = ttk.Entry(master=okt_frame, font=fontmedium, width=10, textvariable=okt_entry_var) #Entry
okt_entry.grid(row=2, column=1, columnspan=3, sticky='ew',pady=10)


button_frame = tk.Frame(master=okt_frame, width=200, height=200, bg='dark grey') #Button Frame
button_frame.grid(row=3, column=1, columnspan=3,rowspan=4, sticky='nsew')
button_frame.columnconfigure((0,1,2), weight = 1)
button_frame.rowconfigure((0,1,2), weight = 1)
width_setter = tk.Frame(master=button_frame, bg='dark grey', width=300) #Width Setter
width_setter.grid(row=0, column=0, columnspan=3)
height_setter = tk.Frame(master=button_frame, bg='black', height=175) #Height Setter
height_setter.grid(row=0, column=0, rowspan=4)

okt0 = okt1 = okt2 = okt3 = okt4 = okt5 = okt6 = okt7 = ttk.Button()
okt_btn_list = [okt1, okt2, okt3, okt4, okt5, okt6, okt7, okt0]
for i in range(8):
  okt_btn_list[i] = ttk.Button(master=button_frame, text=str(i), command=lambda i=i: okt_entry_button(str(i)), bootstyle='primary-outline', takefocus=False) #Num Button
  okt_btn_list[i].grid(row=i//3, column=i%3, sticky='nsew', padx=5, pady=5)

conv_okt = ttk.Button(master=okt_frame, text='Convert', command=okt_entry_convert, bootstyle='success', takefocus=False, width=4) #Button 
conv_okt.grid(row=9, column=3, pady=10, sticky='ew', padx=5)


del_clr_frame = tk.Frame(master=okt_frame, height=10) #Empty Frame
del_clr_frame.grid(row=9, column=1, columnspan=2, sticky='ew', padx=5)
del_clr_frame.columnconfigure((0,1), weight = 1)

del_okt = ttk.Button(master=del_clr_frame, text='Del', command=delete_okt, bootstyle='warning-outline', takefocus=False, width=2) #Button
del_okt.grid(row=9, column=0, pady=10, sticky='ew')

clr_okt = ttk.Button(master=del_clr_frame, text='Clear', command=clear_okt, bootstyle='danger-outline', takefocus=False, width=2) #Button
clr_okt.grid(row=9, column=1, pady=10, sticky='ew')

# Frame Octal End ======================================================================================================


# Frame Hexadesimal ====================================================================================================
hex_frame = ttk.Frame(window, width=300, height=400, relief='raised', padding=10)
hex_frame.grid(row=2, column=4, sticky='nsew', padx=3)
hex_frame.columnconfigure((0,1,2,3,4), weight = 1)
hex_frame.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1)

label_hexa = ttk.Label(master=hex_frame, text='Hexadesimal', font=fontmedium, anchor='center', justify='center') #Label
label_hexa.grid(row=0, column=1, columnspan=3, sticky='nsew')

hex_entry_var = tk.StringVar()
hex_entry = ttk.Entry(master=hex_frame, font=fontmedium, width=10, textvariable=hex_entry_var) #Entry
hex_entry.grid(row=2, column=1, columnspan=3, sticky='ew',pady=10)

button_frame = tk.Frame(master=hex_frame, bg='black', width=200, height=200) #Button Frame
button_frame.grid(row=3, column=1, columnspan=3,rowspan=4, sticky='nsew')
button_frame.columnconfigure((0,1,2,3), weight = 1)
button_frame.rowconfigure((0,1,2,3), weight = 1)
width_setter = tk.Frame(master=button_frame, bg='black', width=300) #Width Setter
width_setter.grid(row=0, column=0, columnspan=4)
height_setter = tk.Frame(master=button_frame, bg='black', height=150) #Height Setter
height_setter.grid(row=0, column=0, rowspan=4)

hex_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
hex0 = hex1 = hex2 = hex3 = hex4 = hex5 = hex6 = hex7 = hex8 = hex9 = hexa = hexb = hexc = hexd = hexe = hexf = ttk.Button()

hex_btn_list = [hex0, hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9, hexa, hexb, hexc, hexd, hexe, hexf]

for i, button in enumerate(hex_symbol):
  hex_btn_list[i] = ttk.Button(master=button_frame, text=button, command=lambda i=i: hex_entry_button(hex_symbol[i]), bootstyle='primary-outline', takefocus=False) #Num Button
  hex_btn_list[i].grid(row=i//4, column=i%4, sticky='nsew', padx=5, pady=5)

conv_hex = ttk.Button(master=hex_frame, text='Convert', command=hex_entry_convert, bootstyle='success', takefocus=False, width=4) #Button 
conv_hex.grid(row=9, column=3, pady=10, sticky='ew', padx=5)


del_clr_frame = tk.Frame(master=hex_frame, height=10) #Empty Frame
del_clr_frame.grid(row=9, column=1, columnspan=2, sticky='ew', padx=5)
del_clr_frame.columnconfigure((0,1), weight = 1)

del_hex = ttk.Button(master=del_clr_frame, text='Del', command=delete_hex, bootstyle='warning-outline', takefocus=False, width=2) #Button
del_hex.grid(row=9, column=0, pady=10, sticky='ew')

clr_hex = ttk.Button(master=del_clr_frame, text='Clear', command=clear_hex, bootstyle='danger-outline', takefocus=False, width=2) #Button
clr_hex.grid(row=9, column=1, pady=10, sticky='ew')


# Frame Hexadesimal End =================================================================================================


# Frame How To ==================================================================================================
howto_frame = ttk.Frame(window, height=200, relief='raised', borderwidth=2, padding=10)
howto_frame.grid(row=3, column=1, columnspan=4, sticky='nsew', padx=3, pady=10)

howto = ttk.Label(master=howto_frame, text='Cara Menggunakan Program: ')
howto.place(x=0, y=0)

howto1 = ttk.Label(master=howto_frame, text='1. Masukkan angka yang ingin dikonversi ke dalam kolom yang tersedia. gunakan tombol yang tersedia untuk memasukkan angka.')
howto1.place(x=0, y=25)

howto2 = ttk.Label(master=howto_frame, text='2. Tekan tombol "Convert" untuk mengkonversi angka yang telah dimasukkan.')
howto2.place(x=0, y=50)

howto3 = ttk.Label(master=howto_frame, text='3. Hasil konversi akan muncul di kolom masing-masing sistem bilangan lain yang tersedia.')
howto3.place(x=0, y=75)

howto4 = ttk.Label(master=howto_frame, text='4. Untuk menghapus satu angka yang telah dimasukkan, tekan tombol "Del".')
howto4.place(x=0, y=100)

howto5 = ttk.Label(master=howto_frame, text='5. Untuk menghapus semua angka yang telah dimasukkan, tekan tombol "Clear". Tombol "Clear" juga akan mengaktifkan tombol yang dinonaktifkan.')
howto5.place(x=0, y=125)

# Frame Floating Point End ==============================================================================================

# Frame CopyRight =======================================================================================================
copy_frame = ttk.Frame(window,height=20, relief='raised', borderwidth=2, padding=10)
copy_frame.grid(row=4, column=1, columnspan=4, sticky='nsew', padx=3, pady=10, ipadx=0, ipady=0)

copy = ttk.Label(master=copy_frame, text='© 2023 Kelompok 6 TI08 - Hilmi Abdullah, Muhammad Ihsan, Surya Wijaya Rambe, Irham Syahputra', bootstyle='inverse-info')
copy.pack(side='top')



############################################################################################################




############################################################################################################
# Additional Functions


window.mainloop()