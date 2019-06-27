import tkinter

# Creates window.
window = tkinter.Tk()
window.title("BinCalc")

# Creates frames inside window.
top_frame = tkinter.Frame(window)
top_frame.pack()
mode_frame = tkinter.Frame(window)
mode_frame.pack()
entry_frame = tkinter.Frame(window)
entry_frame.pack(pady = 5)
results1_frame = tkinter.Frame(window)
results1_frame.pack()
results2_frame = tkinter.Frame(window)
results2_frame.pack()
results3_frame = tkinter.Frame(window)
results3_frame.pack()
error_frame = tkinter.Frame(window)
error_frame.pack()

# Variables.
mode = tkinter.StringVar()
q = tkinter.StringVar()
x = tkinter.StringVar()
y = tkinter.StringVar()
z = tkinter.StringVar()
error = tkinter.StringVar()


# Function to set mode to decimal.
def set_mode_dec():
    global mode
    mode.set("DEC")
    button1.configure(background = "light grey")
    button2.configure(background = "SystemButtonFace")
    button3.configure(background = "SystemButtonFace")
    reset()


# Function to set mode to binary.
def set_mode_bin():
    global mode
    mode.set("BIN")
    button1.configure(background = "SystemButtonFace")
    button2.configure(background = "light grey")
    button3.configure(background = "SystemButtonFace")
    reset()


# Function to set mode to hexadecimal.
def set_mode_hex():
    global mode
    mode.set("HEX")
    button1.configure(background = "SystemButtonFace")
    button2.configure(background = "SystemButtonFace")
    button3.configure(background = "light grey")
    reset()


# Function to call when GO button is pressed.
def button_go(event=None):
    if mode.get() == "DEC":
        if int(q.get()) < 256:
            dec_go()
        else:
            inv_num()
    elif mode.get() == "BIN":
        if int(q.get()) < 11111112:
            if len(q.get()) == 8:
                bin_go()
            else:
                inv_num()
        else:
            inv_num()
    elif mode.get() == "HEX":
        if len(q.get()) > 2:
            inv_num()
        else:
            hex_go()


# Function to convert decimal to binary and hexadecimal.
def dec_go():
    global x
    global y
    global z
    x.set(q.get())
    y.set(str(bin(int(q.get())))[slice(2, 10)])
    z.set(str.upper(hex(int(q.get())))[2:4])
    entry1.delete(0, 'end')
    error.set("")


# Function to convert binary to decimal and hexadecimal.
def bin_go():
    global x
    global y
    global z
    x.set(int(q.get(), 2))
    y.set(q.get())
    z.set(str.upper(hex(int(q.get(), 2)))[2:4])
    entry1.delete(0, 'end')
    error.set("")


# Function to convert hexadecimal to decimal and binary.
def hex_go():
    global x
    global y
    global z
    x.set(int(q.get(), 16))
    y.set(str(bin(int(q.get(), 16)))[slice(2, 10)])
    z.set(q.get().upper())
    entry1.delete(0, 'end')
    error.set("")


# Function to display error message on invalid input.
def inv_num():
    entry1.delete(0, 'end')
    error.set("Invalid number!")
    x.set("")
    y.set("")
    z.set("")


# Function to clear inputs.
def reset():
    entry1.delete(0, 'end')
    x.set("")
    y.set("")
    z.set("")
    error.set("")


# Buttons, labels, entry widgets.
button1 = tkinter.Button(top_frame, text = "DEC", fg = "blue", width = "10", command = set_mode_dec)
button1.pack(side = "left")
button2 = tkinter.Button(top_frame, text = "BIN", fg = "red", width = "10", command = set_mode_bin)
button2.pack(side = "left")
button3 = tkinter.Button(top_frame, text = "HEX", fg = "green", width = "10", command = set_mode_hex)
button3.pack(side = "left")

# label10 = tkinter.Label(mode_frame, text = "MODE: ").pack(side = "left")
# label11 = tkinter.Label(mode_frame, textvariable = mode).pack(side = "left")

label1 = tkinter.Label(entry_frame, text = "Enter number:").pack()
entry1 = tkinter.Entry(entry_frame, fg = "black", textvariable = q)
entry1.pack()
entry1.bind("<Return>", button_go)

button4 = tkinter.Button(entry_frame, text = "GO", width = 10, command = button_go).pack(pady = 5)

label2 = tkinter.Label(results1_frame, text = "DECIMAL: ", font=(None, 10, "bold")).pack(side = "left", pady = 5)
label3 = tkinter.Label(results1_frame, fg = "red", textvariable = x, font=(None, 10, "bold")).pack(pady = 5)
label4 = tkinter.Label(results2_frame, text = "BINARY: ", font=(None, 10, "bold")).pack(side = "left", pady = 5)
label5 = tkinter.Label(results2_frame, fg = "red", textvariable = y, font=(None, 10, "bold")).pack(pady = 5)
label6 = tkinter.Label(results3_frame, text = "HEXADECIMAL: ", font=(None, 10, "bold")).pack(side = "left", pady = 5)
label7 = tkinter.Label(results3_frame, fg = "red", textvariable = z, font=(None, 10, "bold")).pack(pady = 5)

labelerror = tkinter.Label(error_frame, fg = "red", textvariable = error).pack()


window.mainloop()
