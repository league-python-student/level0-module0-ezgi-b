from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    randvar = random.randint(0, 3)
    # 2. Print your variable to the console
    print(randvar)
    # 3. Get the user to enter something that they think is awesome
    enter = simpledialog.askstring(title="Question", prompt='What is one activity you find awesome?')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if randvar == 0:
        messagebox.showinfo(title="Result", message="Yes, " + enter + " is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if randvar == 1:
        messagebox.showinfo(title="Result", message="Well, " + enter + " is okay.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if randvar == 2:
        messagebox.showinfo(title="Result", message="No, " + enter + " is actually very boring.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if randvar == 3:
        messagebox.showinfo(title="Result", message="Yes, " + enter + " is awesome! But only on Mondays.")
    # Run the window's .mainloop() method
