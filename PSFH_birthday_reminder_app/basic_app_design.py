"""
    A tkinter app which display the remaining days for a
    given date string and a pre specified birthday string.
"""

import os
import tkinter as tk
from datetime import datetime
from utils_and_functions import date_set_generator, main_func, check_valid_date


class App:
    def __init__(self, main):
        self.master = main

    def add_label(self, msg, rrr, ccc):
        self.label = tk.Label(self.master, text=msg, padx=40, pady=10)
        self.label["borderwidth"] = 2
        self.label["relief"] = "flat"
        self.label.configure(anchor=tk.W)
        self.label["background"] = "white"
        self.label.grid(row=rrr, column=ccc, sticky="nsew")
        # self.label.pack()

    def add_text_box(self, msg, rrr, ccc):
        self.text = tk.Text(self.master)
        self.text.insert(tk.END, msg)
        self.text.grid(row=rrr, column=ccc, sticky="nsew")

    def column_frame(self, message, nrow):
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=nrow, column=0, sticky="nsew")
        self.column = 5
        for col in range(self.column):
            self.add_label(message[col], nrow, col)


# Main starts from here
if __name__ == "__main__":
    print("""Welcome to the Birthday Reminder App. Birthday you would not like to forget!!
Please type END to exit..\n""")

    while True:
	# Take birthday string input
        try:
            birthstr = input("Enter Birthday [Format -> dd/mm/yyyy]: ")
        except Exception:
            birthstr = "29/05/2020"
        finally:
            if birthstr.upper() == "END":
                break
            else:
                birthstr = birthstr[:-4] + str(datetime.now().year)
            # check if the date is valid
            if not check_valid_date(birthstr):
                print("Invalid date. Try again!")
                continue

	# generate set of dates
        date_set_generator(birthstr)

        root = tk.Tk()
        root.title("Birthday App")

        heading = tk.Frame(root, width=1100, height=20)
        heading.grid(row=0, column=0, sticky="nsew")

        headingApp = App(heading)
        head_list = (" " * 15, "Date              ", "Weekday    ",
                "Today                          ", " " * 43)
        headingApp.column_frame(head_list, 0)

        canvas = tk.Canvas(root)
        canvas.grid(row=1, column=0, sticky=tk.N)

        yscroll = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
        yscroll.grid(row=1, column=1, sticky=tk.N + tk.S)

        winframe = tk.Frame(canvas)
        winframe.grid(row=0, column=0, sticky=tk.N)

        BirthdayApp = App(winframe)

        with open("dataset.txt") as FH:
            header = next(FH)
            all_dates = list()
            for line in FH:
                date = line.split(",")
                if len(date) == 1:
                    # unwanted "\n"
                    date = date[0][:-1]
                else:
                    date = date[0]
                all_dates.append(date)
		
        message_list = list()
        for date in all_dates:
            message_list.append(main_func(date, birthstr))

        rows = len(all_dates)
        for row in range(rows):
            BirthdayApp.column_frame(message_list[row], row)

        canvas.create_window(0, 0, anchor='center', window=winframe)
        canvas.update_idletasks()

        canvas.config(scrollregion=canvas.bbox('all'), yscrollcommand=yscroll.set)

        root.update()

        canvas.config(width=1100, height=1000)

        canvas.yview_moveto(0)

        """
            Adding mouse scroll for the window.
            Doesn't work for all laptop touchpads
        """

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def _bound_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)

        canvas.bind("<Enter>", _bound_to_mousewheel)

        root.mainloop()

	# delete previous set of dates
        os.system(r"rm dataset.txt")

