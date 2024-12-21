# from tkinter import Tk
# from gui.app import FirewallGUI

# if __name__ == "__main__":
#     root = Tk()
#     app = FirewallGUI(root)
#     root.mainloop()




import gui.app_streamlit  # Import the refactored app.py file

if __name__ == "__main__":
    gui.app_streamlit.FirewallApp()
