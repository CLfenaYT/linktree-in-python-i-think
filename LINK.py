import webbrowser

print("██╗░░░░░██╗███╗░░██╗██╗░░██╗░██████╗")
print("██║░░░░░██║████╗░██║██║░██╔╝██╔════╝")
print("██║░░░░░██║██╔██╗██║█████═╝░╚█████╗░")
print("██║░░░░░██║██║╚████║██╔═██╗░░╚═══██╗")
print("███████╗██║██║░╚███║██║░╚██╗██████╔╝")
print("╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░.py")

print("1 = instagram  2 = twitter  3 = twitch  4 = youtube  5 = tik tok")

c = input("You > ")

if c == "1":
    webbrowser.open('https://www.instagram.com/')
if c == "2":
    webbrowser.open('https://twitter.com/')
if c == "3":
    webbrowser.open('https://www.twitch.tv/')
if c == "4":
    webbrowser.open('https://www.youtube.com/')
if c == "5":
    webbrowser.open('https://www.tiktok.com/')