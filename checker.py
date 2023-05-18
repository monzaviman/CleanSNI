import alpn_checker
import get_cert_info
import websocket
from json import loads
from requests import post
from threading import Thread


BOT_TOKEN = ''
CHAT_ID = ''


def send_to_telegram(domain: str):
    html_message = f"NEW SNI \n{domain}"
    post_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": html_message,
        "parse_mode": "HTML"
    }

    try:
        post(post_url, data=payload)

        with open("SNI.txt", "a+") as file:
            file.write(f"{domain}\n")

    except:
        pass


def checker(domains: list):
    for domain in domains:
        if alpn_checker.check_alpn_h2_support(domain):
            cipher_algo = get_cert_info.get_cipher_algorithm(domain)

            if cipher_algo is dict:
                if "AES_128" in cipher_algo["Algorithm"] and "1.3" in cipher_algo["TLS_Version"]:
                    send_to_telegram(domain)
                    return


def check_issuer(response: dict):
    # if "google" in response["leaf_cert"]["extensions"]["authorityInfoAccess"]:
    if "google" in response["source"]["name"]:
        checker(response["leaf_cert"]["all_domains"])


def connection():
    url = "ws://188.165.126.234:8765"
    ws = websocket.create_connection(url)

    ws.recv()
    key = get_key()
    ws.send(key)
    code = ws.recv()

    if code == "200":
        print("connect")
        while True:
            response = loads(ws.recv())

            # multi threading mode
            # thread = Thread(target=check_issuer, args=(response, ))
            # thread.start()

            # single thread mode
            check_issuer(response)
    else:
        print("can't connect to socket")
        exit(1)


def get_key():
    with open("key.txt", "r") as file:
        return file.read().strip()


if __name__ == "__main__":
    connection()
