import os
import time
import json
import requests

# Configuration
API_ENDPOINT = "https://api.indexnow.org/IndexNow"
API_KEY = "19cc1f2d481e483cba93ee3bd92020d6"
HOST = "www.marion-immo.lu"
KEY_LOCATION = f"https://{HOST}/{API_KEY}.txt"
PUBLIC_DIR = "public"  # Chemin vers votre site généré
BASE_URL = f"https://{HOST}"
LAST_RUN_FILE = "lastrun_timestamp.txt"  # Fichier pour stocker la dernière exécution

# Fonction pour lire le timestamp de la dernière exécution
def get_last_run_time():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as f:
            return float(f.read().strip())
    return 0

# Fonction pour enregistrer le timestamp actuel
def save_last_run_time(timestamp):
    with open(LAST_RUN_FILE, "w") as f:
        f.write(str(timestamp))

# Fonction pour récupérer les URLs générées depuis la dernière exécution
def get_modified_urls(base_url, directory, last_run_time):
    urls = []
    print("Recherche des fichiers HTML modifiés depuis le dernier run :", time.ctime(last_run_time))
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                # Vérifie si le fichier a été modifié après le dernier run
                if os.path.getmtime(file_path) > last_run_time:
                    relative_path = os.path.relpath(file_path, directory)
                    url = f"{base_url}/{relative_path.replace(os.sep, '/')}"
                    print(f"URL détectée (modifiée) : {url}")
                    urls.append(url)
    print(f"Total des URLs modifiées : {len(urls)}")
    return urls

# Fonction pour envoyer les URLs à IndexNow
def send_urls_to_indexnow(urls):
    payload = {
        "host": HOST,
        "key": API_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    print("Envoi des URLs à IndexNow...")
    response = requests.post(API_ENDPOINT, data=json.dumps(payload), headers=headers)
    return response.status_code, response.text

# Script principal
if __name__ == "__main__":
    # Récupérer le timestamp de la dernière exécution
    last_run_time = get_last_run_time()
    current_time = time.time()

    # Récupérer les URLs modifiées
    urls = get_modified_urls(BASE_URL, PUBLIC_DIR, last_run_time)

    # Vérifier s'il y a des URLs à envoyer
    if urls:
        print(f"\nEnvoi de {len(urls)} URL(s) à IndexNow :")
        for url in urls:
            print(f"  - {url}")
        status_code, response_text = send_urls_to_indexnow(urls)
        print(f"\nStatut de la requête : {status_code}")
        print(f"Réponse de l'API : {response_text}")
    else:
        print("Aucune URL modifiée depuis le dernier run.")

    # Sauvegarder le timestamp de cette exécution
    save_last_run_time(current_time)
