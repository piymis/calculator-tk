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
        self.init_ui()
    
    def init_ui(self):
        self.pack(fill=BOTH, expand=True)
        
        # Text entry area 
        self.entry_area = ttk.Entry(self, width=50)
        self.entry_area.grid(row=0, columnspan=4)
        
        # ----- 1st Row -----
        self.button7 = ttk.Button(self, text="7").grid(row=1, column=0)
        self.button8 = ttk.Button(self, text="8").grid(row=1, column=1)
        self.button9 = ttk.Button(self, text="9").grid(row=1, column=2)
        self.button_div = ttk.Button(self, text="/").grid(row=1, column=3)
        
        # ----- 2nd Row -----
        self.button4 = ttk.Button(self, text="4").grid(row=2, column=0)
        self.button5 = ttk.Button(self, text="5").grid(row=2, column=1)
        self.button6 = ttk.Button(self, text="6").grid(row=2, column=2)
        self.button_mul = ttk.Button(self, text="*").grid(row=2, column=3)
        
        # ----- 3rd Row -----
        self.button1 = ttk.Button(self, text="1").grid(row=3, column=0)
        self.button2 = ttk.Button(self, text="2").grid(row=3, column=1)
        self.button3 = ttk.Button(self, text="3").grid(row=3, column=2)
        self.button_add = ttk.Button(self, text="+").grid(row=3, column=3)
        
        # ----- 4th Row -----
        self.button_ac = ttk.Button(self, text="AC").grid(row=4, column=0)
        self.button0 = ttk.Button(self, text="0").grid(row=4, column=1)
        self.button_eq = ttk.Button(self, text="=").grid(row=4, column=2)
        self.button_sub = ttk.Button(self, text="-").grid(row=4, column=3)

root = Tk()
calculator = Calculator(root)
root.geometry("400x400")
root.mainloop()