import  webbrowser
while(True):
    print("Do you want to search the song:")
    print("1. yes[y]    2. no[n] ")
    choice = input()
    if(choice=='y'):
        print("search the song here: ")
        yes_choice= input()

        yes_choice=yes_choice.replace(" ","+")
        yes_choice = yes_choice.rstrip("+")
        web = 'https://music.youtube.com/search?q='+yes_choice
        webbrowser.open(web, new=2)
        break
    elif(choice=='n'):
        webbrowser.open('https://music.youtube.com/', new=2)
        break
    else:
        print("wrong data entered.Please try again")
        continue
