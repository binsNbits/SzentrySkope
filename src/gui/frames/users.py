import customtkinter
from constants.constants import (
    CORNER_RADIUS_0
)

class Users(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # config style
        self._corner_radius = CORNER_RADIUS_0