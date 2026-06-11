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
	"--max-concurrent-downloads=5",
	"--continue=true"
])

sleep(1) 

def download_models(settings: Settings, models: list[model_info]):
	# Koble til aria2 RPC
	print("Creating Aria client")
	aria2 = aria2p.API(aria2p.Client(host="http://localhost", port=6800, secret=""))

	if not len(aria2.get_download) == 0:
		print("Clearing excisting queue.")
		try:
			for d in aria2.get_downloads():
				aria2.remove(d, force=True)
		except Exception as e: 
			print(f"Could not remove {d.gid}: {e}")


	print(f"Adding {len(models)} downloads to queue.")
	for item in models:
		download_path = settings.loc_models / item.dir
		aria2.add_uris([item.url], options={"dir": str(download_path)})
		print(f"Added {item.dir} to download queue")
		pass
	
	
	while True:
		active_downloads = aria2.get_downloads()


		for d in active_downloads:
			d.update()  # refresh status
			print(d.progress_string(), d.download_speed, d.name, d.status )
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n")
		if all(d.is_complete or d.is_removed for d in active_downloads):
			print("Download finished!")
			break
		
		sleep(2)