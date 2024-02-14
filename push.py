import os
import subprocess
from tqdm import tqdm
import time
from colorama import Fore, Back, Style, init

init()

def push_to_github(repo_path, commit_message, branch):
    os.chdir(repo_path)

    subprocess.run(["git", "add", "."])
    print(f"{Fore.GREEN}Adding changes to staging area...{Fore.RESET}")
    for i in tqdm(range(100), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Fore.RESET)):
        time.sleep(0.01)  

    subprocess.run(["git", "commit", "-m", commit_message])
    print(f"{Fore.GREEN}Commiting changes...{Fore.RESET}")
    for i in tqdm(range(100), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
        time.sleep(0.01)  

    subprocess.run(["git", "push", "origin", branch])
    print(f"{Fore.GREEN}Pushing changes to GitHub...{Fore.RESET}")
    for i in tqdm(range(100), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
        time.sleep(0.01)  

config_path = os.path.expanduser("~/.config")

commit_message = "Update config"

branch = "master"

push_to_github(config_path, commit_message, branch)