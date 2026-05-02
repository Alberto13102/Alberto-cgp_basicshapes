import tkinter as tk

# Create window
window = tk.Tk()
window.title("My Canvas Drawing")
window.geometry("500x400")

# Create canvas
canvas = tk.Canvas(window, width=500, height=400, bg="white")
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 150, fill="green")

# Draw a circle (oval)
canvas.create_oval(200, 50, 300, 150, fill="pink")

# Draw a line
canvas.create_line(50, 200, 300, 200, fill="blue", width=3)

# Add your name at the bottom
canvas.create_text(250, 350, text="Michael Sam B. Alberto", font=("Arial", 14))

# Run the window
window.mainloop()