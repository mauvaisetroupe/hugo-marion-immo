import os
import json
import requests

# Configuration
API_ENDPOINT = "https://api.indexnow.org/IndexNow"
API_KEY = "19cc1f2d481e483cba93ee3bd92020d6"
HOST = "www.marion-immo.lu"
KEY_LOCATION = f"https://{HOST}/{API_KEY}.txt"
PUBLIC_DIR = "public"  # Chemin vers votre site généré
BASE_URL = f"https://{HOST}"

# Fonction pour récupérer les URLs générées
def get_all_urls(base_url, directory):
    urls = []
    print("Recherche des fichiers HTML dans le dossier :", directory)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                url = f"{base_url}/{relative_path.replace(os.sep, '/')}"
                print(f"URL détectée : {url}")
                urls.append(url)
    print(f"Total des URLs collectées : {len(urls)}")
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
    # Récupérer les URLs générées
    urls = get_all_urls(BASE_URL, PUBLIC_DIR)

    # Vérifier s'il y a des URLs à envoyer
    if urls:
        print(f"\nEnvoi de {len(urls)} URL(s) à IndexNow :")
        for url in urls:
            print(f"  - {url}")
        status_code, response_text = send_urls_to_indexnow(urls)
        print(f"\nStatut de la requête : {status_code}")
        print(f"Réponse de l'API : {response_text}")
    else:
        print("Aucune URL trouvée à envoyer.")
