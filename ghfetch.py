from typing import Optional
from colorama import Fore, Back, Style, init
import typer
import requests
import json

app = typer.Typer()

init(autoreset=True)

@app.command()
def fetch(user: str, credits: Optional[bool] = False):
    # print("Github Fetch")
    if not credits:
        res = requests.get(f"https://api.github.com/users/{user}")
    
        if res.status_code >= 200 and res.status_code < 300:

            resj = json.loads(res.text)
            
            line1 = f"{Fore.GREEN}{user}{Fore.WHITE}@{Fore.GREEN}Github"
            line2 = " "
            line3 = f"{Fore.YELLOW}Website{Fore.WHITE}: {resj['blog']}"
            line4 = f"{Fore.YELLOW}Company{Fore.WHITE}: {resj['company']}"
            line5 = f"{Fore.YELLOW}Follower(s){Fore.WHITE}: {resj['followers']}"
            line6 = f"{Fore.YELLOW}Following{Fore.WHITE}: {resj['following']}"
            line7 = f"{Fore.YELLOW}Location{Fore.WHITE}: {resj['location']}"
            line8 = f"{Fore.YELLOW}Repos{Fore.WHITE}: {resj['public_repos']}"


            print(f"               .mmMMMMMMMMMMMMMmm.                  | ")            
            print(f"           .mMMMMMMMMMMMMMMMMMMMMMMMm.              | ")            
            print(f"        .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.           | ")            
            print(f"      .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.         | ")            
            print(f"    .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.       | ")            
            print(f"   MMMMMMMM'  `\"MMMMM\"\"\"\"\"\"\"MMMM\"\"`  'MMMMMMMM      | ")            
            print(f"  MMMMMMMMM                           MMMMMMMMM     | ")            
            print(f" MMMMMMMMMM:                         :MMMMMMMMMM    | {line1}")            
            print(f".MMMMMMMMMM                           MMMMMMMMMM.   | {line2}")            
            print(f"MMMMMMMMM\"                             \"MMMMMMMMM   | {line3}")            
            print(f"MMMMMMMMM                               MMMMMMMMM   | {line4}")            
            print(f"MMMMMMMMM                               MMMMMMMMM   | {line5}")            
            print(f"MMMMMMMMMM                             MMMMMMMMMM   | {line6}")            
            print(f"`MMMMMMMMMM                           MMMMMMMMMM`   | {line7}")            
            print(f" MMMMMMMMMMMM.                     .MMMMMMMMMMMM    | {line8}")            
            print(f"  MMMMMM  MMMMMMMMMM         MMMMMMMMMMMMMMMMMM     | ")            
            print(f"   MMMMMM  'MMMMMMM           MMMMMMMMMMMMMMMM      | ")            
            print(f"    `MMMMMM  \"MMMMM           MMMMMMMMMMMMMM`       | ")            
            print(f"      `MMMMMm                 MMMMMMMMMMMM`         | ")            
            print(f"        `\"MMMMMMMMM           MMMMMMMMM\"`           | ")            
            print(f"           `\"MMMMMM           MMMMMM\"`              | ")            
            print(f"               `\"\"M           M\"\"`                  | ")            
        else:
            if res.status_code == 404:
                print("User not found")
            else:
                print("Unexpected Error")
    else:
        print("Credits:")
        print("Made by woooferz")
        print("ASCII art by pi314")


def run():
    app()


if __name__ == "__main__":
    app()
