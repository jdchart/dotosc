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