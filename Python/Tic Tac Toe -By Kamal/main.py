from tkinter import *
import tkinter.messagebox
import random
import pygame
import os
from PIL import Image,ImageTk
pygame.mixer.init()
def mains():
    global player
    global text
    global tk
    board=[' ' for x in range(10)]
    tk = Tk()
    tk.title("Tic Tac Toe *Singleplayer*")
    tk.iconbitmap("imgs//icon.ico")
    tk.geometry("370x400")
    tk.resizable(False,False)
    k=[]
    z=""
    player=True
    text=Label(text="Player's turn")
    text.pack_configure()
    bv1=StringVar()
    bv2=StringVar()
    bv3=StringVar()
    bv4=StringVar()
    bv5=StringVar()
    bv6=StringVar()
    bv7=StringVar()
    bv8=StringVar()
    bv9=StringVar()
    def b1c():
        bv1.set("x")
        b1.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Computer's turn")
        board[1] = "X"
        k.append("1")
    def b2c():
        bv2.set("x")
        b2.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        board[2] = "X"
        text.config(text="Computer's turn")
        k.append("2")
    def b3c():
        bv3.set("x")
        b3.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        board[3] = "X"
        text.config(text="Computer's turn")
        k.append("3")
    def b4c():
        bv4.set("x")
        b4.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        board[4] = "X"
        text.config(text="Computer's turn")
        k.append("4")
    def b5c():
        bv5.set("x")
        board[5] = "X"
        b5.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Computer's turn")
        k.append("5")   
    def b6c():
        bv6.set("x")
        board[6] = "X"
        b6.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Computer's turn")
        k.append("6")
    def b7c():
        k.append("7")
        bv7.set("x")
        board[7] = "X"
        b7.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Computer's turn")
    def b8c():
        k.append("8")
        bv8.set("x")
        b8.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        board[8] = "X"
        text.config(text="Computer's turn")
    def b9c():
        k.append("9")
        bv9.set("x")
        b9.configure(text="X", font="algerian 80 bold", state=DISABLED)
        player=False
        board[9] = "X"
        text.config(text="Computer's turn")
