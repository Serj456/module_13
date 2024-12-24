import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for number_ball in range(1,6):
        wait_ = 7-power
        await asyncio.sleep(wait_)
        print(f'Силач {name} поднял {number_ball} шар')
    print(f'Силач {name} закончил соревнование')

async def start_tournament():
     task1 = asyncio.create_task(start_strongman('pasha',3))
     task2 = asyncio.create_task(start_strongman('denis', 4))
     task3 = asyncio.create_task(start_strongman('appolon',5))
     await task1
     await task2
     await task3

asyncio.run(start_tournament())

