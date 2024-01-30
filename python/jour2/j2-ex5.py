import shutil 
  
path = "C:\\Users\\itaka\\Documents\\python"

stat = shutil.disk_usage(path) 

print("Utilisation du disque:") 
print(stat) 