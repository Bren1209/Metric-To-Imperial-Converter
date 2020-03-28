import tkinter as tk
from time import sleep



def top_val_err():
    global top_label
    top_label.destroy()
    top_label = tk.Label(master, text='Please enter a valid number')
    top_label.config(fg='red', font=30)
    canvas1.create_window(200, 90, window=top_label)


def bot_val_err():
    global bot_label
    bot_label.destroy()
    bot_label = tk.Label(master, text='Please enter a vaild number')
    bot_label.config(fg='red', font=30)
    canvas1.create_window(200, 180, window=bot_label)


def convert_kg_lbs():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            kg = float(entry1.get())
            kg_to_lbs = round((kg * 2.204), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{kg_to_lbs} Lbs')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            lbs = float(entry2.get())
            lbs_to_kg = round((lbs / 2.204), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{lbs_to_kg} Kg')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window=bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()


def convert_km_mi():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            km = float(entry1.get())
            km_to_mi = round((km * 0.621), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{km_to_mi} Mi')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            mi = float(entry2.get())
            mi_to_km = round((mi / 0.621), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{mi_to_km} Km')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window=bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()


def convert_m_ft():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            m = float(entry1.get())
            m_to_ft = round((m * 3.28), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{m_to_ft} Ft')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            ft = float(entry2.get())
            ft_to_m = round((ft / 3.28), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{ft_to_m} M')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window = bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()


def convert_m_y():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            m = float(entry1.get())
            m_to_y = round((m * 1.093), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{m_to_y} Yd')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            y = float(entry2.get())
            y_to_m = round((y / 1.093), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{y_to_m} M')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window=bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()


def convert_cm_in():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            cm = float(entry1.get())
            cm_to_inch = round((cm * 0.397), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{cm_to_inch} in')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            inch = float(entry2.get())
            inch_to_cm = round((inch / 0.397), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{inch_to_cm} cm')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window = bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()


def convert_g_oz():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            g = float(entry1.get())
            g_to_oz = round((g * 0.035), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{g_to_oz} oz')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            oz = float(entry2.get())
            oz_to_g = round((oz / 0.035), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{oz_to_g} g')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window=bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()


def convert_temp():

    global top_label
    global bot_label

    try:
        if len(str(entry1.get())) > 0:
            c = float(entry1.get())
            c_to_f = round(((c * (9/5)) + 32), 1)
            top_label.destroy()
            top_label = tk.Label(master, text=f'{c_to_f} F')
            top_label.config(font=40)
            canvas1.create_window(200, 90, window=top_label)
        else:
            pass
    except ValueError:
        top_val_err()

    try:
        if len(str(entry2.get())) > 0:
            f = float(entry2.get())
            f_to_c = round(((f - 32) * (5/9)), 1)
            bot_label.destroy()
            bot_label = tk.Label(master, text=f'{f_to_c} C')
            bot_label.config(font=40)
            canvas1.create_window(200, 180, window=bot_label)
        else:
            pass
    except ValueError:
        bot_val_err()

###################################################################


master = tk.Tk()

canvas1 = tk.Canvas(master, width=400, height=240)
canvas1.pack()
master.title('Unit Converter')

label1 = tk.Label(master, text='Enter Metric value: ')
label2 = tk.Label(master, text='Enter Imperial value: ')
top_label = tk.Label(master, text='0')
bot_label = tk.Label(master, text='0')

entry1 = tk.Entry(master)
entry2 = tk.Entry(master)

but_quit = tk.Button(master, text='Quit', command=master.quit)
but_mass1 = tk.Button(master, text='Kg <> Lbs', command=convert_kg_lbs)
but_mass2 = tk.Button(master, text='g <> oz', command=convert_g_oz)
but_dist1 = tk.Button(master, text='Km <> Mi', command=convert_km_mi)
but_dist2 = tk.Button(master, text='M <> Ft', command=convert_m_ft)
but_dist3 = tk.Button(master, text='M <> Yd', command=convert_m_y)
but_dist4 = tk.Button(master, text='cm <> in', command=convert_cm_in)
but_temp = tk.Button(master, text='C <> F', command=convert_temp)

canvas1.create_window(200, 30, window=label1)
canvas1.create_window(200, 60, window=entry1)
canvas1.create_window(200, 120, window=label2)
canvas1.create_window(200, 150, window=entry2)
canvas1.create_window(200, 220, window=but_quit)
canvas1.create_window(60, 30, window=but_mass1)
canvas1.create_window(60, 60, window=but_mass2)
canvas1.create_window(60, 90, window=but_dist1)
canvas1.create_window(60, 120, window=but_dist2)
canvas1.create_window(60, 150, window=but_dist3)
canvas1.create_window(60, 180, window=but_dist4)
canvas1.create_window(60, 210, window=but_temp)


master.mainloop()
