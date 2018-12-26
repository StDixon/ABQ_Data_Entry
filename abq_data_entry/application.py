#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:33:07 2018

@author: sdixon
"""

import tkinter as tk
from tkinter import ttk

from datetime import datetime

from . import views as v
from . import models as m

class Application(tk.Tk):
    """Application root window"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("ABQ Data Entry Application")
        self.resizable(width=False, height=False)
        
        ttk.Label(self,
                  text="ABQ Data Entry Application",
                  font=("TkDefaultFont", 16)
                  ).grid(row=0)
        
        # Form
        self.recordform = v.DataRecordForm(self)
        self.recordform.grid(row=1, padx=10)
        
        self.savebutton = ttk.Button(self, text="Save",
                                     command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2, padx=10)
        
        # Status Bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)
        
        self.records_saved = 0
        
    def on_save(self):
        
        """Handles save button clicks"""
        errors = self.recordform.get_errors()
        if errors:
            self.status.set(
                    "Cannot save, errors in fields: {}"
                    .format(','.join(errors.keys())))
            return False
        
        #for now a hardcoded filename
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "abq_data_record_{}.csv".format(datestring)
        model = m.CSVModel(filename)
                
        data=self.recordform.get()
        
        model.save_record(data)
            
        self.records_saved += 1
        self.status.set(
                "{} records saved this session".format(self.records_saved))
        
        self.recordform.reset()