# ===============================================
# ===============================================
    def b1o():
        bv1.set("o")
        b1.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Player's turn")
        board[1] = "O"
        k.append("1")
    def b2o():
        bv2.set("o")
        b2.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        board[2] = "O"
        text.config(text="Player's turn")
        k.append("2")
    def b3o():
        bv3.set("o")
        b3.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        board[3] = "O"
        text.config(text="Player's turn")
        k.append("3")
    def b4o():
        bv4.set("o")
        b4.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        board[4] = "O"
        text.config(text="Player's turn")
        k.append("4")
    def b5o():
        bv5.set("o")
        board[5] = "O"
        b5.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Player's turn")
        k.append("5")   
    def b6o():
        bv6.set("o")
        board[6] = "O"
        b6.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Player's turn")
        k.append("6")
    def b7o():
        k.append("7")
        bv7.set("o")
        board[7] = "O"
        b7.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        text.config(text="Player's turn")
    def b8o():
        k.append("8")
        bv8.set("o")
        b8.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        board[8] = "O"
        text.config(text="Player's turn")
    def b9o():
        k.append("9")
        bv9.set("o")
        b9.configure(text="O", font="algerian 80 bold", state=DISABLED)
        player=False
        board[9] = "O"
        text.config(text="Player's turn")
    #============================================
    #============================================
    def winner():
        if (bv1.get()=="x" and bv2.get()=="x" and bv3.get()=="x" or
            bv1.get()=="x" and bv5.get()=="x" and bv9.get()=="x" or
            bv1.get()=="x" and bv4.get()=="x" and bv7.get()=="x" or
            bv4.get()=="x" and bv5.get()=="x" and bv6.get()=="x" or
            bv7.get()=="x" and bv8.get()=="x" and bv9.get()=="x" or
            bv3.get()=="x" and bv5.get()=="x" and bv7.get()=="x" or
            bv3.get()=="x" and bv6.get()=="x" and bv9.get()=="x" or
            bv2.get()=="x" and bv5.get()=="x" and bv8.get()=="x" or
            bv3.get()=="x" and bv5.get()=="x" and bv7.get()=="x"):
            q=tkinter.messagebox.askquestion(title="Result", message="Player wins!!\nWanna Play Again??")
            if q=="yes":
                tk.destroy()
                mains()
            elif q=="no":
                tk.destroy()
                exit()
        elif (bv1.get()=="o" and bv2.get()=="o" and bv3.get()=="o" or
            bv1.get()=="o" and bv5.get()=="o" and bv9.get()=="o" or
            bv1.get()=="o" and bv4.get()=="o" and bv7.get()=="o" or
            bv4.get()=="o" and bv5.get()=="o" and bv6.get()=="o" or
            bv7.get()=="o" and bv8.get()=="o" and bv9.get()=="o" or
            bv3.get()=="o" and bv5.get()=="o" and bv7.get()=="o" or
            bv3.get()=="o" and bv6.get()=="o" and bv9.get()=="o" or
            bv2.get()=="o" and bv5.get()=="o" and bv8.get()=="o" or
            bv3.get()=="o" and bv5.get()=="o" and bv7.get()=="o"):
            q=tkinter.messagebox.askquestion(title="Result", message="Computer wins!!\nWanna Play Again??")
            if q=="yes":
                tk.destroy()
                mains()
            elif q=="no":
                tk.destroy()
                exit()
        elif len(k) >= 9:
            q=tkinter.messagebox.askquestion(title="Result", message="Tie Game!!\nWanna Play Again??")
            if q=="yes":
                tk.destroy()
                mains()
            elif q=="no":
                tk.destroy()
                exit()
    def display():
        a=computer()
        if a == 1:
            b1o()
        elif a==2:
            b2o()
        elif a==3:
            b3o()
        elif a==4:
            b4o()
        elif a==5:
            b5o()
        elif a==6:
            b6o()
        elif a==7:
            b7o()
        elif a==8:
            b8o()
        elif a==9:
            b9o()
    def isWinner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)
    def selectRandom(li):
        ln = len(li)
        r = random.randrange(0,ln)
        return li[r]
    def computer():
        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0
        for let in ['O','X']:
            for i in possibleMoves:
                boardCopy = board[:]
                boardCopy[i] = let
                if isWinner(boardCopy, let):
                    move = i
                    return move
        cornersOpen = []
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
                
        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen)
            return move
        if 5 in possibleMoves:
            move = 5
            return move
        edgesOpen = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
        return move
    b1=Button(text="",textvariable=bv1, command=lambda:[b1c(),display(),winner()])
    b1.place_configure(x=10,y=30, width=110, height=110)
    b2=Button(text="",textvariable=bv2, command=lambda:[b2c(),display(),winner()])
    b2.place_configure(x=130,y=30, width=110, height=110)
    b3=Button(text="",textvariable=bv3, command=lambda:[b3c(),display(),winner()])
    b3.place_configure(x=250,y=30, width=110, height=110)
    b4=Button(text="",textvariable=bv4, command=lambda:[b4c(),display(),winner()])
    b4.place_configure(x=10,y=150, width=110, height=110)
    b5=Button(text="",textvariable=bv5, command=lambda:[b5c(),display(),winner()])
    b5.place_configure(x=130,y=150, width=110, height=110)
    b6=Button(text="", textvariable=bv6,command=lambda:[b6c(),display(),winner()])
    b6.place_configure(x=250,y=150, width=110, height=110)
    b7=Button(text="",textvariable=bv7, command=lambda:[b7c(),display(),winner()])
    b7.place_configure(x=10,y=270, width=110, height=110)
    b8=Button(text="",textvariable=bv8, command=lambda:[b8c(),display(),winner()])
    b8.place_configure(x=130,y=270, width=110, height=110)
    b9=Button(text="",textvariable=bv9, command=lambda:[b9c(),display(),winner()])
    b9.place_configure(x=250,y=270, width=110, height=110)
    tk.mainloop()
