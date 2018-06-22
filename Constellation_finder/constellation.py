from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter import messagebox


class Constellation:

    def __init__(self, root):
        global constellation
        constellation = {1.20: 'Aquarius',
                         2.19: 'Pisces',
                         3.21: 'Aries',
                         4.20: 'Taurus',
                         5.21: 'Gemini',
                         6.22: 'Cancer',
                         7.23: 'Leo',
                         8.23: 'Virgo',
                         9.23: 'Libra',
                         10.24: 'Scorpio',
                         11.22: 'Sagittarius',
                         12.22: 'Capricornus'}
        global today
        today = date.today().month + date.today().day * 0.01
        global is_start
        is_start = True

        def start():
            global today
            global is_start

            if not is_start:
                self.frame.destroy()

            root.resizable(False, False)
            root.title('Constellation v1.0')
            root.configure(background='#232949')

            self.frame = Frame(root, background='#232949')
            self.frame.pack()

            self.title_photo = PhotoImage(file='Constellation/title.gif')
            self.bg1 = PhotoImage(file='Constellation/bg1.gif', height=580)
            self.bg2 = PhotoImage(file='Constellation/bg2.gif', height=580)
            self.find = PhotoImage(file='Constellation/find.gif').subsample(3, 3)
            self.all = PhotoImage(file='Constellation/all.gif').subsample(3, 3)

            ttk.Label(self.frame, image=self.title_photo, background='#232949').grid(row=0, column=0, columnspan=3)
            ttk.Label(self.frame, image=self.bg1, background='#232949').grid(row=1, column=0, rowspan=3)
            ttk.Label(self.frame, image=self.bg2, background='#232949').grid(row=1, column=2, rowspan=3)

            ttk.Button(self.frame, image=self.all, command=first).grid(row=1, column=1)
            ttk.Button(self.frame, image=self.find, command=second).grid(row=2, column=1)

            for i in constellation:
                if today >= 12.22 or today < 1.20:
                    name = 'Capricornus'
                    break
                if today < i:
                    break
                name = constellation[i]

            self.today_pic = PhotoImage(file='Constellation/'+name+'.gif').subsample(1, 1)
            ttk.Label(self.frame, background='#232949', image=self.today_pic, text='Constellation of Today:\n'+name,
                      foreground='#81ABEC', compound='bottom', font=('Harrington', 18), justify='center')\
                .grid(row=3, column=1)

        def first():
            global is_start
            is_start = False

            self.frame.destroy()
            self.frame = Frame(root, bg='#232949')
            self.frame.pack()

            self.c1 = PhotoImage(file='Constellation/Aquarius1.gif').subsample(2, 2)
            self.c2 = PhotoImage(file='Constellation/Pisces1.gif').subsample(2, 2)
            self.c3 = PhotoImage(file='Constellation/Aries1.gif').subsample(2, 2)
            self.c4 = PhotoImage(file='Constellation/Taurus1.gif').subsample(2, 2)
            self.c5 = PhotoImage(file='Constellation/Gemini1.gif').subsample(2, 2)
            self.c6 = PhotoImage(file='Constellation/Cancer1.gif').subsample(2, 2)
            self.c7 = PhotoImage(file='Constellation/Leo1.gif').subsample(2, 2)
            self.c8 = PhotoImage(file='Constellation/Virgo1.gif').subsample(2, 2)
            self.c9 = PhotoImage(file='Constellation/Libra1.gif').subsample(2, 2)
            self.c10 = PhotoImage(file='Constellation/Scorpio1.gif').subsample(2, 2)
            self.c11 = PhotoImage(file='Constellation/Sagittarius1.gif').subsample(2, 2)
            self.c12 = PhotoImage(file='Constellation/Capricornus1.gif').subsample(2, 2)
            self.back = PhotoImage(file='Constellation/back.gif').subsample(3, 3)

            ttk.Button(self.frame, image=self.c1, command=lambda: show_constellation('Aquarius'), text='Aquarius',
                       compound=BOTTOM).grid(row=0, column=0, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c2, command=lambda: show_constellation('Pisces'), text='Pisces',
                       compound=BOTTOM).grid(row=0, column=1, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c3, command=lambda: show_constellation('Aries'), text='Aries',
                       compound=BOTTOM).grid(row=0, column=2, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c4, command=lambda: show_constellation('Taurus'), text='Taurus',
                       compound=BOTTOM).grid(row=0, column=3, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c5, command=lambda: show_constellation('Gemini'), text='Gemini',
                       compound=BOTTOM).grid(row=1, column=0, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c6, command=lambda: show_constellation('Cancer'), text='Cancer',
                       compound=BOTTOM).grid(row=1, column=1, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c7, command=lambda: show_constellation('Leo'), text='Leo',
                       compound=BOTTOM).grid(row=1, column=2, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c8, command=lambda: show_constellation('Virgo'), text='Virgo',
                       compound=BOTTOM).grid(row=1, column=3, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c9, command=lambda: show_constellation('Libra'), text='Libra',
                       compound=BOTTOM).grid(row=2, column=0, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c10, command=lambda: show_constellation('Scorpio'), text='Scorpio',
                       compound=BOTTOM).grid(row=2, column=1, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c11, command=lambda: show_constellation('Sagittarius'),
                       text='Sagittarius', compound=BOTTOM).grid(row=2, column=2, padx=50, pady=25)
            ttk.Button(self.frame, image=self.c12, command=lambda: show_constellation('Capricornus'),
                       text='Capricornus', compound=BOTTOM).grid(row=2, column=3, padx=50, pady=25)

            ttk.Button(self.frame, image=self.back, command=start).grid(row=3, column=0)

        def second():
            global constellation
            global is_start
            is_start = False

            def get_constellation():
                try:
                    if birth_date.get() not in range(1, 32) or birth_month.get() not in range(1, 13):
                        raise ValueError

                    select_date = int(month_spin.get()) + int(date_combo.get()) * 0.01
                    for i in constellation:
                        if select_date >= 12.22 or select_date < 1.20:
                            name = 'Capricornus'
                            break
                        if select_date < i:
                            break
                        name = constellation[i]
                    show_constellation(name)
                except ValueError:
                    messagebox.showinfo(title='Nah',
                                        message='You need select your birthday date')

            self.frame.destroy()
            self.frame = Frame(root, bg='#232949')
            self.frame.pack()

            self.back = PhotoImage(file='Constellation/back.gif').subsample(3, 3)
            self.submit = PhotoImage(file='Constellation/submit.gif').subsample(4, 4)

            birth_month = IntVar()
            birth_date = IntVar()

            month_spin = Spinbox(self.frame, textvariable=birth_month, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
            month_spin.grid(row=1, column=0, padx=20, pady=20)

            date_list = list(range(1, 32))
            date_combo = ttk.Combobox(self.frame, values=date_list, textvariable=birth_date)
            date_combo.grid(row=1, column=1, padx=20, pady=20)

            ttk.Button(self.frame, image=self.submit, command=get_constellation).grid(row=1, column=2, padx=20, pady=40)
            ttk.Button(self.frame, image=self.back, command=start).grid(row=2, column=0, columnspan=3, padx=40)

            ttk.Label(self.frame, text='Birthday Month', foreground='#81ABEC', background='#232949',
                      font=('Harrington', 15)).grid(row=0, column=0)
            ttk.Label(self.frame, text='Birthday Date', foreground='#81ABEC', background='#232949',
                      font=('Harrington', 15)).grid(row=0, column=1)

        def show_constellation(choice):
            global is_start
            is_start = False

            self.frame.destroy()
            self.frame = Frame(root, bg='#232949')
            self.frame.pack()

            f = open('Constellation/Leo.txt', 'r')
            content = f.read()
            f.close()

            ttk.Label(self.frame, text=content, background='#232949', foreground='#81ABEC', font=('Harrington', 15))\
                .grid(row=0, column=1, rowspan=2, columnspan=3)

            self.choose_photo = PhotoImage(file='Constellation/'+choice+'.gif')
            self.find = PhotoImage(file='Constellation/find.gif').subsample(4, 4)
            self.all = PhotoImage(file='Constellation/all.gif').subsample(4, 4)
            self.back = PhotoImage(file='Constellation/back.gif').subsample(4, 4)

            ttk.Label(self.frame, text=choice, image=self.choose_photo, compound=BOTTOM, background='#232949',
                      foreground='#81ABEC', font=('Harrington', 40)).grid(row=0, column=0)

            ttk.Button(self.frame, image=self.back, command=start).grid(row=1, column=0, pady=10)

            ttk.Button(self.frame, image=self.all, command=first).grid(row=1, column=1, pady=10)
            ttk.Button(self.frame, image=self.find, command=second).grid(row=1, column=2, pady=10)

        start()


def main():
    root = Tk()
    constellation = Constellation(root)
    root.mainloop()


if __name__ == '__main__':
    main()
