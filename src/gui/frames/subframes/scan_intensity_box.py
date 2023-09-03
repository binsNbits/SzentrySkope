import customtkinter
import tkinter
from constants.constants import (
    CORNER_RADIUS_0, TRANSPARENT, GRID_ROW_1, GRID_COL_1, PADX_1, PADY_1, NSEW, EW, 
    PADY_2, GRID_COL_0, GRID_ROW_0 
)
from constants.net_scan_gui_const import (
    SCAN_1_INT, SCAN_2_INT, SCAN_3_INT
)

class ScanIntensityBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=GRID_COL_1, padx=(PADX_1, 0), pady=(PADY_1, 0), sticky=NSEW)

        # config style
        self._corner_radius = CORNER_RADIUS_0
        self.fg_color = TRANSPARENT
        
        self.previous_value = ""
        self.seg_var = tkinter.StringVar(value=SCAN_1_INT)

        # create segmented button 1
        '''elf.seg_button_1 = customtkinter.CTkSegmentedButton(self, variable=self.seg_var, command=self.show_present_silder)
        self.seg_button_1.grid(row=GRID_ROW_0, column=GRID_COL_0, padx=(PADX_1, 10), pady=(PADY_2, 10), sticky=EW)
        self.seg_button_1.configure(values=[SCAN_1_INT, SCAN_2_INT, SCAN_3_INT])
        self.seg_button_1.set(value=1)'''
        
        
        self.slider_1 = customtkinter.CTkSlider(self, from_=0, to=5, number_of_steps=5)
        self.slider_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1.set(0)
        self.slider_1.bind("<B1-Motion>", lambda event: self.on_slider_move(self.slider_1.get()))
        self.stealth_label = customtkinter.CTkLabel(self, text="Stealth")
        self.stealth_label.grid(row=1, column=0, padx=(10, 10), pady=(1, 1), sticky="ns")
        
        self.slider_2 = customtkinter.CTkSlider(self, from_=0, to=9,number_of_steps=9)
        self.slider_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2.set(0)
        self.slider_2.bind("<B1-Motion>", lambda event: self.on_slider_move(self.slider_2.get()))
        self.aggression_label = customtkinter.CTkLabel(self, text="Aggression")
        self.aggression_label.grid(row=2, column=0, padx=(10, 10), pady=(1, 1), sticky="ns")

        self.slider_3 = customtkinter.CTkSlider(self, from_=0, to=9,number_of_steps=9)
        self.slider_3.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_3.set(0)
        self.slider_3.bind("<B1-Motion>", lambda event: self.on_slider_move(self.slider_3.get()))
        self.evasion_label = customtkinter.CTkLabel(self, text="Evasion")
        self.evasion_label.grid(row=3, column=0, padx=(10, 10), pady=(1, 1), sticky="ns")

    def on_slider_move(self, value):
        if value != self.previous_value:            #print("Slider value:", value)
            print("Slider value:", value)
            self.previous_value = value

    def show_present_silder(self, event=None):
        pass
       
    '''
    LEFT OFF
    TODO redo this and add it's proper settings options objects
    6/21/23
    '''

    