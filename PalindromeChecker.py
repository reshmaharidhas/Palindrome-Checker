import tkinter as tk
from tkinter import messagebox

class Icons:
    iconPicture = r"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"


class PalindromeChecker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Palindrome Checker")
        self.window.geometry("800x600")
        self.window.config(bg="#686de0")
        self.iconPicture = tk.PhotoImage(data=Icons.iconPicture)
        self.textWidget = tk.Text(self.window,border=5)
        self.textWidget.pack(pady=20)
        self.frame1 = tk.Frame(self.window,bg="#686de0")
        self.frame1.pack()
        self.checkButton = tk.Button(self.frame1,text="Check Palindrome",font=("Times New Roman",14),padx=10,bg="black",fg="white",command=self.isPalindrome)
        self.checkButton.grid(row=0,column=0,padx=10,pady=20)
        self.findWordCount = tk.Button(self.frame1,text="Character Count",font=("Times New Roman",14),bg="black",fg="white",command=self.countCharacters)
        self.findWordCount.grid(row=0,column=2)
        self.result = tk.Label(self.window,font=("Arial",20),bg="#686de0")
        self.result.pack()
        self.window.iconphoto(True,self.iconPicture)
        self.window.mainloop()
    def isPalindrome(self):
        sentence = self.textWidget.get("0.0",tk.END)
        if sentence=="" or len(sentence)==1 or sentence.isspace():
            self.alertUser()
            return
        left_Ptr=0
        right_Ptr = len(sentence)-2
        notPalindrome=False
        while left_Ptr<=right_Ptr:
            if sentence[left_Ptr]==sentence[right_Ptr]:
                left_Ptr += 1
                right_Ptr -= 1
            else:
                notPalindrome = True
                break
        if notPalindrome==True:
            self.result.config(text="Not a palindrome")
        else:
            self.result.config(text="Palindrome")

    def countCharacters(self):
        sentence = self.textWidget.get("0.0",tk.END)
        if len(sentence)<=1:
            self.alertUser()
            return
        sentence = self.textWidget.get("0.0",tk.END)
        total_characters  = len(sentence)-1
        total_spaces = sentence.count(" ")
        final_result = "Total number of characters = "+str(total_characters)+"\nNumber of spaces = "+str(total_spaces)
        messagebox.showinfo("Character count",final_result)
    def alertUser(self):
        self.result.config(text="")
        messagebox.showerror("Invalid","Please enter a valid input to check")


PalindromeChecker()