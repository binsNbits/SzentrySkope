import customtkinter
import os
from PIL import Image
from constants.constants import (
    GRID_ROW_0, GRID_COL_0, NSEW, APP_TITLE, PADX_1, SIZE_15, LOGO_IMG, MAP_IMG, SIZE_26, SHADE_3, SHADE_4, 
    SHADE_5, SHADE_6, TRANSPARENT, GRID_COL_1, GRID_ROW_1, GRID_ROW_2, GRID_ROW_3, GRID_ROW_4, GRID_ROW_6, EW, CORNER_RADIUS_0, 
    PEOPLE_IMG, DEV_IMG, EXP_IMG, HOME_IMG, NET_IMG, APP_IMG, IOT_IMG, SIZE_20, PADY_2, FRAME_STR_1, FRAME_STR_2, FRAME_STR_3, FRAME_STR_4, FRAME_STR_5, 
    FRAME_STR_6, FRAME_STR_7, FRAME_STR_8, DARK_MODE, LIGHT_MODE, SYS_MODE, S
)


class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # set image path and images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images") # TODO -> config path 
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, LOGO_IMG)), size=(SIZE_26, SIZE_26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, LOGO_IMG)), size=(SIZE_20, SIZE_20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, HOME_IMG)),
                                                 dark_image=Image.open(os.path.join(image_path, HOME_IMG)), size=(SIZE_20, SIZE_20))
        self.devices_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, PEOPLE_IMG)),
                                                 dark_image=Image.open(os.path.join(image_path, PEOPLE_IMG)), size=(SIZE_20, SIZE_20))
        self.people_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, DEV_IMG)),
                                                     dark_image=Image.open(os.path.join(image_path, DEV_IMG)), size=(SIZE_20, SIZE_20))
        self.cve_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, EXP_IMG)),
                                                     dark_image=Image.open(os.path.join(image_path, EXP_IMG)), size=(SIZE_20, SIZE_20))
        self.net_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, NET_IMG)),
                                                     dark_image=Image.open(os.path.join(image_path, NET_IMG)), size=(SIZE_20, SIZE_20))
        self.app_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, APP_IMG)),
                                                     dark_image=Image.open(os.path.join(image_path, APP_IMG)), size=(SIZE_20, SIZE_20))
        self.map_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, MAP_IMG)),
                                                     dark_image=Image.open(os.path.join(image_path, MAP_IMG)), size=(SIZE_20, SIZE_20))
        self.iot_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, IOT_IMG)),
                                                     dark_image=Image.open(os.path.join(image_path, IOT_IMG)), size=(SIZE_20, SIZE_20))


        # config style
        self._corner_radius = CORNER_RADIUS_0

        # create label
        self.nav_label = customtkinter.CTkLabel(self,
                                                text=f"  {APP_TITLE}", 
                                                image=self.logo_image,
                                                compound="left", 
                                                font=customtkinter.CTkFont(size=SIZE_15, 
                                                weight="bold"))
        
        self.nav_label.grid(row=GRID_ROW_0, 
                            column=GRID_COL_0, 
                            padx=PADX_1, 
                            pady=PADX_1)
        
        self.grid(row=GRID_ROW_0, 
                  column=GRID_COL_0, 
                  sticky=NSEW)
        
        # create navigation buttons
        self.sidebar_btn_1 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_1,
                                                   fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                   image=self.home_image, anchor="w")
        self.sidebar_btn_1.grid(row=GRID_ROW_1, column=GRID_COL_0, sticky=EW)

        self.sidebar_btn_2 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_2,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.devices_image, anchor="w")
        self.sidebar_btn_2.grid(row=GRID_ROW_2, column=GRID_COL_0, sticky=EW)

        self.sidebar_btn_3 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_3,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.people_image, anchor="w")
        self.sidebar_btn_3.grid(row=GRID_ROW_3, column=GRID_COL_0, sticky=EW)

        self.sidebar_btn_4 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_4,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.cve_image, anchor="w")
        self.sidebar_btn_4.grid(row=GRID_ROW_4, column=GRID_COL_0, sticky=EW)

        self.sidebar_btn_5 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_5,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.net_image, anchor="w")
        self.sidebar_btn_5.grid(row=GRID_ROW_1, column=GRID_COL_1, sticky=EW)

        self.sidebar_btn_6 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_6,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.app_image, anchor="w")
        self.sidebar_btn_6.grid(row=GRID_ROW_2, column=GRID_COL_1, sticky=EW)

        self.sidebar_btn_7 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_7,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.map_image, anchor="w")
        self.sidebar_btn_7.grid(row=GRID_ROW_3, column=GRID_COL_1, sticky=EW)

        self.sidebar_btn_8 = customtkinter.CTkButton(self, corner_radius=CORNER_RADIUS_0, height=40, border_spacing=PADY_2, text=FRAME_STR_8,
                                                      fg_color=TRANSPARENT, text_color=(SHADE_3, SHADE_4), hover_color=(SHADE_5, SHADE_6),
                                                      image=self.iot_image, anchor="w")
        self.sidebar_btn_8.grid(row=GRID_ROW_4, column=GRID_COL_1, sticky=EW)

        # create appearance mnode menu with options
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self, values=[DARK_MODE, LIGHT_MODE, SYS_MODE])
                                                                
        self.appearance_mode_menu.grid(row=GRID_ROW_6, column=GRID_COL_0, padx=PADX_1, pady=PADX_1, sticky=S)

       