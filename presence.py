from pypresence import Client
import time
import config
client_id = config.client_id
client = Client(client_id)
client.start()
client.set_activity(pid=1, state="Simping4Alvin", details= "Alvin Simp Sesh", small_image="alvin", small_text="alvin small", large_image="alvin", large_text="alvin big", start = time.time(), party_id='What goes here', party_size = [1, 50000], join="JOINHERE")
while True:
    time.sleep(15)