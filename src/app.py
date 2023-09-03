import customtkinter
import os
from PIL import Image
from gui.frames.sidebar import Sidebar
from gui.frames.home import Home
from gui.frames.users import Users
from gui.frames.devices import Devices
from gui.frames.cves import CVES
from gui.frames.scanner.network_scanner import NetworkScanner
from gui.frames.scanner.app_scanner import AppScanner
from gui.frames.scanner.map_scanner import MapScanner
from gui.frames.scanner.iot_scanner import IOTScanner
from constants.constants import *

customtkinter.set_appearance_mode(DARK_MODE)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(BLUE_THEME)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set main frame image(s)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gui//images") # TODO -> config path 
        self.large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, LOGO_IMG)), size=(SIZE_600, SIZE_200))
        self.large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_image)
        self.large_image_label.grid(row=GRID_ROW_0, column=GRID_COL_1, padx=PADX_1, pady=PADY_2)

        self.name_label = customtkinter.CTkLabel(self,
                                                text=f"{APP_TITLE}", 
                                                compound="center", 
                                                font=customtkinter.CTkFont(size=SIZE_50, 
                                                slant="italic",
                                                weight="bold"))
        
        self.name_label.grid(row=GRID_ROW_0, 
                            column=GRID_COL_1, 
                            padx=PADX_1, 
                            pady=PADX_1)


        # create title
        self.title(APP_TITLE)

        # create geometry
        self.geometry(f"{WINDOW_GEOMETRYX}x{WINDOW_GEOMETRYY}")

        self.grid_rowconfigure(GRID_ROW_0, 
                               weight=GRID_WEIGHT_1)
        
        self.grid_columnconfigure(1, 
                                  weight=GRID_WEIGHT_1)

        # create sidebar for navigation
        self.sidebar = Sidebar(self)
        self.sidebar.grid_rowconfigure(GRID_ROW_5, 
                                       weight=GRID_WEIGHT_1)

        
        
        # create frames and map them to sidebar buttons
            # home frame/button
        self.sidebar.sidebar_btn_1.configure(command=self.sidebar_btn_1_event)
        self.home = Home(self)
        self.home.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

            # users frame/button
        self.sidebar.sidebar_btn_2.configure(command=self.sidebar_btn_2_event)
        self.users = Users(self)
        self.users.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

            # devices frame/button
        self.sidebar.sidebar_btn_3.configure(command=self.sidebar_btn_3_event)
        self.devices = Devices(self)
        self.devices.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

            # cves frame/button
        self.sidebar.sidebar_btn_4.configure(command=self.sidebar_btn_4_event)
        self.cves = CVES(self)
        self.cves.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

        
            # network_scanner frame/button
        self.sidebar.sidebar_btn_5.configure(command=self.sidebar_btn_5_event)
        self.network_scanner = NetworkScanner(self)
        self.network_scanner.grid_columnconfigure(GRID_COL_1, weight=GRID_WEIGHT_1)
        self.network_scanner.grid_columnconfigure((GRID_COL_2, GRID_COL_3), weight=GRID_WEIGHT_0)
        self.network_scanner.grid_rowconfigure((GRID_COL_0, GRID_COL_1, GRID_COL_2), weight=GRID_WEIGHT_1)
        
            # app_scanner frame/button
        self.sidebar.sidebar_btn_6.configure(command=self.sidebar_btn_6_event)
        self.app_scanner = AppScanner(self)
        self.app_scanner.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

            # map_scanner frame/button
        self.sidebar.sidebar_btn_7.configure(command=self.sidebar_btn_7_event)
        self.map_scanner = MapScanner(self)
        self.map_scanner.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

            # iot_scanner frame/button
        self.sidebar.sidebar_btn_8.configure(command=self.sidebar_btn_8_event)
        self.iot_scanner = IOTScanner(self)
        self.iot_scanner.grid_columnconfigure(GRID_COL_0, weight=GRID_WEIGHT_1)

        # create appearance mode menu
        self.sidebar.appearance_mode_menu.configure(command=self.change_appearance_mode_event)

    # change appearance mode
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Select frame by name
    def select_frame_by_name(self, name):
        frame_button_pairs_1 = [
        (self.home, self.sidebar.sidebar_btn_1, FRAME_STR_1),
        (self.users, self.sidebar.sidebar_btn_2, FRAME_STR_2),
        (self.devices, self.sidebar.sidebar_btn_3, FRAME_STR_3),
        (self.cves,self.sidebar.sidebar_btn_4, FRAME_STR_4), 
        (self.network_scanner, self.sidebar.sidebar_btn_5, FRAME_STR_5), 
        (self.app_scanner, self.sidebar.sidebar_btn_6, FRAME_STR_6), 
        (self.map_scanner, self.sidebar.sidebar_btn_7, FRAME_STR_7), 
        (self.iot_scanner, self.sidebar.sidebar_btn_8, FRAME_STR_8)
        ]

        

        for frame, button, frame_name in frame_button_pairs_1:
            button.configure(fg_color=(SHADE_1, SHADE_2) if name == frame_name else TRANSPARENT)

            if name == frame_name:
                frame.grid(row=0, column=GRID_COL_1, sticky=NSEW)
            else:
                frame.grid_forget()

        


    # create sidebar button events
    def sidebar_btn_1_event(self):
        print("button" + FRAME_STR_1 + " clicked")
        self.select_frame_by_name(FRAME_STR_1)

    def sidebar_btn_2_event(self):
        print("button" + FRAME_STR_2 + " clicked")
        self.select_frame_by_name(FRAME_STR_2)

    def sidebar_btn_3_event(self):
        print("button" + FRAME_STR_3 + " clicked")
        self.select_frame_by_name(FRAME_STR_3)

    def sidebar_btn_4_event(self):
        print("button" + FRAME_STR_4 + " clicked")
        self.select_frame_by_name(FRAME_STR_4)

    def sidebar_btn_5_event(self):
        print("button" + FRAME_STR_5 + " clicked")
        self.select_frame_by_name(FRAME_STR_5)

    def sidebar_btn_6_event(self):
        print("button" + FRAME_STR_6 + " clicked")
        self.select_frame_by_name(FRAME_STR_6)

    def sidebar_btn_7_event(self):
        print("button" + FRAME_STR_7 + " clicked")
        self.select_frame_by_name(FRAME_STR_7)

    def sidebar_btn_8_event(self):
        print("button" + FRAME_STR_8 + " clicked")
        self.select_frame_by_name(FRAME_STR_8)

    # create net_scanner checkbox frame event
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.network_scanner.scan_techniques_box.get_checked_items()}")
        