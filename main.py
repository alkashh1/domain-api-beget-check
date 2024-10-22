import subprocess
import shutil
import os
import time

# Путь к папке src
src_folder = "src"

# Список скриптов для последовательного запуска
scripts = [
    "all get.py",
    "filter date.py",
    "convert list to json.py",
    "list price renew.py"
]

# Запускаем каждый скрипт по порядку
for script in scripts:
    script_path = os.path.join(src_folder, script)
    print(f"Запускаем {script_path}...")
    subprocess.run(["python", script_path], check=True)

    # Задержка в 5 секунд
    # print("Ожидаем 5 секунд перед запуском следующего скрипта...")
    # time.sleep(5)

# Перемещение файла end.txt в корневую папку
end_file_src = os.path.join(src_folder, "end.txt")
end_file_dest = os.path.join(os.getcwd(), "end.txt")  # Перемещение в корень текущей директории

# Проверяем, существует ли файл end.txt
if os.path.exists(end_file_src):
    print(f"Перемещаем {end_file_src} в {end_file_dest}")
    shutil.move(end_file_src, end_file_dest)
else:
    print(f"Файл {end_file_src} не найден.")

# Список JSON-файлов для удаления
json_files = [
    "converted_list.json",
    "domain.json",
    "zone.json",
    "id.json",
    "list.json"
]

# Удаление JSON-файлов
for json_file in json_files:
    json_file_path = os.path.join(os.getcwd(), json_file)
    if os.path.exists(json_file_path):
        print(f"Удаляем {json_file_path}...")
        os.remove(json_file_path)
    else:
        print(f"Файл {json_file_path} не найден.")

print("Все JSON-файлы успешно удалены.")
