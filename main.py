from tqdm import tqdm
import requests

def install():
    url = "https://github.com/crosire/d3d8to9/releases/download/v1.12.0/d3d8.dll"
    response = requests.get(url, stream=True)

    with open("d3d8", "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

    return [True, "Let's steal some cars!"]