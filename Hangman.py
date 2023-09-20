import random
import string
with open("words.txt") as f:
    ch = f.read().splitlines()
ran_ch=random.choice(ch)
st=ran_ch.casefold()
new_str=[]
for i in st:
    new_str.append(i)
str=[]
for j in new_str:
    if j==new_str[0]:
        str.append(j)
    elif j==new_str[-1]:
        str.append(j)
    else:
        str.append('_')
print(str)
s= 1
wrong=0
w=0
while s!=0:
    guess=input("\nEnter the Choice letter: ").lower()
    wrong=0
    for k in range(0, len(new_str)):
        if guess==new_str[k]:
            str[k]=guess
        else:
            wrong+=1
    if wrong==len(new_str):
        w+=1
        if w==1:
            print(str)
            print("\nIncorrect Guess word 😔 !")
            print('''
            --------------
               |         |
                         |
                         
            ''')
        elif w==2:
            print(str)
            print("\nIncorrect Guess word 😔😔 !")
            print('''
            --------------
               |         |
               0         |
                         |
                         
            ''')
        elif w==3:
            print(str)
            print("\nIncorrect Guess word 😔😔😔 !")
            print('''
            --------------
               |         |
               0         |
              |||        |
                         |
                         
            ''')
        elif w==4:
            print(str)
            print("\nIncorrect Guess word 😔😔😔😔 !")
            print('''
            --------------
               |         |
               0         |
             /|||\       |
                         |
            ''')
        elif w==5:
            print("\nIncorrect Guess word 😔😔😔😔😔 !")
            print('''
            -----------
               |      H
               0      A
             /|||\    N
              / \     G
                      E
            H A N G E D  
            ''')
            print("You LOST the game 😭😭😭😭😭 !")
    else:
        wrong=0
        for l in str:
            if l=='_':
                s=1
                print()
                print(str)
                break
            else:
                s=0
    if w==5:
        s=input("Enter 0, to over ")
        if s!=0:
            exit(0)
n=0
for p in range(0, len(str)):
    if str[p]==new_str[p]:
        n+=1
if n== len(str):
    print()
    print(str)
    print("\n💐💐CONGRATULATION💐💐 !!\nYou WIN 🥳🥳  the game 😀😀😀😀😀 !")
print("\nOver")  