import os
import sys

# --- TRAVA DE SEGURANÇA ---
# Isso impede que o ransomware varra o C:\ inteiro ou pastas de sistema
SAFE_DIR = r"C:\ransom_test"

def discover_files():
    """
    Retorna uma lista de todos os arquivos dentro do diretório seguro.
    Se o diretório não for o esperado, aborta o programa.
    """
    
    if not os.path.exists(SAFE_DIR):
        print(f"[!] ERRO CRÍTICO: O diretório alvo {SAFE_DIR} não existe.")
        print("[!] Abortando para segurança do sistema.")
        sys.exit(1)

    target_files = []
    
    print(f"[*] Iniciando varredura segura em: {SAFE_DIR}")

    for root, dirs, files in os.walk(SAFE_DIR):
        for file in files:
            abs_path = os.path.join(root, file)
            
            if file == "ransom_note.txt" or file.endswith(".py"):
                continue
            
            target_files.append(abs_path)

    print(f"[*] Varredura concluída. {len(target_files)} alvos encontrados.")
    return target_files

# Bloco de teste (só roda se você executar este arquivo diretamente)
if __name__ == "__main__":
    arquivos = discover_files()
    # Lista os primeiros 5 arquivos encontrados para confirmar
    for f in arquivos[:5]:
        print(f" -> Encontrado: {f}")