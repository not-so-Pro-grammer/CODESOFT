import tkinter as tk
def click(event):
    # Function to handle button clicks
    text = event.widget.cget("text")  #Get the text from the clicked button
    
    if text == "=":
        try:
            #Evaluate the expression in the entry field
            result = str(eval(screen.get()))  #Evaluate the expression and convert result to string
            screen.set(result)  #Update the entry field with the result
            entry.update()  #Update the display
        except Exception as e:
            screen.set("Error")  #Display "Error" if evaluation fails
            entry.update()  #Update the display
    elif text == "C":
        screen.set("")  #Clear the entry field
        entry.update()  #Update the display
    else:
        screen.set(screen.get() + text)  #Append clicked button's text to the entry field
        entry.update()  #Update the display
#Create the main application window
root = tk.Tk()
root.geometry("300x400")  #Set window size
root.title("Calculator")  #Set window title

#Variable to hold the current input expression
screen = tk.StringVar()

#Create an entry widget to display the input and result
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)  # Pack the entry widget into the window

#Define the buttons for the calculator
buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', 'C', '0', '=', '+']

#Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()  #Pack the frame into the window

#Create and place each button in the button frame
i = 0
for btn_text in buttons:
    button = tk.Button(button_frame, text=btn_text, font="lucida 15 bold") # font used 
    button.grid(row=i // 4, column=i % 4, padx=10, pady=10)  #Grid layout for buttons
    button.bind("<Button-1>", click)  #Bind left mouse click event to the click function
    i += 1

root.mainloop()  #Start the main event loop
