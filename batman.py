import  socket
import sys
from colorama import init, Fore
import os
import subprocess
import time
import shutil
import zipfile
import argparse
import logging
import click


init()

text_green=Fore.GREEN
text_blue=Fore.BLUE

print("     ")
print("     ")
print("     ")
print(text_green+"                     .~?5GBBGPY!:.                                                                                                          ")
print(text_green+"                  ^P&@@@@@@@@@@@@@B?.                                                                                                       ")
print(text_green+"                7&@@@@@@@@@@@@@@@@@@@G:                                                                                                     ")
print(text_green+"               B@@@@@@@@@@@@@@@@@@@@@@@!                                                                                                    ")
print(text_green+"      .PP7.   G@@@@@@@@@@@@@@@@@@@@@@@@@:  .!J5!                                                                                            ")
print(text_green+"     .B@@@@J .@@@@@@@@@@@@@@@@@@@@@@@@@@Y :&@@@@7                                                                                           ")
print(text_green+"    G@@@@@@@@J@@@B@@@@@@@@@@@@@@@@@@@B@@GY@@@@@@@&~                                                                                         ")
print(text_green+"    B@@@@@@@@5&@B&@@@@@@@@@@@@@@@@@@@B@@5@@@@@@@@@~     7B&&&G^    ?GP.                        ^YB&&&BGJ.       :YGPPGP                     ")
print(text_green+"     ?GBBBB&&BP&&@Y!~~!YB@@@@@G!^^~7B@B@5@&BBBBB5:     G@@G~@@@^  5@@!                .      .B@@@@&@@@@@7     B@@@@@@@              .      ")
print(text_green+"             .:5@~       G@@@!       &&^..            .@@@. B@@? G@&:        J&BBBPB@@@@&G.  B@@@@~  B@@@@:    &BB@@@@B     J&BBBP@@@@&G.  ")
print(text_green+"              !&@^      ^@@@@G.      B@P               &@@Y?@@&:B@&~P&@@@B^  G@@@@@&B@@@@@B :@@@@B   5@@@@!      5@@@@P     B@@@@@&B@@@@@B  ")
print(text_green+"              !@@&7^^!5&@7.7.B@BY7!!P@@B                JB&&BJ^B@B:&@@!^@@@. B@@@@?  !@@@@B ~@@@@P   B@@@@:      B@@@@J     B@@@@?  !@@@@B  ")
print(text_green+"               ^B@@@@@@@B :5 ^@@@@@@@@5.                     .&@B ^@@@  @@@: &@@@@   ^@@@@P .@@@@&: ?@@@@G       &@@@@!     &@@@@   ~@@@@5  ")
print(text_green+"                .~&G.G@@@5B@YB@@@~!&G^.                     ~@@G  .&@@5B@@G .@@@@&   ?@@@@Y  ^&@@@@@@@@@5        @@@@@~    .@@@@&   ?@@@@J  ")
print(text_green+"      .....^!YB@@Y@@:7&&@@@@@@@&G.P@&Y@BP?~^:....           Y5?     ?PBG5~  .55557   ^5555:    ^JPGGPY~.         Y5555.    .55557   ~5555:  ")
print(text_green+"    .&@@@@@@@@@@@!B@@&BB&B&BBB&BB@@@JG@@@@@@@@@@@J                                                                                          ")
print(text_green+"    :@@@@@@@@@&J:  B@@@&BGBBGBB@@@@!  ~G@@@@@@@@@P                                                                                          ")
print(text_green+"      Y@@@@@B~     .B@@@@@@&@@@@@@~     .J@@@@@@.                                                                                           ")
print(text_green+"      .GBBP:         !B@@@@@@@@&Y.         JBBB7                                                                                            ")
print(text_green+"                       .^^^~~^.                                                                                                             ")
print("    ")
print("    ")
print(text_blue +"✗ Power by %n01n ")
print("    ")
print("    ")
print("✚ List of subroutines :")
print("    ")
print("⮩  1 - My ip")
print("⮩  2 - IP Finder")
print("    ")
x=(int(input("✚ Enter the number opposite the desired program : ")))


if x==1:
    flammaIP = socket.gethostname()
    IP_Address= socket.gethostbyname(flammaIP)
    print(Fore.GREEN+f"IP Address : {IP_Address}")
    return1 = input("click R to return to main menu ")
    if return1 ==  "r" or "R" :
        click.clear()
        import batman

    else:
        sys.exit()

elif x==2:
    click.clear()
    import ip_t.py
    sys.exit()

else :
    click.clear()
    print("wrong number !")
    print("wrong number !")
    sys.exit()