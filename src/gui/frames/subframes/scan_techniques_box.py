import customtkinter
import tkinter
import os
from PIL import Image
from constants.constants import (
    W
)
from data.net_scan_data import (
    scan_techniques
) 

class ScanTechniquesBox(customtkinter.CTkScrollableFrame):
    def __init__(self, master, args_list=None, checkbox_list=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.command = command
        self.names_list = list(scan_techniques.keys())
        self.values_list = list(scan_techniques.values())
        self.checkbox_list = checkbox_list # gui - displays keys()
        self.args_list = args_list if args_list is not None else [] 
        

        # style config 
        self.grid(row=1, column=2, padx=(20, 0), pady=(20, 0))

        for i, item in enumerate(self.names_list):
            self.add_item(item, self.values_list[i])

    def add_item(self, item, other_value):
        var = tkinter.StringVar()
        var.set(other_value)

        self.checkbox = customtkinter.CTkCheckBox(self, text=item, variable=var, onvalue=1, offvalue=0,
                                                  command=lambda value=var.get(): self.checkbox_command(value))
        self.checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10), sticky='w')
        self.checkbox_list.append(self.checkbox)

    def checkbox_command(self, value):
        if self.command is not None:
            on_value = self.checkbox._onvalue
            off_value = self.checkbox._offvalue
            index = self.values_list.index(value)
            xindex = self.values_list[index]

            if on_value == 1 and xindex not in self.args_list:
                self.args_list.append(xindex)
            elif off_value == 0 and xindex in self.args_list:
                self.args_list.remove(xindex)

            print("Updated args_list:", self.args_list)
            self.update_checkbox_args_list()
            self.command()  # Call the command to update ArgsHandler

    def update_checkbox_args_list(self):
        self.master.checkbox_args_list = self.args_list
        print("MASTER ARGS LIST in ScanTechniquesBox OBJ:", self.master.checkbox_args_list)
       



    