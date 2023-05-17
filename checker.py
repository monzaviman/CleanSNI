import alpn_checker
import get_cert_info

def send_to_telegram():
    pass

def get_domains():
    #connect to Cert-WebSocket


    #Filter function for getting only Google-Certificate-Issuer

    if (alpn_checker.check_alpn_h2_support() == True) and (get_cert_info.get_cipher_algorithm() == True):
        send_to_telegram()


get_domains()

