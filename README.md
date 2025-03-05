# dotosc
Python bridge for Movella Xsens DOT for sending IMU data over OSC

> [!WARNING]
> Make sure that your sensors are set to no higher than 60 Hz (this blocks real-time transmission).

## Usage

If you clone this repo, you'll have to install the package with `pip install .`.

Otherwise you can run a `pip install git+https://github.com/jdchart/dotosc.git`

### 1. Create a "routing matrix" like this:

```python
import dotosc
import asyncio
from utils import write_json
import os

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
```

This will detect all currently available devices (sometimes you may need to run the script a few times if there are many sensors) and create a file keeping track of their uuids and give them a generic osc adresse "Device x" (this can be modified in the script or in the resulting file).

### 2. Connect sensor and sen dover osc

```python
import dotosc
import utils
import os

# Get routing matrix:
ROUTING_MATRIX_PATH = os.path.join(os.getcwd(), "examples", "usage", "routing", "Routing Matrix.json")
routing_matrix = utils.read_json(ROUTING_MATRIX_PATH)

# Start OSC server:
osc_server = dotosc.OSCSender()
osc_server.start_server()

# Callback for sending data:
def callback_func(obj, sender, data):
    
    free_acceleration = utils.encode_free_acceleration(data)[0]
    free_acceleration = str(free_acceleration)[1:-1]
    osc_server.send(f"/{routing_matrix[obj.id]}", free_acceleration.replace(",", ""))

# Connect to devices:
device_list = []
for item in routing_matrix:
    device_list.append(item)
utils.quick_connect(device_list, callback_func)
```