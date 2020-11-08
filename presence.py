from pypresence import Client
import time
import config
client_id = config.client_id
client = Client(client_id)
client.start()
client.set_activity(pid=3, state="Watching Words 2020", details= "Rooting for Cloud 9", small_image="alvin", small_text="alvin small", large_image="alvin", large_text="alvin big", start = time.time(), party_id="C9VIEWPARTY", party_size = [1, 50000], join="C9WIN")
while True:

    time.sleep(15)