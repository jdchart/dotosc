import dotosc

# create instance of osc sender:
osc_server = dotosc.OSCSender(
    ip = "127.0.0.1",
    port = 12345
)

# start server:
osc_server.start_server()

# send a test message:
osc_server.send("/test", 123)