import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = "192.168.29.179"
port = 5001
filename = "Doctor.Strange.in.the.Multiverse.of.Madness.2022.x264.900MB.HDTS - QRips.mkv"
filesize = os.path.getsize(filename)

s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True,unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
s.close()

