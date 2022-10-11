import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init']) #llama a la terminal y inicia git
subprocess.call(['git', 'add', '*']) #agrega todos los documentos del directorio a staging
subprocess.call(['git', 'commit', '-m', 'Initial commit']) #crea el primer commit con toda nuestra configuración inicial y la manda al repositorio

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")