from src import Evoke

evoke = Evoke()
    
async def main(task: str):
    await evoke.ask(task)
    
if __name__ == "__main__":
    import asyncio
    task = input("[:] ")
    asyncio.run(main(task))