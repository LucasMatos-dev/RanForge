import os
import target_discovery
import crypto_engine
import persistence
import metrics

def run_decryption_logic():
    """
    Executa a descriptografia e retorna um relatório em texto (string)
    para ser exibido na interface gráfica.
    """
    log = [] 
    
    if not os.path.exists(crypto_engine.KEY_FILE):
        return "ERRO CRÍTICO: Chave mestra não encontrada. Recuperação impossível."

    with open(crypto_engine.KEY_FILE, "rb") as kf:
        key = kf.read()
    
    targets = target_discovery.discover_files()
    decrypted_count = 0

    for file_path in targets:
        if "LEIA_ME_AGORA.txt" in file_path: continue
        if crypto_engine.decrypt_file(file_path, key):
            decrypted_count += 1

    ransom_note_path = os.path.join(target_discovery.SAFE_DIR, "LEIA_ME_AGORA.txt")
    if os.path.exists(ransom_note_path):
        try:
            os.remove(ransom_note_path)
        except: pass

    persistence.remove_persistence()

    stats = metrics.verify_integrity_gui(targets) 
    
    log.append(f"Arquivos Descriptografados: {decrypted_count}")
    log.append(f"Validacao de Integridade: {stats['success_rate']:.2f}%")
    log.append(f"Arquivos Integros: {stats['match']}")
    log.append(f"Arquivos Corrompidos: {stats['error']}")
    
    return "\n".join(log)