import socket
import platform

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
OSname = platform.system()
processor = platform.processor()
 
print("Nom PC: " + hostname)
print("IP: " + IPAddr)
print("OS : " + OSname)
print("processeur : " + processor)