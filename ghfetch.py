from typing import Optional
from colorama import Fore, Back, Style, init
import typer
import requests
import json

app = typer.Typer()

init(autoreset=True)

@app.command()
def fetch(user: str, credits: Optional[bool] = False, repo: Optional[str] = None):
    # print("Github Fetch")
    if not credits and repo is None:
        try:
            res = requests.get(f"https://api.github.com/users/{user}")
        except requests.exceptions.ConnectionError:
            print("Connection Error!")
            return
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

            if user == "woooferz":
                line9 = f"| {Fore.BLUE}(Creator of ghfetch)"
            else:
                line9 = ""

            print(f"               .mmMMMMMMMMMMMMMmm.                   ")            
            print(f"           .mMMMMMMMMMMMMMMMMMMMMMMMm.               ")            
            print(f"        .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.            ")            
            print(f"      .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.          ")            
            print(f"    .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.        ")            
            print(f"   MMMMMMMM'  `\"MMMMM\"\"\"\"\"\"\"MMMM\"\"`  'MMMMMMMM       ")            
            print(f"  MMMMMMMMM                           MMMMMMMMM      ")            
            print(f" MMMMMMMMMM:                         :MMMMMMMMMM    | {line1}")            
            print(f".MMMMMMMMMM                           MMMMMMMMMM.   | {line2}")            
            print(f"MMMMMMMMM\"                             \"MMMMMMMMM   | {line3}")            
            print(f"MMMMMMMMM                               MMMMMMMMM   | {line4}")            
            print(f"MMMMMMMMM                               MMMMMMMMM   | {line5}")            
            print(f"MMMMMMMMMM                             MMMMMMMMMM   | {line6}")            
            print(f"`MMMMMMMMMM                           MMMMMMMMMM`   | {line7}")            
            print(f" MMMMMMMMMMMM.                     .MMMMMMMMMMMM    | {line8}")            
            print(f"  MMMMMM  MMMMMMMMMM         MMMMMMMMMMMMMMMMMM     {line9}")            
            print(f"   MMMMMM  'MMMMMMM           MMMMMMMMMMMMMMMM       ")            
            print(f"    `MMMMMM  \"MMMMM           MMMMMMMMMMMMMM`        ")            
            print(f"      `MMMMMm                 MMMMMMMMMMMM`          ")            
            print(f"        `\"MMMMMMMMM           MMMMMMMMM\"`            ")            
            print(f"           `\"MMMMMM           MMMMMM\"`               ")            
            print(f"               `\"\"M           M\"\"`                   ")            
        else:
            if res.status_code == 404:
                print("User not found")
            else:
                print("Unexpected Error")
    elif credits == True:
        print("Credits:")
        print("Made by woooferz")
        print("ASCII art by pi314")
    elif repo is not None:
        try:
            res = requests.get(f"https://api.github.com/repos/{user}/{repo}")
        except requests.exceptions.ConnectionError:
            print("Connection Error!")
            return
        if res.status_code >= 200 and res.status_code < 300:

            resj = json.loads(res.text)
            
            line1 = f"{Fore.GREEN}{resj['name']}{Fore.WHITE}@{Fore.GREEN}Github-Repo"
            line2 = " "
            line3 = f"{Fore.YELLOW}Owner{Fore.WHITE}: {resj['owner']['login']}"
            line4 = f"{Fore.YELLOW}License{Fore.WHITE}: {resj['license']['name']}"

            line5 = f"{Fore.YELLOW}Star(s){Fore.WHITE}: {resj['stargazers_count']}"
            line6 = f"{Fore.YELLOW}Fork(s){Fore.WHITE}: {resj['forks']}"
            line7 = f"{Fore.YELLOW}URL{Fore.WHITE}: {resj['html_url']}"
            line8 = f"{Fore.YELLOW}Homepage{Fore.WHITE}: {resj['homepage']}"

            if user == "woooferz" and repo == "ghfetch":
                line9 = f"| {Fore.BLUE}(Repo of this)"
            else:
                line9 = ""

            print(f"               .mmMMMMMMMMMMMMMmm.                   ")            
            print(f"           .mMMMMMMMMMMMMMMMMMMMMMMMm.               ")            
            print(f"        .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.            ")            
            print(f"      .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.          ")            
            print(f"    .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.        ")            
            print(f"   MMMMMMMM'  `\"MMMMM\"\"\"\"\"\"\"MMMM\"\"`  'MMMMMMMM       ")            
            print(f"  MMMMMMMMM                           MMMMMMMMM      ")            
            print(f" MMMMMMMMMM:                         :MMMMMMMMMM    | {line1}")            
            print(f".MMMMMMMMMM                           MMMMMMMMMM.   | {line2}")            
            print(f"MMMMMMMMM\"                             \"MMMMMMMMM   | {line3}")            
            print(f"MMMMMMMMM                               MMMMMMMMM   | {line4}")            
            print(f"MMMMMMMMM                               MMMMMMMMM   | {line5}")            
            print(f"MMMMMMMMMM                             MMMMMMMMMM   | {line6}")            
            print(f"`MMMMMMMMMM                           MMMMMMMMMM`   | {line7}")            
            print(f" MMMMMMMMMMMM.                     .MMMMMMMMMMMM    | {line8}")            
            print(f"  MMMMMM  MMMMMMMMMM         MMMMMMMMMMMMMMMMMM     {line9}")            
            print(f"   MMMMMM  'MMMMMMM           MMMMMMMMMMMMMMMM       ")            
            print(f"    `MMMMMM  \"MMMMM           MMMMMMMMMMMMMM`        ")            
            print(f"      `MMMMMm                 MMMMMMMMMMMM`          ")            
            print(f"        `\"MMMMMMMMM           MMMMMMMMM\"`            ")            
            print(f"           `\"MMMMMM           MMMMMM\"`               ")            
            print(f"               `\"\"M           M\"\"`                   ")            
        else:
            if res.status_code == 404:
                print("Repo not found")
            else:
                print("Unexpected Error")


def run():
    app()


if __name__ == "__main__":
    app()
