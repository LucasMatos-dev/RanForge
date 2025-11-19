import os
import random
import string

# --- CONFIGURAÇÃO ---
# Diretório alvo OBRIGATÓRIO. O ransomware só pode tocar aqui.
TARGET_DIR = r"C:\ransom_test"
NUM_FILES = 50  # Quantidade de arquivos para gerar

def create_dummy_files():
    # 1. Cria o diretório se não existir
    if not os.path.exists(TARGET_DIR):
        try:
            os.makedirs(TARGET_DIR)
            print(f"[+] Diretório criado: {TARGET_DIR}")
        except PermissionError:
            print(f"[!] ERRO: Sem permissão. Execute o VS Code como Administrador.")
            return

    print(f"[*] Gerando {NUM_FILES} arquivos de teste...")

    # 2. Loop para criar arquivos
    for i in range(NUM_FILES):
        # Gera um nome aleatório (ex: financial_data_392.txt)
        filename = f"doc_confidencial_{i}_{random.randint(1000, 9999)}.txt"
        filepath = os.path.join(TARGET_DIR, filename)

        # Gera conteúdo aleatório (Lorem Ipsum falso)
        content = ''.join(random.choices(string.ascii_letters + string.digits, k=500))
        
        # Salva o arquivo
        with open(filepath, "w") as f:
            f.write(f"DADOS IMPORTANTES - ID {i}\n")
            f.write("-" * 30 + "\n")
            f.write(content)
    
    print(f"[OK] Sucesso! {NUM_FILES} arquivos criados em {TARGET_DIR}")

if __name__ == "__main__":
    create_dummy_files()