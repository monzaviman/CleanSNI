import ssl
import socket


def get_cipher_algorithm(domain: str) -> dict | bool:
    context = ssl.create_default_context()

    try:
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as s:
                cipher = s.cipher()

                return {"Algorithm":cipher[0],"TLS_Version":cipher[1]}
    except:
        return False


# Example usage
if __name__ == "__main__":
    domain = 'github.com'
    cipher_algorithm = get_cipher_algorithm(domain)
    print(cipher_algorithm)
