from src import Evoke
from rich import print as rprint
import os

import asyncio
import nest_asyncio
nest_asyncio.apply()

evoke = Evoke()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
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
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(evoke.ask(task_message=task))
        except:
            loop.close()
        finally:
            loop.close()
        print("Press enter to continue...")
        input()
        return 1
    
if __name__ == "__main__":
    result = 1
    while result:
        result = main()