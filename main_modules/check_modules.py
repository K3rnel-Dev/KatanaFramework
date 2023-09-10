import importlib.util
import subprocess
from rich.console import Console
from time import sleep
console = Console()
console.print('''[bold red]
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠄⠄⠈⠙⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿
⣿⣿⣿⣿⡿⠃⠄⠄⠄⢀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠈⢿
⣿⣿⣿⡟⠄⠄⠄⠄⠐⢻⣿⣿⣿⣷⡄⠄⠄⠄⠄⠄⠄⠈
⣿⣿⣿⠃⠄⠄⠄⢀⠴⠛⠙⣿⣿⡿⣿⣦⠄⠄⠄⠄⠄⠄
⣿⣿⠃⠄⢠⡖⠉⠄⠄⠄⣠⣿⡏⠄⢹⣿⠄⠄⠄⠄⠄⢠
⣿⠃⠄⠄⢸⣧⣤⣤⣤⢾⣿⣿⡇⠄⠈⢻⡆⠄⠄⠄⠄⣾
⠁⠄⠄⠄⠈⠉⠛⢿⡟⠉⠉⣿⣷⣀⠄⠄⣿⡆⠄⠄⢠⣿
⠄⠄⠄⠄⠄⠄⢠⡿⠿⢿⣷⣿⣿⣿⣿⣿⠿⠃⠄⠄⣸⣿
⠄⠄⠄⠄⠄⢀⡞⠄⠄⠄⠈⣿⣿⣿⡟⠁⠄⠄⠄⠄⣿⣿
⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⢀⣿⣿⡟⠄⠄⠄⠄⠄⢠⣿⣿
⠄⠄⠄⠄⠄⠘⠄⠄⠄⢀⡼⠛⠉⠄⠄⠄⠄⠄⠄⣼⣿⣿
⠄⠄⠄⠄⠄⡇⠄⠄⢀⠎⠄⠄⠄⠄CHECKING
⠄⠄⠄⠄⢰⠃⠄⢀⠎⠄⠄⠄Dependeces⠄⠄⠄⣿⣿
[/bold red]''')
modules_to_check = [
    "colorama",
    "psutil",
    "click",
    "phonenumbers",
    "pystyle",
    "urllib3",
    "readchar",
    "netifaces",
    "pyperclip",
    "rich"
]
nc_utility = "nc"


def check_module(module_name):
    spec = importlib.util.find_spec(module_name)
    return spec is not None

def check_nc_utility():
    try:
        subprocess.run(["nc", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def main():
    missing_modules = [module for module in modules_to_check if not check_module(module)]

    nc_installed = check_nc_utility()

    for module in modules_to_check:
        checkbox = "[green]✓[/green]" if check_module(module) else "[red]✗[/red]"
        console.print(f":skull:{module}: {checkbox}")

    nc_checkbox = "[green]✓[/green]" if nc_installed else "[red]✗[/red]"
    console.print(f":skull:netcat: {nc_checkbox}")

    if missing_modules or not nc_installed:
        console.print(":vampire:[bold red]Please[/bold red] install the necessary libraries to run the script! :vampire:")
        if missing_modules:
            console.print(f":skull:You need to install the following libraries: {', '.join(missing_modules)}.")
        if not nc_installed:
            console.print("The 'nc' utility (netcat) needs to be installed.")

        install_choice = input("Want to install missing items? (y/n): ")
        if install_choice.lower() == "y":
            if missing_modules:
                subprocess.run(["pip", "install"] + missing_modules)
            if not nc_installed:
                console.print("[bold red]Install the 'nc' (netcat) utility using your package manager.[/bold red]")
        else:
            console.print("[bold red]You have chosen not to use the missing elements. The script may not work without them.[/bold red]")

    sleep(3)