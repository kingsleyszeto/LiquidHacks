from pypresence import Client
import time
import config
def foo(x):
    print("AHHH")
    print("Hello there")
client_id = config.client_id
client = Client(client_id)

client.start()
client.register_event("ACTIVITY_JOIN", foo, args={'cmd': "DISPATCH", 'data': {'secret': "BEEPUBEEP"}, "evt": "ACTIVITY_JOIN"})
a = client.set_activity(pid=0, state="Watching Worlds 2020", details= "Rooting for Team Liquid", small_image="alvin", small_text="alvin small", large_image="alvin", large_text="alvin big", start = time.time(), party_size=[1,10000], party_id='TLVIEWPARTY20AA', join="TLWIN")
print(a)
while True:
    time.sleep(1)
    a = client.loop.run_until_complete(client.read_output())
    print(a)
    if a['evt'] == 'ACTIVITY_JOIN':
        client.set_activity(pid=0, state="Watching Worlds 2020", details= "Rooting for Team Liquid", small_image="alvin", small_text="alvin small", large_image="alvin", large_text="alvin big", start = time.time(), party_size=[1,10000], party_id='C9VIEWPARTY', join=a['data']['secret'])
    # print(client.sock_reader.feed_data)
