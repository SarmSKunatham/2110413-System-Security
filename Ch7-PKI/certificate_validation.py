from OpenSSL import crypto
import pem

def verify_chain_of_trust(cert_pem, trusted_cert_pems):
    print("Loading server certificate.")
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
    
    store = crypto.X509Store()
    print("Loading trusted CA certificates.")
    for trusted_cert_pem in trusted_cert_pems:
        trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, trusted_cert_pem)
        store.add_cert(trusted_cert)
    
    print("Verifying the chain of trust...")
    store_ctx = crypto.X509StoreContext(store, certificate)
    try:
        store_ctx.verify_certificate()
        print("Verification successful: The certificate chain is trusted.")
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False

def verify():
    with open('server_cert_dir/twitter_com.cert', 'r') as cert_file:
        cert = cert_file.read()
    with open('server_cert_dir/intermediate.pem', 'r') as int_cert_file:
        int_cert = int_cert_file.read()
    
    pems = pem.parse_file('server_cert_dir/ca-certificates.crt')
    trusted_certs = [str(mypem) for mypem in pems]
    trusted_certs.append(int_cert)
    
    print("Preparing to verify the server's certificate...")
    verified = verify_chain_of_trust(cert, trusted_certs)
    if verified:
        print('Certificate verified.')
    else:
        print('Certificate not verified.')

if __name__ == '__main__':
    print('Starting certificate verification process...')
    verify()
