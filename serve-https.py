"""Serve this folder over HTTPS so phones on the same Wi-Fi can use the camera.

Usage: python3 serve-https.py [port]
Generates a self-signed certificate in .cert/ if one doesn't exist yet.
"""
import http.server, os, socket, ssl, subprocess, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8443
HERE = os.path.dirname(os.path.abspath(__file__))
CERT, KEY = os.path.join(HERE, ".cert/cert.pem"), os.path.join(HERE, ".cert/key.pem")

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()

ip = lan_ip()
if not os.path.exists(CERT):
    os.makedirs(os.path.dirname(CERT), exist_ok=True)
    subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "365",
                    "-keyout", KEY, "-out", CERT, "-subj", "/CN=foggy-webcam",
                    "-addext", f"subjectAltName=IP:{ip},DNS:localhost"], check=True)

os.chdir(HERE)
httpd = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(CERT, KEY)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
print(f"Open on your phone:  https://{ip}:{PORT}")
print("Your browser will warn about the certificate - choose to continue anyway.")
httpd.serve_forever()
