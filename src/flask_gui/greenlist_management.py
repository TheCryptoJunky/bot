# File: /src/gui/greenlist_management.py

import tkinter as tk
from tkinter import messagebox
from src.database import add_to_greenlist, remove_from_greenlist, get_greenlist, update_focus_duration

class GreenlistManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Greenlist Management")

        # Greenlist frame
        self.greenlist_frame = tk.Frame(self.root)
        self.greenlist_frame.pack(pady=10)

        # Add new Greenlist asset
        self.asset_label = tk.Label(self.greenlist_frame, text="Asset Address:")
        self.asset_label.grid(row=0, column=0, padx=10, pady=10)

        self.asset_entry = tk.Entry(self.greenlist_frame)
        self.asset_entry.grid(row=0, column=1, padx=10, pady=10)

        self.focus_label = tk.Label(self.greenlist_frame, text="Focus Duration (minutes):")
        self.focus_label.grid(row=1, column=0, padx=10, pady=10)

        self.focus_entry = tk.Entry(self.greenlist_frame)
        self.focus_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.greenlist_frame, text="Add to Greenlist", command=self.add_asset)
        self.add_button.grid(row=2, column=1, padx=10, pady=10)

        # Greenlist display
        self.greenlist_display = tk.Listbox(self.greenlist_frame, width=50)
        self.greenlist_display.grid(row=3, columnspan=2, padx=10, pady=10)

        self.update_greenlist_display()

        # Remove selected Greenlist asset
        self.remove_button = tk.Button(self.greenlist_frame, text="Remove Selected", command=self.remove_asset)
        self.remove_button.grid(row=4, column=1, padx=10, pady=10)

        # Update focus duration for selected asset
        self.update_button = tk.Button(self.greenlist_frame, text="Update Focus Duration", command=self.update_focus)
        self.update_button.grid(row=5, column=1, padx=10, pady=10)

    def add_asset(self):
        """
        Adds the asset to the Greenlist and updates the display.
        """
        asset_address = self.asset_entry.get()
        focus_duration = self.focus_entry.get()

        if not asset_address or not focus_duration.isdigit():
            messagebox.showerror("Error", "Invalid input. Please enter valid asset and duration.")
            return

        try:
            add_to_greenlist(asset_address, int(focus_duration))
            self.update_greenlist_display()
            messagebox.showinfo("Success", f"Asset {asset_address} added to Greenlist.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add asset: {e}")

    def remove_asset(self):
        """
        Removes the selected asset from the Greenlist.
        """
        selected_item = self.greenlist_display.curselection()
        if not selected_item:
            messagebox.showerror("Error", "No asset selected.")
            return

        asset_address = self.greenlist_display.get(selected_item)
        try:
            remove_from_greenlist(asset_address)
            self.update_greenlist_display()
            messagebox.showinfo("Success", f"Asset {asset_address} removed from Greenlist.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove asset: {e}")

    def update_focus(self):
        """
        Updates the focus duration for the selected Greenlist asset.
        """
        selected_item = self.greenlist_display.curselection()
        focus_duration = self.focus_entry.get()

        if not selected_item or not focus_duration.isdigit():
            messagebox.showerror("Error", "Invalid input.")
            return

        asset_address = self.greenlist_display.get(selected_item)
        try:
            update_focus_duration(asset_address, int(focus_duration))
            messagebox.showinfo("Success", f"Focus duration updated for {asset_address}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update focus duration: {e}")

    def update_greenlist_display(self):
        """
        Refreshes the Greenlist display.
        """
        self.greenlist_display.delete(0, tk.END)
        greenlist = get_greenlist()

        for asset in greenlist:
            self.greenlist_display.insert(tk.END, asset["asset_address"])

if __name__ == "__main__":
    root = tk.Tk()
    app = GreenlistManager(root)
    root.mainloop()
