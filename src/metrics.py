import hashlib
import json
import time
import os

# Arquivo onde salvaremos o "estado original" para comparação
HASH_DB_FILE = "file_integrity_db.json"

def calculate_sha256(file_path):
    """Lê o arquivo em blocos e calcula o hash SHA256."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Ler em blocos de 4K para não travar a memória
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def save_baseline(files_list):
    """Gera e salva os hashes dos arquivos originais (ANTES do ataque)."""
    print("[METRICS] Gerando Baseline de Integridade (SHA256)...")
    baseline = {}
    
    start_time = time.time()
    
    for f in files_list:
        if "LEIA_ME_AGORA.txt" in f:
            continue
            
        h = calculate_sha256(f)
        if h:
            baseline[f] = h
            
    with open(HASH_DB_FILE, "w") as db:
        json.dump(baseline, db, indent=4)
        
    print(f"[METRICS] Baseline salvo em {HASH_DB_FILE}")
    return start_time

def verify_integrity(files_list):
    """Compara os arquivos atuais com o baseline salvo (PÓS recuperação)."""
    print("[METRICS] Verificando Integridade Pós-Recuperação...")
    
    if not os.path.exists(HASH_DB_FILE):
        print("[!] ERRO: Banco de dados de hashes não encontrado.")
        return

    with open(HASH_DB_FILE, "r") as db:
        baseline = json.load(db)

    match_count = 0
    error_count = 0
    skipped_count = 0

    for f_path in files_list:
        if "LEIA_ME_AGORA.txt" in f_path:
            continue
            
        if f_path not in baseline:
            skipped_count += 1
            continue
            
        current_hash = calculate_sha256(f_path)
        original_hash = baseline[f_path]

        if current_hash == original_hash:
            match_count += 1
        else:
            print(f"[!] FALHA DE INTEGRIDADE: {f_path}")
            # print(f"    Original: {original_hash}") # Descomente para debug
            # print(f"    Atual:    {current_hash}")
            error_count += 1

    total_checked = match_count + error_count
    success_rate = (match_count / total_checked) * 100 if total_checked > 0 else 0
    
    print("-" * 40)
    print(f"RELATÓRIO FINAL DE INTEGRIDADE")
    print(f"Arquivos validados: {match_count}")
    print(f"Arquivos corrompidos: {error_count}")
    print(f"Taxa de Sucesso: {success_rate:.2f}%")
    print("-" * 40)

def verify_integrity_gui(files_list):
    """Versão silenciosa que retorna um dicionário para a GUI."""
    if not os.path.exists(HASH_DB_FILE):
        return {"match": 0, "error": 0, "success_rate": 0}

    with open(HASH_DB_FILE, "r") as db:
        baseline = json.load(db)

    match_count = 0
    error_count = 0

    for f_path in files_list:
        if "LEIA_ME_AGORA.txt" in f_path: continue
        if f_path not in baseline: continue
            
        current_hash = calculate_sha256(f_path)
        if current_hash == baseline[f_path]:
            match_count += 1
        else:
            error_count += 1

    total = match_count + error_count
    rate = (match_count / total) * 100 if total > 0 else 0
    
    return {"match": match_count, "error": error_count, "success_rate": rate}