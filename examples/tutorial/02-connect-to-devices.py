import dotosc
import asyncio
import utils

# movella ids (found using the first example):
ids = ['C8973990-73A7-69EC-F21E-BFC8A82FA281']

# create a callback function that will handle the data:
def callback_func(obj, sender, data):
    free_acceleration = utils.encode_free_acceleration(data)[0]
    free_acceleration = str(free_acceleration)[1:-1]
    print(f"{obj.id}: {free_acceleration}")

# create connector instance for each id:
devices = []
for id in ids:
    devices.append(dotosc.XSConnect(id = id, callback = callback_func))

# connect to each device:
async def connect_all():
    await asyncio.gather(*(device.connect_device() for device in devices))
asyncio.run(connect_all())

# to quit, use ctrl+c