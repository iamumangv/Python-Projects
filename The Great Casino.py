#--------------- The Grand Casino ----------------
import random
from time import sleep

class casino:
    name = GuessPlay= highLowPlay = LuckyDraw = RPSPlay = age = money = 0

    def __init__(self):
        print("\n----      Welcome to our casino       ----")
        sleep(1)

        self.name = input("\nEnter your Name: ")
        self.age = int(input("Enter your Age: "))
        self.money = int(input("Enter your Money: "))
        sleep(1)
        print(f"\nThank You for registration {self.name}.")

        if self.age > 18:
            print("\nYou are eligible.")
            if self.money < 1000:
                sleep(1.5)
                print("\nSeems you have less money!\nTake 20000 more")
                self.money += 20000
                sleep(1)
                print(f"\nYour money: {self.money}")
            self.on_Off = 1
        
        else:
            print("But you are not eligible!")
            self.on_Off = 0

    # Game 1 Higher or Lower
    def highlow(self):
        print("\n------------------  Higher or Lower  ----------------")
        a = random.randint(1,11)
        sleep(1)
        print("Winning doubles the money!")
        hChoice = int(input("\nPlease enter your choice [1 to 10]: "))
        hToken = input("Please enter your choice [higher/lower]: ")
        hMoney = int(input("How much do you want to bet: "))
        sleep(1)
        if hToken == "higher":
            if hChoice < a:
                print("You Won!")
                self.money += (2*hMoney)
                print(f"\nYour money: {self.money}")
                self.highLowPlay = "won"
            else:
                print("You lost!")
                self.money -= hMoney
                print(f"\nYour money: {self.money}")
                self.highLowPlay = "lost"
            if hChoice == a:
                print("Its a draw !")
                print(f"\nYour money: {self.money}")
                self.highLowPlay = "Draw"
        if hToken == "lower":
            if hChoice > a:
                print("You Won!")
                self.money += (2*hMoney)
                print(f"\nYour money: {self.money}")
                self.highLowPlay = "won"
            else:
                print("You lost!")
                self.money -= hMoney
                print(f"\nYour money: {self.money}")
                self.highLowPlay = "lost"
            if hChoice == a:
                print("Its a draw !")
                print(f"\nYour money: {self.money}")
                self.highLowPlay = "Draw"
        sleep(1)
        print(f"The number was: {a}")
        sleep(3)
            
    # Game 2 Guess the number
    def guessNo(self):
        print("\n------------------  Guess the number  ----------------")
        a = random.randint(1,10)
        sleep(1)
        print("Winning Multiply the bet by 5!\nLosing decrease it by 3 times")
        gChoice = int(input("\nPlease enter your choice [1 to 10]: "))
        gMoney = int(input("How much do you want to bet: "))
        sleep(1)
        if gChoice == a:
            print("You Won!")
            self.money += (5*gMoney)
            print(f"\nYour money: {self.money}")
            self.GuessPlay = "won"
        else:
            print("You lost!")
            self.money -= 3*gMoney
            print(f"\nYour money: {self.money}")
            self.GuessPlay = "lost"
        sleep(1)
        print(f"The number was: {a}")
        sleep(3)

    # User Information
    def userInfo(self):
        print(f"\nUser Name : {self.name}")
        sleep(1)
        print(f"User Age : {self.age}")
        sleep(1)
        print(f"User Balance : {self.money}")
        
        if self.highLowPlay != 0:
            sleep(1)
            print(f"Last time in Higher or lower you {self.highLowPlay}")
        
        if self.GuessPlay != 0:
            sleep(1)
            print(f"Last time in Guess the number you {self.GuessPlay}")
        
        if self.RPSPlay != 0:
            sleep(1)
            print(f"Last time in Rock paper scissor you {self.RPSPlay}")
        
        if self.LuckyDraw != 0:
            sleep(1)
            print(f"Last time in Lucky Draw you made {self.LuckyDraw}")

    #Add money 
    def addMoney(self):
        print("------------ ADD Money --------------")
        sleep(1)
        print(f"Account Balance : {self.money}")
        sleep(1)
        addMoney = int(input("How much money you want to enter :"))
        self.money += addMoney
        print(f"Current Account Balance : {self.money}")
        sleep(3)

    def RockPaperScissor(self):
        print("-------- Rock Paper Scissor ----------")
        sleep(1)
        print("Winning quadrouple's the Money But Losing Reduse it by 3 times")
        sleep(1)
        RPSplayer = input("\nrock,paper or scissor ?")
        RPSbet = int(input("Enter you bet amount : "))
        RPSplayer = RPSplayer.lower()
        sleep(1)
        # Computer Choice
        l = ["rock","paper","scissor"]
        RPScomputer = random.choice(l)
        #   Logic
        if RPSplayer == RPScomputer :
            print("Computer chose : ",RPScomputer) 
            print("Its a tie !")
            self.RPSPlay = "Tie"

        if RPSplayer == "rock" :
            print("Computer chose : ",RPScomputer)
            if RPScomputer == "paper" :
                print("You lost !")
                self.RPSPlay = "Lost"
                self.money -= 3*RPSbet
            if RPScomputer == "scissor" :
                print("You Won !")
                self.RPSPlay = "Won"
                self.money += 4*RPSbet

        if RPSplayer == "paper" :
            print("Computer chose : ",RPScomputer)
            if RPScomputer == "rock" :
                print("You won !")
                self.RPSPlay = "Won"
                self.money += 4*RPSbet
            if RPScomputer == "scissor" :
                print("You lost !")
                self.RPSPlay = "Lost"
                self.money -= 3*RPSbet

        if RPSplayer == "scissor" :
            print("Computer chose : ",RPScomputer)
            if RPScomputer == "paper" :
                print("You won !")
                self.RPSPlay = "Won"
                self.money += 4*RPSbet
            if RPScomputer == "rock" :
                print("You lost !")
                self.RPSPlay = "Lost"
                self.money -= 3*RPSbet
        sleep(1)
        print(f"\nBank Amount :{self.money}")
        sleep(3)

    def Luckydraw(self):
        print("--------       Lucky Draw        -----------")
        sleep(1.5)
        print("Three random numbers will be selected and their sum will affect your money\n[Numbers can be negative too!]")
        sleep(0.8)
        LDbet = int(input("Enter Your grand Bet : "))

        n1 = random.randint(-5,9)
        n2 = random.randint(-4,9)
        n3 = random.randint(-5,9)
        nTotal = n1 + n2 + n3
        LDamount = nTotal * LDbet
        self.LuckyDraw = LDamount
        self.money += LDamount

        sleep(2)
        print("The first number is : ",n1)
        sleep(2)
        print("The second number is : ",n2)
        sleep(2)
        print("The third number is : ",n3)
        sleep(2)
        print(f"--------------------------\nThe grand total is {nTotal} times")
        print(f"Which is {LDamount}")
        sleep(2)
        print(f"=======================\nBank Balance : {self.money}")
        sleep(3)

def enterCas():
    cas = casino()
    while cas.on_Off == 1:
        print("\n------ Enter your choice -----")
        sleep(1)
        print("\n1. Higher or Lower")
        print("2. Guess the number")
        print("3. Rock , Paper ,Scissor")
        print("4. Lucky ? Draw")
        print("5. Add Money")
        print("6. User Info")
        print("7. Leave")

        select = int(input("Enter your choice (in number): "))
        print("------------------------------")

        if select == 1:
            cas.highlow()
        elif select == 2:
            cas.guessNo()
        elif select == 3:
            cas.RockPaperScissor()

        elif select == 4:
            cas.Luckydraw()

        elif select == 5:
            cas.addMoney()

        elif select == 6:
            cas.userInfo()

        elif select == 7:
            cas.on_Off = 0
enterCas()