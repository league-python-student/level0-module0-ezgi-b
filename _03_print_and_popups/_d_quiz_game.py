from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer = simpledialog.askstring(title="Question 1", prompt='What is the elemental symbol for gold?')
    #      // 3.  Use an if statement to check if their answer is correct
    if answer.lower() == 'au':
        #      // 4.  if the user's answer was correct, add one to their score
        messagebox.showinfo(title='Notification', message='Correct!')
        score = score + 1
    else:
        messagebox.showerror(title='ERROR', message='Incorrect! The elemental symbol is Au, not ' + answer + '!')


    answer1 = simpledialog.askstring(title="Question 2", prompt='Is a platypus a mammal (yes or no)?')
    if answer1.lower() == 'yes':
        messagebox.showinfo(title="Notification", message="Correct!")
        score = score + 1
    else:
        messagebox.showerror(title='ERROR', message='Incorrect! A platypus IS a mammal!')


    answer2 = simpledialog.askstring(title="Question 3", prompt='What do you call a group of ravens (just the word)?')
    if answer2.lower() == 'unkindness':
        messagebox.showinfo(title="Notification", message="Correct!")
        score = score + 1
    else:
        messagebox.showerror(title='ERROR', message='Incorrect! The answer is an unkindness, not ' + answer2 + '!')
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title="End of Game", message="Your final score is " + str(score) + "!")
    # Run the window's .mainloop() method
