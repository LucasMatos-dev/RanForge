import os
import sys
import winreg

def enable_persistence():
    """
    Adiciona uma entrada no Registo do Windows para que este script
    seja executado automaticamente no arranque do sistema.
    """
    python_exe = sys.executable
    script_path = os.path.abspath("main.py")
    
    command = f'"{python_exe}" "{script_path}"'
    
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "RanForge_SystemCheck"

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, command)
        
        winreg.CloseKey(key)
        
        print(f"[PERSISTÊNCIA] Chave de Registo criada com sucesso.")
        print(f" -> Nome: {app_name}")
        return True
        
    except Exception as e:
        print(f"[ERRO] Falha ao criar persistência: {e}")
        return False

def remove_persistence():
    """
    Remove a entrada do registo.
    """
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "RanForge_SystemCheck"

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, app_name)
        winreg.CloseKey(key)
        print("[PERSISTÊNCIA] Chave de Registo removida.")
    except FileNotFoundError:
        print("[INFO] Nenhuma persistência encontrada para remover.")
    except Exception as e:
        print(f"[ERRO] Falha ao remover persistência: {e}")

if __name__ == "__main__":
    enable_persistence()