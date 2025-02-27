# Winget Backup Script

Este é um script Python para **fazer backup dos programas instalados usando o Windows Package Manager (`winget`)** e gerar um script `.bat` para reinstalar esses programas após uma formatação ou migração de sistema.

---

## 📌 Funcionalidades

✔ Lista os programas instalados via `winget`.  
✔ Filtra corretamente os nomes e IDs dos aplicativos.  
✔ Gera um arquivo `install_apps.bat` para reinstalar os programas automaticamente.  
✔ Solicita ao usuário se deseja reiniciar o computador após a instalação.

---

## 📂 Estrutura do Projeto

```
📦 winget-backup  
 ├── 📜 winget-backup.py  # Script principal  
 ├── 📜 install_apps.bat  # Arquivo gerado para reinstalar programas  
 └── 📜 README.md         # Documentação  
```

---

## 🚀 **Pré-requisitos**

Antes de rodar o script, certifique-se de que:

### 1️⃣ **Python 3.x instalado**
- Verifique sua versão do Python:
  ```sh
  python --version
  ```
- Se não tiver instalado, baixe o **[Python aqui](https://www.python.org/downloads/)**.

### 2️⃣ **Winget instalado**
- O `winget` precisa estar disponível no sistema:
  ```sh
  winget --version
  ```
- Se não tiver, siga as **[instruções oficiais](https://learn.microsoft.com/pt-br/windows/package-manager/winget/)**.

### 3️⃣ **Executar o terminal como Administrador**
O `winget` exige permissões elevadas para instalar aplicativos.

---

## ▶ **Como Usar**

### 📌 **Passo 1: Executar o script**
Abra um terminal **(cmd, PowerShell ou Terminal do Windows)** e rode:
```sh
python winget-backup.py
```

### 📌 **Passo 2: Gerar o arquivo de instalação**
Após a execução, o script criará um arquivo chamado `install_apps.bat` contendo os comandos para reinstalar os programas.

### 📌 **Passo 3: Executar o script gerado**
Quando precisar reinstalar os programas, basta rodar:
```sh
install_apps.bat
```
O script instalará todos os programas automaticamente.

### 📌 **Passo 4: Escolher se deseja reiniciar**
No final, o script perguntará:
```
Deseja reiniciar o computador agora? (S/N)
```
Se escolher `S`, o sistema será reiniciado imediatamente.

---

## 🛠 **Detalhes Técnicos**

O script tem duas funções principais:

### 📌 **1. `get_installed_programs()`**
- Executa `winget list` e captura os programas instalados.
- Filtra corretamente o **nome** e o **app ID**.
- Remove entradas inválidas (como versões detectadas erroneamente como ID).

### 📌 **2. `generate_winget_install_script()`**
- Cria um arquivo `.bat` contendo os comandos `winget install`.
- Adiciona um prompt perguntando se o usuário deseja reiniciar o computador após a instalação.

---

## 📝 **Exemplo de Arquivo Gerado (`install_apps.bat`)**
O script criará um arquivo como este:

```bat
@echo off
echo Instalando programas via Winget...
winget install --id Notepad++.Notepad++ --accept-package-agreements --accept-source-agreements
winget install --id Google.Chrome --accept-package-agreements --accept-source-agreements
winget install --id VLC.VLC --accept-package-agreements --accept-source-agreements
echo Instalação concluída!
echo Por favor, responda 'S' para Sim ou 'N' para Não.
choice /M "Deseja reiniciar o computador agora?"
if %ERRORLEVEL% == 1 shutdown /r /t 0
```

---

## 💡 **Dicas e Soluções de Problemas**

🔹 **O `winget` não está reconhecendo os comandos?**
- Tente rodar o terminal como **Administrador**.
- Verifique se o `winget` está instalado:
  ```sh
  winget --version
  ```

🔹 **O script não está capturando todos os programas?**
- O `winget list` pode listar alguns aplicativos do Windows que não são reinstaláveis pelo `winget`.

🔹 **Como editar a lista antes de instalar?**
- Abra o arquivo `install_apps.bat` e remova as linhas dos programas que você não deseja reinstalar.

---

## 🏆 **Contribuição**

Sinta-se à vontade para melhorar o script! Se encontrar problemas ou quiser adicionar recursos, contribua.

---

🚀 **Agora você pode formatar seu PC sem perder tempo reinstalando programas!**
