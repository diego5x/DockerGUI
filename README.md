# DockerGUI

O **DockerGUI** é uma aplicação desenvolvida em Python com interface gráfica para facilitar o gerenciamento de containers Docker. A ideia é permitir iniciar, parar, visualizar status ou logs e realizar outras operações básicas de containers de forma visual.

Este projeto serve como estudo prático de desenvolvimento de interfaces gráficas usando Qt/PyQt.

---

## Pré‑Requisitos

- ✅ Python 3
- ✅ Docker instalado e rodando no seu sistema
- ✅ Permissões para acessar o **docker.sock** (geralmente executando com permissões de administrador ou adicionando seu usuário ao grupo Docker)

---

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/diego5x/DockerGUI.git
   ```

2. Entre no diretório:

   ```bash
   cd DockerGUI
   ```

3. Instale dependências:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Usar

Execute o programa principal com Python:

```bash
python3 main.py
```

Isso deve abrir a interface gráfica do **DockerGUI**. A partir dela você poderá:

* Listar containers
* Iniciar/Parar containers
* Visualizar status

---
