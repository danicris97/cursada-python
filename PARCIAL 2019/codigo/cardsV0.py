from Tkinter import Button, Label, LabelFrame, PhotoImage, DISABLED, NORMAL, E, W

import Tkinter as tk

import tkMessageBox

import random



class clsCards(tk.Tk):
    def __init__(self):

        self.__currScore =0
        self.__myList=[] # lista de cartas
        self.__myText=''
        self.__column=0        
        

        tk.Tk.__init__(self)

        self.__frame1 = LabelFrame(self)
        self.__frame1.grid(row=0, column=0)

 
        self.__frame3 = LabelFrame(self)
        self.__frame3.grid(row=1, column=0, columnspan=2, sticky=W+E)


        self.__frame4 = LabelFrame(self)
        self.__frame4.grid(row=2, column=0, columnspan=2, sticky=W+E)


        self.__btnNew = Button(self.__frame4, bg='skyblue', text='New Game', command='')
        self.__btnNew.grid(row=0, column=0, pady=3, sticky=W+E)


        self.__btnMore = Button(self.__frame4, bg='skyblue', text='More', command=self.continueGame)
        self.__btnMore.grid(row=0, column=1, pady=3, sticky=W+E)
        self.__btnMore.configure(state=DISABLED)


        self.__btnQuit = Button(self.__frame4, bg='skyblue', text='Quit', command='')
        self.__btnQuit.grid(row=0, column=2, pady=3, sticky=W+E)


        self.__lblScore = Label(self.__frame3, textvariable=self.__myText)
        self.__lblScore.grid(row=0, column=0, pady=3, sticky=W+E)        

        

    def getCardAtRandom(self):
        numberAtRandom = random.randint(1,13)

        if numberAtRandom ==1:
            numberAtRandom=14
        
        typeAtRandom = random.randint(1,4)

        if typeAtRandom ==1:
            card = 'pika'

        if typeAtRandom ==2:
            card = 'diamante'

        if typeAtRandom ==3:
            card = 'corazon'

        if typeAtRandom ==4:
            card = 'trebol'

        return str(numberAtRandom) + "-" + card


    def showCard(self):
        print str(self)

        ban = True
        continueGame=False

        while ban:
            cardOne = self.getCardAtRandom()
            if cardOne not in self.__myList:
                ban=False


        position = cardOne.find('-')
        if position>-1:
            self.__myList.append(cardOne)

            myNumber = int(cardOne[0: position])

            self.__currScore+=myNumber

            if self.__currScore==21:
                self.__myText='You win!!'

            else:

                if self.__currScore>21:
                    self.__myText='You lose ;('
                else:
                    self.__myText='Your score: ' + str(self.__currScore)     
                    continueGame=True   


        myCard = 'cards//' + cardOne + '.png' 

        self.button1 = Button (self.__frame1)
        photo1 = PhotoImage(file=myCard)
        self.button1.config(image=photo1)
        self.button1.grid(row=0, column=self.__column, padx=2, pady=2)
        self.button1.photo = photo1

        return continueGame
    

    def resetInfo(self):
        self.__currScore =0
        self.__myList=[] # lista de cartas
        self.__myText=''
        self.__column=0        
        self.__btnMore.configure(state=DISABLED)


    def continueGame(self):
        response = self.showCard()

        if response:
            self.__column+=1
        else:
            self.resetInfo()
        


    def newGame(self):
        self.resetInfo()
        self.continueGame()
        self.__btnMore.configure(state=NORMAL)        

        

if __name__ == "__main__":
    app = clsCards()
    app.title('DiPy 2019')
    app.geometry('280x180')

    app.newGame()
    app.mainloop()
