# gui.py
import logging
import tkinter as tk

class GUI:
    def __init__(self, config):
        self.config = config
        self.root = tk.Tk()

    def run(self):
        self.root.mainloop()

# Usage:
gui = GUI(config)
gui.run()
