import customtkinter as ctk
import datetime

class SpacedRepetition:
    def __init__(self, root):
        self.root = root
        self.root.title('Spaced Repetition')

        # Date
        self.date_frame = ctk.CTkFrame(self.root)
        self.date_frame.pack(
            side="top",
            padx=20,
            pady=20,
            fill="x"
        )
        
        today = datetime.date.today()
        date_label = ctk.CTkLabel(
            self.date_frame,
            text=today.strftime("%B %d, %Y")
        )
        date_label.pack(side="left")
        
        # Main
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(
            side="bottom",
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        
        # Courses
        self.courses_frame = ctk.CTkFrame(self.main_frame)
        self.courses_frame.pack(
            side="left",
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )
        
        # Buttons
        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.pack(
            side="right",
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        add_button = ctk.CTkButton(
            self.buttons_frame,
            text="Add Course",
            command=self.add_course
        )
        add_button.pack(
            side="top",
            pady=10
        )
        
        quit_button = ctk.CTkButton(
            self.buttons_frame,
            text="Quit",
            command=self.quit
        )
        quit_button.pack(
            side="top",
            pady=10
        )
        
        self.main_frame.grid_columnconfigure(0, weight=8)
        self.main_frame.grid_columnconfigure(1, weight=2)

    def add_course(self):
        pass
    
    def quit(self):
        self.root.destroy()