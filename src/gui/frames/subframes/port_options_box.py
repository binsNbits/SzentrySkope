import customtkinter
import tkinter
import sys
import traceback

from constants.constants import (
    CORNER_RADIUS_0, GRID_ROW_2, GRID_COL_2, PADY_1, PADX_1, NSEW, PADX_2, 
    PADY_2, PADX_1, N
)
from constants.path_constants import (PATH_1)
from data.net_scan_data import scan_ports
#sys.path.append('/home/cyberyshield/SzentrySkope/src/gui/frames/')
#from err.err_msg import ErrMsg

class PortOptionsBox(customtkinter.CTkFrame):
    def __init__(self, master, args_list=None, command=None):
        super().__init__(master)

        self.grid(row=1, column=3, padx=(PADX_1, 20), pady=(PADY_1, 0), sticky=NSEW)

        # styling configure
        self._corner_radius = CORNER_RADIUS_0

        # setup port variables key/value pairs
        self.port_opt_len = len(scan_ports)
        self.kp_0 = self.port_opt_len - 3
        self.kp_1 = self.port_opt_len - 2
        self.kp_2 = self.port_opt_len - 1

        self.command = command
        self.args_list = args_list if args_list is not None else []
        self.first_key, self.first_value = list(scan_ports.items())[self.kp_0]
        self.second_key, self.second_value = list(scan_ports.items())[self.kp_1]
        self.third_key, self.third_value = list(scan_ports.items())[self.kp_2]

        

        # init args
       
        self.toplevel_window = None # err msg handler
        self.entry_start = None
        self.entry_end = None
        self.previous_selection = ""
        
        # set default selected value for radio buttons
        self.radio_var = tkinter.StringVar(value=self.first_value)
        self.switch_var = customtkinter.StringVar(value="off")

        self.label_radio_group = customtkinter.CTkLabel(self,  text="Port Range")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=PADX_2, pady=PADY_2, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(self, text=self.first_key, variable=self.radio_var, value=self.first_value, command=self.radio_button_command)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n",columnspan=1)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text=self.second_key, variable=self.radio_var, value=self.second_value, command=self.radio_button_command)
        self.radio_button_2.grid(row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N, columnspan=1)
        
        self.switch = customtkinter.CTkSwitch(self, text=self.third_key + " Off", variable=self.switch_var, onvalue="on", offvalue="off", command=self.switch_event)
        self.switch.grid(row=3, column=2, pady=PADY_2, padx=PADX_1, sticky="n", columnspan=1)

        

        self.start_value = tkinter.StringVar()
        self.end_value = tkinter.StringVar()
        
        self.entry_start = customtkinter.CTkEntry(self, placeholder_text="From...", textvariable=self.start_value)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.entry_end = customtkinter.CTkEntry(self, placeholder_text="To...", textvariable=self.end_value)
        self.entry_end.grid(row=5, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.submit_button_event) 
        self.submit_button.grid(row=6, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.reset_button = customtkinter.CTkButton(self, text="Reset", command=self.reset_port_options)
        self.reset_button.grid(row=7, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.reset_button.configure(state=tkinter.DISABLED)

        self.entry_start.configure(state=tkinter.DISABLED)
        self.entry_end.configure(state=tkinter.DISABLED)
        self.submit_button.configure(state=tkinter.DISABLED)

    


    def radio_button_command(self):
        self.current_selection = self.radio_var.get()
        if self.current_selection == self.first_value and self.current_selection not in self.args_list:
            self.args_list = [self.first_value]
            self.command(self.args_list)
            print(self.args_list)
                
        elif self.current_selection == self.second_value:
            self.args_list = [self.second_value]
            self.command(self.args_list)
            print(self.args_list)
           
    
        self.previous_selection = self.current_selection

    def switch_event(self):
        self.switch_state = self.switch_var.get()
        
        if self.switch_state == "on":
            # Disable radio buttons
            self.switch.configure(text=self.third_key + " On")
            self.radio_button_1.configure(state=tkinter.DISABLED)
            self.radio_button_2.configure(state=tkinter.DISABLED)

            # Enable entry fields and submit button
            self.entry_start.configure(state=tkinter.NORMAL)
            self.entry_end.configure(state=tkinter.NORMAL)
            self.submit_button.configure(state=tkinter.NORMAL)
            
        else:
            # Enable radio buttons
            self.switch.configure(text=self.third_key + " Off")
            self.radio_button_1.configure(state=tkinter.NORMAL)
            self.radio_button_2.configure(state=tkinter.NORMAL)

            # Disable entry fields and submit button
            self.entry_start.configure(state=tkinter.DISABLED)
            self.entry_end.configure(state=tkinter.DISABLED)
            self.submit_button.configure(state=tkinter.DISABLED)
            
            
            
           

    def submit_button_event(self):
        self.start_input = self.start_value.get()
        self.end_input = self.end_value.get()
        
        try:
            self.start_value = int(self.start_input)
            self.end_value = int(self.end_input)
            
            if 1 <= self.start_value <= 65535 and 1 <= self.end_value <= 65535 and self.start_value < self.end_value:
                self.start_value = self.start_value
                self.end_value = self.end_value
                # Use the start_value and end_value as needed
                print("Start value:", self.start_value)
                print("End value:", self.end_value)
                self.args_list = [f"-p {str(self.start_value)}-{str(self.end_value)}"]
                self.command(self.args_list)
                print("now->", self.args_list)
                #self.reset_instance() # is this function changing argslist back to '-p 1000'?
                self.radio_button_1.configure(state=tkinter.DISABLED)
                self.radio_button_2.configure(state=tkinter.DISABLED)
                self.entry_start.configure(state=tkinter.DISABLED)
                self.entry_end.configure(state=tkinter.DISABLED)
                self.submit_button.configure(state=tkinter.DISABLED)
                self.reset_button.configure(state=tkinter.NORMAL)

            else:
                #self.err1 = ErrMsg(message="Invalid input values. Please enter integers between 1 and 65535, with the start value less than the end value.\nPort settings being reset back to default settings")
                self.reset_instance()  # Reset instance on error

        except ValueError as e:
            #self.err2 = ErrMsg(message="Invalid input values. No characters Allowed. Only integers between 1-65535\nPort settings being reset back to default settings")
            self.reset_instance()  # Reset instance on error
        except Exception as e:
            print("An error occurred:", str(e))
            traceback.print_exc()  # Print the traceback for debugging
            self.reset_instance()  # Reset instance on error

    def reset_instance(self):
        # Reset instance variables to their initial values
        self.radio_var.set(self.first_value)
        self.switch_var.set("off")
        self.entry_start.delete(0, tkinter.END)
        self.entry_end.delete(0, tkinter.END)
        self.switch_event()  # Reset switch state
        self.radio_button_command()  # Trigger radio button command


    def reset_port_options(self):
        self.reset_instance()
    
    
        