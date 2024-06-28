import customtkinter as ctk
from Class.spaced_repetition import SpacedRepetition

if __name__ == "__main__":
    root = ctk.CTk()
    app = SpacedRepetition(root)
    root.mainloop()