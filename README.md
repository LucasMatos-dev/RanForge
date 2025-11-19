# RanForge - Academic Ransomware Simulator

**⚠️ DISCLAIMER: FOR EDUCATIONAL PURPOSES ONLY ⚠️**
This project is a controlled simulation designed for cybersecurity research, academic study (Purple Teaming), and defensive training. It contains safety mechanisms to prevent execution outside designated test directories. The author is not responsible for misuse.

---

## 📋 Sobre o Projeto
O **RanForge** é um simulador de ransomware desenvolvido para demonstrar o ciclo de vida de uma ameaça criptográfica em ambiente controlado (Sandbox). O projeto foca na análise de comportamento, criptografia (AES-256) e reversibilidade (Engenharia Reversa/Forense).

### 🚀 Funcionalidades
- **Criptografia Real:** Utiliza AES-256 para bloquear arquivos.
- **Trava de Segurança:** Atua estritamente no diretório `C:\ransom_test\`.
- **Persistência:** Simulação de chaves de registro (Registry Run Keys).
- **Interface Gráfica:** GUI intimidativa para simulação de Engenharia Social.
- **Métricas Forenses:** Relatório de integridade SHA-256 pós-recuperação.

## 🛠️ Tecnologias
* Python 3.x
* Cryptography (Fernet/AES)
* Tkinter (GUI)
* PyInstaller (Binary Compilation)

## ⚙️ Como Rodar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt


2. **Gere os arquivos de teste: Execute o script auxiliar para criar dados falsos:**
    ```bash
    python dummy_gen.py

3. **Execute o Simulador:**
    ```bash
    python main.py

## 🔨 Como Compilar (Gerar o .exe)

Para transformar os scripts Python em um executável único (stand-alone) para Windows, utilizamos o **PyInstaller**.

1. Certifique-se de ter as dependências instaladas:
   ```bash
   pip install pyinstaller

2. Execute o comando de build na raiz do projeto:
   ```bash
   pyinstaller --noconsole --onefile --name "RanForge_Setup" main.py


### 📊 Arquitetura