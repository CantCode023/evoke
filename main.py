from src import Evoke
from rich import print as rprint
from rich.pretty import pprint
import os

evoke = Evoke()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
async def main():
    clear()
    
    MENU = """[bright_white]:::::::::: :::     :::  ::::::::  :::    ::: :::::::::: 
:+:        :+:     :+: :+:    :+: :+:   :+:  :+:        
+:+        +:+     +:+ +:+    +:+ +:+  +:+   +:+        
+#++:++#   +#+     +:+ +#+    +:+ +#++:++    +#++:++#   
+#+         +#+   +#+  +#+    +#+ +#+  +#+   +#+        
#+#          #+#+#+#   #+#    #+# #+#   #+#  #+#        
##########     ###      ########  ###    ### ##########[/bright_white]
[bright_black]Evoking excitement..[/bright_black]

type TERMINATE to exit.."""

    rprint(MENU)
    
    task = input("[:] ")
    if task == "TERMINATE":
        return 0
    else:
        result = await evoke.ask(task_message=task)
        pprint(result)
        print("Press enter to continue...")
        input()
        return 1
    
if __name__ == "__main__":
    import asyncio
    result = 1
    while result:
        result = asyncio.run(main())