def main():
    global player
    global text
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe *Multiplayer*")
    tk.iconbitmap("imgs//icon.ico")
    tk.geometry("370x400")
    tk.resizable(False,False)
    k=[]
    z=""
    player=True
    text=Label(tk,text="X's turn")
    text.pack_configure()
    bv1=StringVar()
    bv2=StringVar()
    bv3=StringVar()
    bv4=StringVar()
    bv5=StringVar()
    bv6=StringVar()
    bv7=StringVar()
    bv8=StringVar()
    bv9=StringVar()
    def b1c():
        k.append("b")
        global player
        global text
        if player==True:
            bv1.set("x")
            b1.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv1.set("o")
            b1.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b2c():
        k.append("b")
        global player
        global text
        if player==True:
            bv2.set("x")
            b2.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv2.set("o")
            b2.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
            
    def b3c():
        k.append("b")
        global text
        global player
        if player==True:
            bv3.set("x")
            b3.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv3.set("o")
            b3.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b4c():
        k.append("b")
        global text
        global player
        if player==True:
            bv4.set("x")
            b4.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv4.set("o")
            b4.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b5c():
        k.append("b")
        global text
        global player
        if player==True:
            bv5.set("x")
            b5.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv5.set("o")
            b5.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b6c():
        k.append("b")
        global text
        global player
        if player==True:
            bv6.set("x")
            b6.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv6.set("o")
            b6.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b7c():
        k.append("b")
        global text
        global player
        if player==True:
            bv7.set("x")
            b7.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv7.set("o")
            b7.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b8c():
        k.append("b")
        global text
        global player
        if player==True:
            bv8.set("x")
            b8.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            
            text.configure(text="O's turn")
        else:
            bv8.set("o")
            b8.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    def b9c():
        global text
        global player
        k.append("b")
        if player==True:
            bv9.set("x")
            b9.configure(text="X", font="algerian 80 bold", state=DISABLED)
            player=False
            text.config(text="O's turn")
        else:
            bv9.set("o")
            b9.configure(text="O", font="algerian 80 bold", state=DISABLED)
            player=True
            
            text.configure(text="X's turn")
    #============================================
    #============================================
    def winner():
        if (bv1.get()=="x" and bv2.get()=="x" and bv3.get()=="x" or
            bv1.get()=="x" and bv5.get()=="x" and bv9.get()=="x" or
            bv1.get()=="x" and bv4.get()=="x" and bv7.get()=="x" or
            bv4.get()=="x" and bv5.get()=="x" and bv6.get()=="x" or
            bv7.get()=="x" and bv8.get()=="x" and bv9.get()=="x" or
            bv3.get()=="x" and bv5.get()=="x" and bv7.get()=="x" or
            bv3.get()=="x" and bv6.get()=="x" and bv9.get()=="x" or
            bv2.get()=="x" and bv5.get()=="x" and bv8.get()=="x" or
            bv3.get()=="x" and bv5.get()=="x" and bv7.get()=="x"):
            q=tkinter.messagebox.askquestion(title="Result", message="X wins!!\nWanna Play Again??")
            if q=="yes":
                tk.destroy()
                main()
            elif q=="no":
                tk.destroy()
                exit()
        elif (bv1.get()=="o" and bv2.get()=="o" and bv3.get()=="o" or
            bv1.get()=="o" and bv5.get()=="o" and bv9.get()=="o" or
            bv1.get()=="o" and bv4.get()=="o" and bv7.get()=="o" or
            bv4.get()=="o" and bv5.get()=="o" and bv6.get()=="o" or
            bv7.get()=="o" and bv8.get()=="o" and bv9.get()=="o" or
            bv3.get()=="o" and bv5.get()=="o" and bv7.get()=="o" or
            bv3.get()=="o" and bv6.get()=="o" and bv9.get()=="o" or
            bv2.get()=="o" and bv5.get()=="o" and bv8.get()=="o" or
            bv3.get()=="o" and bv5.get()=="o" and bv7.get()=="o"):
            q=tkinter.messagebox.askquestion(title="Result", message="O wins!!\nWanna Play Again??")
            if q=="yes":
                tk.destroy()
                main()
            elif q=="no":
                tk.destroy()
                exit()
        elif len(k) >= 9:
            q=tkinter.messagebox.askquestion(title="Result", message="Tie Game!!\nWanna Play Again??")
            if q=="yes":
                tk.destroy()
                main()
            elif q=="no":
                tk.destroy()
                exit()
    b1=Button(tk,text="",textvariable=bv1, command=lambda:[b1c(),winner()])
    b1.place_configure(x=10,y=30, width=110, height=110)
    b2=Button(tk,text="",textvariable=bv2, command=lambda:[b2c(),winner()])
    b2.place_configure(x=130,y=30, width=110, height=110)
    b3=Button(tk,text="",textvariable=bv3, command=lambda:[b3c(),winner()])
    b3.place_configure(x=250,y=30, width=110, height=110)
    b4=Button(tk,text="",textvariable=bv4, command=lambda:[b4c(),winner()])
    b4.place_configure(x=10,y=150, width=110, height=110)
    b5=Button(tk,text="",textvariable=bv5, command=lambda:[b5c(),winner()])
    b5.place_configure(x=130,y=150, width=110, height=110)
    b6=Button(tk,text="", textvariable=bv6,command=lambda:[b6c(),winner()])
    b6.place_configure(x=250,y=150, width=110, height=110)
    b7=Button(tk,text="",textvariable=bv7, command=lambda:[b7c(),winner()])
    b7.place_configure(x=10,y=270, width=110, height=110)
    b8=Button(tk,text="",textvariable=bv8, command=lambda:[b8c(),winner()])
    b8.place_configure(x=130,y=270, width=110, height=110)
    b9=Button(tk,text="",textvariable=bv9, command=lambda:[b9c(),winner()])
    b9.place_configure(x=250,y=270, width=110, height=110)
    tk.mainloop()
