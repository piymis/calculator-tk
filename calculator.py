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
        entry_area = ttk.Entry(self)
        entry_area.grid(row=0, column=0, columnspan=8)
        

root = Tk()
calculator = Calculator(root)
root.geometry("400x400")
root.mainloop()