import ssl
import socket

def check_alpn_h2_support(domain):
    context = ssl.create_default_context()
    context.set_alpn_protocols(['h2', 'http/1.1'])

    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            negotiated_protocol = ssock.selected_alpn_protocol()
            return negotiated_protocol == 'h2'

# Example usage
domain = 'mail.google.com'
supports_alpn_h2 = check_alpn_h2_support(domain)
print(f"ALPN H2 Support: {supports_alpn_h2}")