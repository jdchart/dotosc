import dotosc
import utils
import os
import asyncio

# Get routing matrix:
ROUTING_MATRIX_PATH = os.path.join(os.getcwd(), "examples", "usage", "routing", "Routing Matrix.json")
routing_matrix = utils.read_json(ROUTING_MATRIX_PATH)

device_list = []
for item in routing_matrix:
    device_list.append(dotosc.XSConnect(id = item))
async def connect_all():
    await asyncio.gather(*(device.discover_characteristics() for device in device_list))
asyncio.run(connect_all())
