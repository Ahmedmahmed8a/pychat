import socket,_thread

HOST = ''
PORT = 8080
#######################•
# Github:ahmedMahmed8a |
#  enjoy the code (;   |
#######################•
g="\x1b[92m"
r="\x1b[91m"
n="\x1b[0m"
print(f"""
┌────────────────────────────┐
│              _         _   │
│ _ __ _  _ __| |_  __ _| |_ │
│| '_ \ || / _| ' \/ _` |  _|│
│| .__/\_, \__|_||_\__,_|\__|│
│|_|   |__/ %sahmed%sM%sahmed8a%s    │
└────────────────────────────┘""" %(g,r,g,n))
print("[+] Starting the server on port",PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 print("[*] Binding")
 s.bind((HOST, PORT))
 print("[/] Waiting for the client")
 s.listen()
 print("[•] Accepting the connection")
 conn, addr = s.accept()
 with conn:
  print("The user:",addr,"Joined the chat")
  conn.send(b"Welcome yasta :)\x0a")
  conn.send(b"MSG:\n")
  def rec(d):
   while(1):
    data=conn.recv(d)
    print(addr,":",data.decode())
    if not data:
     break
    conn.send(b"S\nMSG:")
  def get():
   while(1):
    data=str(input("MSG> ")).encode()
    conn.sendall(b"[Admin]:"+data+b"\n")
  _thread.start_new_thread(rec,(1024,))
  get()
