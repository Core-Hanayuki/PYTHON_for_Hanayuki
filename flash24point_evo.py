import tkinter as tk
s_l = ("+", "-", "*", "/")


def respawn(lii):
    pac_l_in = []
    for i in range(4):
        a = lii[i]
        for m in range(4):
            if m != i:
                b = lii[m]
                for n in range(4):
                    if n != i and n != m:
                        c = lii[n]
                        d = lii[6-i-m-n]
                        pac_l_in.append([a, b, c, d])
    return pac_l_in


def calc(li):
    exp_l_in = []
    s = 0
    while s < 64:
        exp = "{a}{s1}{b}{s2}{c}{s3}{d}".format(a=li[0], b=li[1], c=li[2], d=li[3],
                                                s1=s_l[int((s / 16) % 4)], s2=s_l[int(s / 4) % 4], s3=s_l[int(s % 4)])
        try:
            result = round(eval(exp), 10)
            if result == 24:
                exp_l_in.append(exp)
        except ZeroDivisionError:
            pass
        s += 1
    s = 0
    while s < 64:
        exp = "({a}{s1}{b}){s2}{c}{s3}{d}".format(a=li[0], b=li[1], c=li[2], d=li[3],
                                                  s1=s_l[int((s / 16) % 4)], s2=s_l[int(s / 4) % 4], s3=s_l[int(s % 4)])
        try:
            result = round(eval(exp), 10)
            if result == 24:
                exp_l_in.append(exp)
        except ZeroDivisionError:
            pass
        s += 1
    s = 0
    while s < 64:
        exp = "{a}{s1}({b}{s2}{c}){s3}{d}".format(a=li[0], b=li[1], c=li[2], d=li[3],
                                                  s1=s_l[int((s / 16) % 4)], s2=s_l[int(s / 4) % 4], s3=s_l[int(s % 4)])
        try:
            result = round(eval(exp), 10)
            if result == 24:
                exp_l_in.append(exp)
        except ZeroDivisionError:
            pass
        s += 1
    s = 0
    while s < 64:
        exp = "{a}{s1}{b}{s2}({c}{s3}{d})".format(a=li[0], b=li[1], c=li[2], d=li[3],
                                                  s1=s_l[int((s / 16) % 4)], s2=s_l[int(s / 4) % 4], s3=s_l[int(s % 4)])
        try:
            result = round(eval(exp), 10)
            if result == 24:
                exp_l_in.append(exp)
        except ZeroDivisionError:
            pass
        s += 1
    s = 0
    while s < 64:
        exp = "({a}{s1}{b}{s2}{c}){s3}{d}".format(a=li[0], b=li[1], c=li[2], d=li[3],
                                                  s1=s_l[int((s / 16) % 4)], s2=s_l[int(s / 4) % 4], s3=s_l[int(s % 4)])
        try:
            result = round(eval(exp), 10)
            if result == 24:
                exp_l_in.append(exp)
        except ZeroDivisionError:
            pass
        s += 1
    s = 0
    while s < 64:
        exp = "{a}{s1}({b}{s2}{c}{s3}{d})".format(a=li[0], b=li[1], c=li[2], d=li[3],
                                                  s1=s_l[int((s / 16) % 4)], s2=s_l[int(s / 4) % 4], s3=s_l[int(s % 4)])
        try:
            result = round(eval(exp), 10)
            if result == 24:
                exp_l_in.append(exp)
        except ZeroDivisionError:
            pass
        s += 1
    return exp_l_in


def sim():
    txt.delete(0.0, 'end')
    exp_l = []
    fi = en1.get()
    se = en2.get()
    th = en3.get()
    fo = en4.get()
    num_l = [fi, se, th, fo]
    try:
        for L in respawn(num_l):
            exp_l = exp_l + calc(L)
    except:
        txt.insert('end', 'Unexpected variables.\n')
        return 0
    if len(exp_l) == 0:
        txt.insert('end', 'Do Not Exist.\n')
    else:
        txt.insert('end', 'Solution: \n')
        for p in set(exp_l):
            txt.insert('end', chars=p + ' = 24\n')


def clr():
    en1.delete(0, 'end')
    en2.delete(0, 'end')
    en3.delete(0, 'end')
    en4.delete(0, 'end')


sub = tk.Tk()
sub.title('Flash 24Point Evolution')
sub.geometry('640x360')

en1 = tk.Entry(sub)
en1.place(relx=0.125, rely=0.1, width=70, height=50)
en2 = tk.Entry(sub)
en2.place(relx=0.25, rely=0.1, width=70, height=50)
en3 = tk.Entry(sub)
en3.place(relx=0.375, rely=0.1, width=70, height=50)
en4 = tk.Entry(sub)
en4.place(relx=0.5, rely=0.1, width=70, height=50)

la = tk.Label(sub, text='在上方输入4个数并点击“计算”，结果会显示在下方 :)', font=('Microsoft YaHei', 14))
la.place(relx=0.1, rely=0.3)

butc = tk.Button(sub, text='清空', font=('仿宋', 12), command=clr, activebackground='#e2d849')
butc.place(relx=0.04, rely=0.1, width=40, height=50)
but = tk.Button(sub, text='计算', font=('仿宋', 15), command=sim, activebackground='#83CBAC')
but.place(relx=0.7, rely=0.1, width=110, height=50)

txt = tk.Text(sub, font=('Arial', 13))
txt.place(relx=0.1, rely=0.4, width=500, height=200)
scroll = tk.Scrollbar()
scroll.pack(side='right', fill='y')
scroll.config(command=txt.yview)
txt.config(yscrollcommand=scroll.set)


sub.mainloop()
