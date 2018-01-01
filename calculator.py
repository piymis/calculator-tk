#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 03:23:31 2017

@author: piyush
"""
from tkinter import *
from tkinter import ttk


class Calculator(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.first_val = ""
        self.init_ui()

    def init_ui(self):
        self.pack(fill=BOTH, expand=True)
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 12",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 14",
                        padding=10)
        # Text entry area
        self.entry_area = ttk.Entry(self, width=55)
        self.entry_area.grid(row=0, columnspan=4)

        # ----- 1st Row -----
        self.button7 = ttk.Button(self, text="7",
            command=lambda: self.number_press("7")).grid(row=1, column=0)
        self.button8 = ttk.Button(self, text="8",
            command=lambda: self.number_press("8")).grid(row=1, column=1)
        self.button9 = ttk.Button(self, text="9",
            command=lambda: self.number_press("9")).grid(row=1, column=2)
        self.button_div = ttk.Button(self, text="/",
            command=lambda: self.math_press("/")).grid(row=1, column=3)

        # ----- 2nd Row -----
        self.button4 = ttk.Button(self, text="4",
            command=lambda: self.number_press("4")).grid(row=2, column=0)
        self.button5 = ttk.Button(self, text="5",
            command=lambda: self.number_press("5")).grid(row=2, column=1)
        self.button6 = ttk.Button(self, text="6",
            command=lambda: self.number_press("6")).grid(row=2, column=2)
        self.button_mul = ttk.Button(self, text="*",
            command=lambda: self.math_press("*")).grid(row=2, column=3)

        # ----- 3rd Row -----
        self.button1 = ttk.Button(self, text="1",
            command=lambda: self.number_press("1")).grid(row=3, column=0)
        self.button2 = ttk.Button(self, text="2",
            command=lambda: self.number_press("2")).grid(row=3, column=1)
        self.button3 = ttk.Button(self, text="3",
            command=lambda: self.number_press("3")).grid(row=3, column=2)
        self.button_add = ttk.Button(self, text="+",
            command=lambda: self.math_press("+")).grid(row=3, column=3)

        # ----- 4th Row -----
        self.button_ac = ttk.Button(self, text="AC",
            command=lambda: self.clear_press()).grid(row=4, column=0)
        self.button0 = ttk.Button(self, text="0",
            command=lambda: self.number_press("0")).grid(row=4, column=1)
        self.button_eq = ttk.Button(self, text="=",
            command=lambda: self.equal_press()).grid(row=4, column=2)
        self.button_sub = ttk.Button(self, text="-",
            command=lambda: self.math_press("-")).grid(row=4, column=3)

    def number_press(self, value):
        entry_val = self.entry_area.get()
        entry_val += value
        self.entry_area.delete(0, "end")
        self.entry_area.insert(0, entry_val)

    def clear_press(self):
        self.entry_area.delete(0, "end")
        self.first_val = ""

    def math_press(self, value):
        self.first_val = self.entry_area.get()
        self.add_flag = False
        self.sub_flag = False
        self.mul_flag = False
        self.div_flag  = False
        if value == "+":
            self.add_flag = True
        elif value == "-":
            self.sub_flag = True
        elif value == "*":
            self.mul_flag = True
        else:
            self.div_flag = True
        self.entry_area.delete(0, "end")

    def equal_press(self):
        if self.add_flag:
            output = float(self.first_val) + float(self.entry_area.get())
        elif self.sub_flag:
            output = float(self.first_val) - float(self.entry_area.get())
        elif self.mul_flag:
            output = float(self.first_val) * float(self.entry_area.get())
        elif self.div_flag:
            output = float(self.first_val) / float(self.entry_area.get())

        self.entry_area.delete(0, "end")
        self.entry_area.insert(0, str(output))

root = Tk()
calculator = Calculator(root)
root.geometry("460x220")
root.mainloop()
