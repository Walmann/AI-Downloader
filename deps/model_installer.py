

import aria2p
from deps.classes import model_info


# Koble til aria2 RPC
ariaClient = aria2p.Client(
    host="http://localhost",
    port=6800,
    secret=""
    )

aria2 = aria2p.API(ariaClient)

def download(models: list[model_info]):
    for item in models:
        aria2.add_uris(
            [item.url],
            options={"dir": item.dir}
        )

