import os
import subprocess
from tqdm import tqdm
import time
from colorama import Fore, Back, Style, init

init()

def merge_branches(repo_path, source_branch, target_branch):
    os.chdir(repo_path)

    print(f"{Fore.GREEN}Checking out to {target_branch}...{Fore.RESET}")
    subprocess.run(["git", "checkout", target_branch])
    for i in tqdm(range(100), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Fore.RESET)):
        time.sleep(0.01)  

    print(f"{Fore.GREEN}Merging {source_branch} into {target_branch}...{Fore.RESET}")
    subprocess.run(["git", "merge", source_branch])
    for i in tqdm(range(100), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):

        time.sleep(0.01)

    print(f"{Fore.GREEN}Pushing changes to GitHub...{Fore.RESET}")
    subprocess.run(["git", "push", "origin", target_branch])
    for i in tqdm(range(100), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):

        time.sleep(0.01)

config_path = os.path.expanduser("~/.config")

source_branch = "master"

target_branch = "main"

merge_branches(config_path, source_branch, target_branch)