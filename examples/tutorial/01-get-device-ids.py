import dotosc
import asyncio

# xsens connector class instance:
connector = dotosc.XSConnect()

# run a bluetooth search for movella devics:
device_ids = asyncio.run(connector.get_devices())

# print the ids of each device:
print(device_ids)