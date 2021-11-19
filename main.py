import tkinter
from PIL import Image, ImageTk

# define Window
root = tkinter.Tk()
root.title('JM Robotics Organizer')
root.iconbitmap("Icons/download.ico")
root.geometry('400x400')
root.config(bg="gray")


# Second Window
def openNewWindow():
    top = tkinter.Toplevel()
    top.title("Image")
    img = Image.open('images/JM-robotics_logo_liggende_profilfarge_496.png')
    tk_pil_img = ImageTk.PhotoImage(img)
    canvas = tkinter.Canvas(top, height=tk_pil_img.height(), width=tk_pil_img.width())
    canvas.create_image(0, 0, anchor='nw', image=tk_pil_img)
    canvas.theimage = tk_pil_img
    canvas.pack()


# Widgets
button = tkinter.Button(root, text="See Backplate", command=openNewWindow).pack()



# Run Window
if __name__ == "__main__":
    root.mainloop()
