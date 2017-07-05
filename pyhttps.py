import argparse
import atexit
import logging
import os
import sys
import tempfile
from subprocess import call

logging.basicConfig(level=logging.INFO)

PY3 = sys.version_info[0] == 3

parser = argparse.ArgumentParser(description='')
parser.add_argument('--host', dest='host', default='localhost')
parser.add_argument('--port', dest='port', type=int, default=4443)
args = parser.parse_args()

server_host = args.host
server_port = args.port
ssl_cert_path = '{}/server.pem'.format(tempfile.gettempdir())

if PY3:
    OpenSslExecutableNotFoundError = FileNotFoundError
else:
    OpenSslExecutableNotFoundError = OSError


def create_ssl_cert():
    if PY3:
        from subprocess import DEVNULL
    else:
        DEVNULL = open(os.devnull, 'wb')

    try:
        ssl_exec_list = ['openssl', 'req', '-new', '-x509', '-keyout', ssl_cert_path,
                         '-out', ssl_cert_path, '-days', '365', '-nodes',
                         '-subj', '/CN=www.talhasch.com/O=Talhasch Inc./C=TR']
        call(ssl_exec_list, stdout=DEVNULL, stderr=DEVNULL)
    except OpenSslExecutableNotFoundError:
        logging.error('openssl executable not found!')
        exit(1)

    logging.info('Self signed ssl certificate created at {}'.format(ssl_cert_path))


def exit_handler():
    # remove certificate file
    os.remove(ssl_cert_path)

    logging.info('Bye!')


def main():
    create_ssl_cert()
    atexit.register(exit_handler)

    if PY3:
        import http.server
        import socketserver
        import ssl

        logging.info('Server running... https://{}:{}'.format(server_host, server_port))
        httpd = socketserver.TCPServer((server_host, server_port), http.server.SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile=ssl_cert_path, server_side=True)
        httpd.serve_forever()

        httpd.shutdown()
    else:
        import BaseHTTPServer
        import SimpleHTTPServer
        import ssl

        logging.info('Server running... https://{}:{}'.format(server_host, server_port))
        httpd = BaseHTTPServer.HTTPServer((server_host, server_port), SimpleHTTPServer.SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile=ssl_cert_path, server_side=True)
        httpd.serve_forever()
