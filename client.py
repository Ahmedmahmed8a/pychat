import socket,_thread
print("""
┌─────────────────────────────┐
│          PyChat             │
│\    / _  |  _  _  ._ _   _  │
│ \/\/ (/_ | (_ (_) | | | (/_ │
│     github:ahmedMahmed8a    │
└─────────────────────────────┘
     Chat ba2a ya sadiqi
""")
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = str(input("$Server IP:"))
port = int(input("$Server Port:"))

conn.connect((host, port))
def rec(d):
   while(1):
    data=conn.recv(d)
    print(data.decode())
    if not data:
     break
def get():
 while(1):
  data=str(input("")).encode()
  conn.sendall(data+b"\n")
_thread.start_new_thread(rec,(1024,))
get()