def intro():
    # global tk
    def run_multi():
        tk1.destroy()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("songs//song2.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        main()
    def run_single():
        tk1.destroy()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("songs//song2.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        mains()
    def exit1():
        tk1.destroy()
    def about():
        os.startfile('about.txt')
    tk1=Tk()
    tk1.title("Tic Tac Toe -By Kamal")
    tk1.iconbitmap("imgs//icon.ico")
    tk1.geometry("370x400")
    tk1.resizable(False, False)
    img = ImageTk.PhotoImage(Image.open("imgs//a.jpg"))
    k1=Label(image=img).pack()
    b1=Button(text="Singleplayer",font="Algerian 20 bold",bg="gray",fg="black",borderwidth="5",command=run_single)
    b2=Button(text="Multiplayer",font="Algerian 20 bold",bg="gray",fg="black",borderwidth="5",command=run_multi)
    b3=Button(text="About",font="Algerian 20 bold",bg="gray",fg="black",borderwidth="5",command=about)
    b4=Button(text="Exit",font="Algerian 20 bold",bg="gray",fg="black",borderwidth="5",command=exit1)
    b1.place(x=80, y=85, height=50,width=225)
    b2.place(x=80, y=165, height=50,width=225)
    b3.place(x=135, y=245, height=50,width=100)
    b4.place(x=135, y=325,height=50,width=100)
    def disable_event():
        pass
    tk1.protocol("WM_DELETE_WINDOW", disable_event)
    tk1.mainloop()
pygame.mixer.music.load("songs//song.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
intro() 