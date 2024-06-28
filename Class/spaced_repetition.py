import customtkinter as ctk

class SpacedRepetition:
    def __init__(self, root):
        self.root = root
        self.root.title('Spaced repetition')

        # Create a frame with padding
        self.mainframe = ctk.CTkFrame(self.root)
        self.mainframe.pack(padx=12, pady=12)

        # Create a label
        ctk.CTkLabel(self.mainframe, text="Hello, Tkinter!").pack()

        # Create a button
        ctk.CTkButton(self.mainframe, text="Quit", command=self.root.destroy).pack()