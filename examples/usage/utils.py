import os
import json
import numpy as np
import dotosc
import asyncio

def read_json(path : str) -> dict:
    """Donner le chemin vers un fichier json et retourner un dict."""
    if os.path.isfile(path):
        if os.path.splitext(path)[1].lower() == ".json":
            with open(path, 'r') as f:
                return json.load(f)
        else:
            print("Erreur ! Il ne s'agit pas d'un fichier json !")
    else:
        print("Erreur ! Le fichier n'existe pas !")

def write_json(path : str, content : dict, indent : int = 4) -> None:
    """
    Donner un chemin de destination et du contenu et enregistrer au format json.
    
    Si le dossier n'existe pas, cette fonction créera le dossier de manière récursive.
    """
    if os.path.splitext(path)[1] == ".json":
        check_dir_exists(path)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii = False, indent = indent)
    else:
        print("Erreur ! Il faut donner un fichier avec une extension \"json\" !")


def check_dir_exists(filepath):
    """Check if folder exists, if not, create it."""
    if os.path.isdir(os.path.dirname(filepath)) == False:
        os.makedirs(os.path.dirname(filepath))

def encode_free_acceleration(bytes_):
    data_segments = np.dtype([
        ('timestamp', np.uint32),
        ('x', np.float32),
        ('y', np.float32),
        ('z', np.float32),
        ('zero_padding', np.uint32)
        ])
    formatted_data = np.frombuffer(bytes_, dtype=data_segments)
    return formatted_data

def quick_connect(ids, callback):
    devices = []
    for id in ids:
        devices.append(dotosc.XSConnect(id = id, callback = callback))
    async def connect_all():
        await asyncio.gather(*(device.connect_device() for device in devices))
    asyncio.run(connect_all())