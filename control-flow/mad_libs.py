import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Mad Libs story add adjective on the blank space:")
ad1 = input("On a beautiful ")
clear()

if ad1 == ad1:
    ad2 = input(f"On a beautiful {ad1} day, I went to the zoo. I saw a funny ")
    clear()
    if ad2 == ad2:
        ad3 = input(f"On a beautiful {ad1} day, I went to the zoo. I saw a funny {ad2} monkey swinging from the trees. Then, I spotted a majestic ")
        clear()
        if ad3 == ad3:
            ad4 = input(f"On a beautiful {ad1} day, I went to the zoo. I saw a funny {ad2} monkey swinging from the trees. Then, I spotted a majestic {ad3} lion lounging in the sun.  What a wild and ")
            clear()
            if ad4 == ad4:
                complete = input(f"On a beautiful {ad1} day, I went to the zoo. I saw a funny {ad2} monkey swinging from the trees. Then, I spotted a majestic {ad3} lion lounging in the sun.  What a wild and {ad4} experience!")
               
