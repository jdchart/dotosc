import dotosc
import asyncio
from utils import write_json
import os

# Set this to what you want. The file will be created in examples/usage/routing/
OUTPUT_FILE = "Routing Matrix.json"

# Get devices
connector = dotosc.XSConnect()
device_ids = asyncio.run(connector.get_devices())

# Structure data
out = {}
for i, item in enumerate(device_ids):
    out[item] = f"Device {i + 1}"

# Write to json
outpath = os.path.join(os.getcwd(), "examples", "usage", "routing")
if os.path.isdir(outpath) == False:
    os.makedirs(outpath)
write_json(os.path.join(outpath, OUTPUT_FILE), out)