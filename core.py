from requests import get, post
from socket import socket, AF_INET, SOCK_STREAM
from ssl import wrap_socket
import json

HEADERS = {"User-Agent": "htbapi"}
BASE = "http://hackthebox.eu/api"

def getRequest(url: str, apitoken: str) -> str:
    return get(f"{BASE}{url}?api_token={apitoken}", headers=HEADERS)

def rawPostSSL(url: str, data: str, apitoken: str, datatype: str, recvstop: str) -> bytes:
    if not datatype == "":
        ct = f"Content-Type: application/{datatype}\r\nContent-Length: {len(data)}\r\n"
    else:
        ct = ""
    ws = wrap_socket(socket(AF_INET, SOCK_STREAM), server_side=False)
    ws.connect(("www.hackthebox.eu", 443))
    request = f"POST /api{url}?api_token={apitoken} HTTP/1.1\r\nHost: www.hackthebox.eu\r\nUser-Agent: htbapi\r\n{ct}\r\n{data}\r\n"
    ws.send(request.encode())
    data = b""
    if not recvstop == "":
        while True:
            tdata = ws.recv(1024)
            data += tdata
            if recvstop.encode() in tdata:
                break
    else:
        data += ws.recv(1024)
    return data










