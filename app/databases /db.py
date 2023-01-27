from tortoise import Tortoise 

async def connectToDatabase():
    await Tortoise.init(
        db_url = 'mysql://root:@127.0.0.1:33306/trello',
        modules = {'models':['app.models']}
    )
    