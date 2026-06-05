import shutil
import os
import schedule
import time

def backup():
    source_folder = "C:\\xampp2\\mysql\\data"  # Ruta de la carpeta que deseas respaldar
    backup_folder = "E:\\"  # Ruta donde se guardará el respaldo

    # Genera un nombre de carpeta basado en la fecha y hora actual para que cada respaldo sea único
    backup_name = time.strftime("%Y%m%d-%H%M%S")
    backup_path = os.path.join(backup_folder, backup_name)

    # Copia la carpeta
    shutil.copytree(source_folder, backup_path)
    print(f"Backup realizado con éxito en {backup_path}")

# Planifica el respaldo para que se ejecute a las 10 AM, 2 PM y 7 PM
schedule.every().day.at("10:00").do(backup)
schedule.every().day.at("14:00").do(backup)
schedule.every().day.at("19:00").do(backup)

print("El servicio de respaldo está programado. Esperando para ejecutar tareas...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Espera un minuto entre cada chequeo
