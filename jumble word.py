import time
from os import name,system
import random

#Defination for clear screen function.
#It will note work if you run this file in python shell !!
def clrscr():
    if(name=='nt'):
        _=system('cls')
    else:
        _=system('clear')
        
#you can add of remove words for choice from following function.
def choose():
    words=['rainbow','water','computer','science','mathematics','player','game','dedicated','blowing','special','superman','spy','expendetion','expectation','colour','happiness','concentration','hippopotamus','elephant','rhinoceroses']
    pick=random.choice(words)
    return pick

#make the world jumbled.
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

#thank you message.
def thank(p1n,p2n,p1,p2):
    print(p1n,' Your score is: ',p1)
    print(p2n,' Your score is: ',p2)
    print('Thanks for playing\nHave a nice day')
    time.sleep(2)
    
#play function
def play():
    p1name=input("Player 1, please enter your name ")
    p2name=input("Player 2, please enter your name ")
    print("Let's start the game!!")
    time.sleep(1)
    pp1=0
    pp2=0
    turn=0
    while(1):
        clrscr()
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            print(p1name,'Your turn')
            ans=input('What\'s on my mind? ')
            if ans==picked_word:
                pp1+=1
                print('Your score is ',pp1)
            else:
                print('Better luck next time.I thought: ',picked_word)
            c=int(input('Press 1 to continue and 0 to quit: '))
            time.sleep(0.4)
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            print(p2name,'Your turn')
            ans=input('What is on my mind? ')
            if ans==picked_word:
                pp2+=1
                print('Your score is ',pp2)
            else:
                print('Better luck next time.I thought: ',picked_word)
            c=int(input('Press 1 to continue and 0 to quit: '))
            time.sleep(0.4)
            if c==0:
                clrscr()
                thank(p1name,p2name,pp1,pp2)
                break
        turn+=1
if __name__ == '__main__' :
    play()
