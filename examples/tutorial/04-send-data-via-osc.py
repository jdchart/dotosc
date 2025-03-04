import dotosc
import utils


# '2F7BC272-B4C1-9972-593F-A156037F1712' = 49:C7
# '862864A5-5BA3-690E-AFAB-F2BD319A1B44' = 49:D6
 
# setup osc server
osc_server = dotosc.OSCSender()
osc_server.start_server()

# create a callback function that will send data over osc:
def callback_func(obj, sender, data):
    free_acceleration = utils.encode_free_acceleration(data)[0]
    free_acceleration = str(free_acceleration)[1:-1]
    osc_server.send(f"/{obj.id}", free_acceleration.replace(",", ""))

# connect to devices:
utils.quick_connect(['A5D63906-B857-C1A4-CE7A-B3015A7528EF'], callback_func)
#utils.quick_connect(['2F7BC272-B4C1-9972-593F-A156037F1712', '862864A5-5BA3-690E-AFAB-F2BD319A1B44'], callback_func)
#utils.quick_connect(['862864A5-5BA3-690E-AFAB-F2BD319A1B44'], callback_func)