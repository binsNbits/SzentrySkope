import customtkinter
import os
from PIL import Image
from constants.constants import (
    CORNER_RADIUS_0, TRANSPARENT, SIZE_20, SIZE_500, SIZE_150, HOME_IMG, LOGO_IMG, 
    GRID_ROW_0, GRID_COL_0, PADX_1, PADY_2
)

class Home(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images") # TODO -> config path 
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, HOME_IMG)),
                                                 dark_image=Image.open(os.path.join(image_path, HOME_IMG)), size=(SIZE_20, SIZE_20))
        self.large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, LOGO_IMG)), size=(SIZE_500, SIZE_150))

        self.home_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_image)
        self.home_frame_large_image_label.grid(row=GRID_ROW_0, column=GRID_COL_0, padx=PADX_1, pady=PADY_2)

        # config style
        self._corner_radius = CORNER_RADIUS_0
        self.fg_color = TRANSPARENT