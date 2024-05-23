import tkinter as tk
from PIL import Image, ImageTk



class Login:
    def __init__(self, parent):
 
                
        self.bg_image = Image.open("login.png")
        self.bg_image = self.bg_image.resize((450, 350), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        
        self.image_label = tk.Label(parent, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.entry1 = tk.Entry(parent)
        self.entry1.place(relx=0.5, rely=0.35, anchor="center")
        
        self.entry2 = tk.Entry(parent)
        self.entry2.place(relx=0.5, rely=0.55, anchor="center")

        self.login_button = tk.Button(parent, text="Login", command=self.login)
        self.login_button.place(relx=0.5, rely=0.65, anchor="center") 

        

    def login(self):
                    
                    print("Logging in...")

if __name__ == "__main__":
            window = tk.Tk()
            window.title ("Login")
            window.geometry("450x350")
            login = Login(window)
            window.mainloop()




