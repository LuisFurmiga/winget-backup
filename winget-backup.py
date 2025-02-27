import subprocess
import re

def is_version_format(value):
    """Verifica se a string contém apenas números, ponto, hífen e reticências."""
    return bool(re.match(r'^[0-9.\-…]+$', value))

def get_installed_programs():
    """Obtém a lista de programas instalados usando Winget."""
    try:
        result = subprocess.run(["winget", "list"], capture_output=True, text=True, check=True, encoding="utf-8")
        installed_programs = []
        for line in result.stdout.splitlines():
            columns = line.split()
            if len(columns) and columns[-1] == "winget":
                index = -2
                while is_version_format(columns[index]):
                    index -= 1
                name = " ".join(columns[:index])  # Nome do programa
                app_id = columns[index]  # ID do aplicativo
                installed_programs.append((name.strip(), app_id.strip()))
        return installed_programs
    except Exception as e:
        print(f"Erro ao obter lista de programas: {e}")
        return []

def generate_winget_install_script(installed_programs, output_file="install_apps.bat"):
    """Gera um script de instalação baseado nos programas instalados."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("@echo off\n")
        f.write("echo Instalando programas via Winget...\n")
        for name, app_id in installed_programs:
            f.write(f"winget install --id {app_id} --accept-package-agreements --accept-source-agreements\n")
        f.write("echo Instalação concluída!\n")
        f.write("echo Por favor, responda 'S' para Sim ou 'N' para Não.\n")
        f.write("choice /M \"Deseja reiniciar o computador agora?\"\n")
        f.write("if %ERRORLEVEL% == 1 shutdown /r /t 0\n")
    print(f"Script de instalação gerado: {output_file}")

if __name__ == "__main__":
    programs = get_installed_programs()
    generate_winget_install_script(programs)
