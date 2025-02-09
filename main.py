from src import Evoke

evoke = Evoke()
    
async def main():
    await evoke.ask("Recommend 10 Python projects about machine learning and cybersecurity.")
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())