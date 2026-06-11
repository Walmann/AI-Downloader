import aria2p
import subprocess
from time import sleep

from deps.classes import model_info, Settings

print("Staring Aria2")
aria2_process = subprocess.Popen([
    "aria2c",
    "--enable-rpc",
    "--rpc-listen-port=6800",
    "--rpc-allow-origin-all",
])

sleep(1) 

def download_models(settings: Settings, models: list[model_info]):
	# Koble til aria2 RPC
	aria2 = aria2p.API(aria2p.Client(host="http://localhost", port=6800, secret=""))


	for item in models:
		download_path = settings.loc_models / item.dir
		aria2.add_uris([item.url], options={"dir": str(download_path)})
		pass
	
	
	while True:
		active_downloads = aria2.get_downloads()

		if all(d.is_complete or d.is_removed for d in active_downloads):
			print("Download finished!")
			break
		
		sleep(2)