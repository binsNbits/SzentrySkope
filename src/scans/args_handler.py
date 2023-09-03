


class ArgsHandler:
    def __init__(self, command=None, args_list1=None, *args, **kwargs):
        self.gui_callback1 = None
        self.args_list1 = args_list1 if args_list1 is not None else []        

    def register_gui_callback(self, callback1):
        self.gui_callback1 = callback1

    

    # handle checkbox args
    def non_gui_method(self):
        # Perform the desired functionality here
        # For example, you can iterate over the args_list1 and process each argument
        for arg in self.args_list1:
            # Perform some action with the argument
            print("Processing argument:", arg)

        # Call the callback function if it exists
        if self.gui_callback1 is not None:
            self.gui_callback1(self.args_list1)
            print("Sending callback1 signal from non-GUI code:", self.args_list1)


'''    def non_gui_method(self):
        print("Non-GUI method")
        if self.gui_callback1 is not None:
            self.gui_callback1(self.args_list1)
            print("Sending callback1 signal from non-GUI code:", self.args_list1)
        
       '''

            
        

        