import ssl
import socket

def get_cipher_algorithm(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cipher = ssock.cipher()
            return {"Algorithm":cipher[0],"TLS_Version":cipher[1]}

# Example usage
domain = 'github.com'
cipher_algorithm = get_cipher_algorithm(domain)
print(cipher_algorithm)