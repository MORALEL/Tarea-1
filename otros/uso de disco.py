from shutil import disk_usage
 
total, usado, libre = disk_usage("/")
print(f"Espacio total: {total // (1024**3)} GB")
print(f"Espacio libre: {libre // (1024**3)} GB")
 
 