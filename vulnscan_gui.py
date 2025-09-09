"""
VulnScanPro Hackathon Edition
-----------------------------
Escáner web seguro y profesional para demostraciones.

Descripción:
------------
VulnScanPro simula pruebas de seguridad en sitios web, incluyendo:
- XSS
- SQLi
- Formularios
- Cabeceras HTTP
- robots.txt
- Enumeración de tecnologías web

Genera un resumen amigable usando OpenAI GPT-4o-mini. En caso de fallo de la API, se utiliza un resumen simulado.

Objetivos:
----------
1. Proporcionar entorno seguro para prácticas de pentesting educativo.
2. Mostrar resultados de forma clara, profesional y visual.
3. Generar reportes automáticos en formato .txt.
4. Ser útil para demostraciones y hackathons.

Arquitectura:
-------------
1. GUI: Tkinter para entrada de URL, selección de escaneos y visualización de logs/resultados.
2. Lógica de Escaneo: Funciones que simulan pruebas según opciones seleccionadas.
3. IA: Función que genera resumen amigable con GPT-4o-mini.

Flujo de Trabajo:
-----------------
1. Ingreso de URL y selección de opciones.
2. Presionar "Iniciar Escaneo".
3. Simulación de escaneo según opciones.
4. Generación de resumen IA (o simulado si falla API).
5. Guardado de reporte en .txt seguro para Windows.
6. Visualización de logs y resumen en la GUI.
7. Sonidos opcionales de alerta de inicio y finalización.

Estructura de Archivos:
-----------------------
VulnScanPro/
├── vulnscan_gui.py         # Código principal con documentación integrada
├── reporte_<URL>_<fecha>.txt  # Reportes generados automáticamente
└── requirements.txt        # Librerías necesarias (openai)

Uso:
----
1. Configurar variable de entorno OPENAI_API_KEY.
2. Ejecutar el script: python vulnscan_gui.py
3. Ingresar URL y seleccionar opciones de escaneo.
4. Presionar "Iniciar Escaneo".
5. Ver resultados en tiempo real y generar reporte.

Seguridad:
----------
- Este escáner **solo simula pruebas**. No realizar ataques reales sin autorización.
- Ideal para hackathons, demostraciones y entornos educativos.

Mejoras Futuras:
----------------
- Barra de progreso y animaciones.
- Logs exportables en HTML con colores.
- Escaneo real de cabeceras y robots.txt.
- Autenticación segura en la GUI.
- Soporte multiplataforma (Linux/Mac).
"""

import os
import re
import tkinter as tk
from tkinter import messagebox, scrolledtext
from urllib.parse import urlparse
from openai import OpenAI
import datetime
import threading
import winsound

# ==============================
# Configuración del cliente OpenAI
# ==============================
client = OpenAI(api_key=os.getenv("AQUI TU API"))

# ==============================
# Funciones utilitarias
# ==============================

def is_valid_url(url):
    """Verifica si la URL tiene un esquema válido (http/https) y un netloc."""
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc

def play_sound(freq=700, duration=200):
    """Reproduce un beep en Windows (opcional, para alertas visuales/sonoras)."""
    try:
        winsound.Beep(freq, duration)
    except:
        pass

# ==============================
# Funciones de escaneo
# ==============================

def simulate_scan(url, options):
    """
    Simula el escaneo de un sitio web según las opciones seleccionadas.
    Retorna una lista de logs y un resumen textual.
    """
    log = []
    resumen = ""

    if options['info']:
        log.append("[INFO] Recopilando información del servidor...")
        resumen += "Información del servidor obtenida.\n"
        log.append("[SUCCESS] Información recopilada.")

    if options['xss']:
        log.append("[INFO] Analizando posibles XSS...")
        resumen += "Prueba de vulnerabilidades XSS simulada.\n"
        log.append("[SUCCESS] Escaneo XSS completado.")

    if options['sqli']:
        log.append("[INFO] Analizando posibles SQLi...")
        resumen += "Prueba de vulnerabilidades SQLi simulada.\n"
        log.append("[SUCCESS] Escaneo SQLi completado.")

    if options['forms']:
        log.append("[INFO] Detectando formularios y probando XSS en ellos...")
        resumen += "Se detectaron formularios y se probaron para XSS de manera segura.\n"
        log.append("[SUCCESS] Prueba de formularios completada.")

    if options['headers']:
        log.append("[INFO] Analizando cabeceras HTTP...")
        resumen += "Revisión de cabeceras HTTP realizada.\n"
        log.append("[SUCCESS] Cabeceras analizadas.")

    if options['robots']:
        log.append("[INFO] Revisando robots.txt...")
        resumen += "robots.txt analizado de forma segura.\n"
        log.append("[SUCCESS] robots.txt revisado.")

    if options['tech']:
        log.append("[INFO] Enumerando tecnologías utilizadas por el sitio...")
        resumen += "Se realizó una enumeración simulada de tecnologías.\n"
        log.append("[SUCCESS] Enumeración de tecnologías completada.")

    return log, resumen

def ai_generate_summary(resumen):
    """
    Genera un resumen profesional usando IA.
    Si falla la API o excede cuota, devuelve un resumen simulado.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content":
                    f"Eres un asistente amigable que resume resultados de seguridad web para un usuario no técnico:\n\n{resumen}"}],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception:
        # Resumen simulado en caso de error de API
        return f"[Resumen simulado debido a error de API]\n{resumen}"

# ==============================
# Función principal del escaneo
# ==============================

def run_scan():
    """Inicia el escaneo seguro de un sitio web y actualiza la GUI."""
    url = entry_url.get().strip()
    if not is_valid_url(url):
        messagebox.showerror("URL inválida", "Ingrese una URL válida (http:// o https://).")
        return

    scan_button.config(state=tk.DISABLED)
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.config(state=tk.DISABLED)
    steps_area.config(state=tk.NORMAL)
    steps_area.delete("1.0", tk.END)
    steps_area.config(state=tk.DISABLED)

    options = {
        'info': var_info.get(),
        'xss': var_xss.get(),
        'sqli': var_sqli.get(),
        'forms': var_forms.get(),
        'headers': var_headers.get(),
        'robots': var_robots.get(),
        'tech': var_tech.get()
    }

    def task():
        # Sonido inicial
        play_sound(600, 200)

        # Simula escaneo
        log, resumen = simulate_scan(url, options)

        # Muestra logs en GUI
        for line in log:
            steps_area.config(state=tk.NORMAL)
            if "[INFO]" in line:
                steps_area.insert(tk.END, line + "\n", "info")
            elif "[SUCCESS]" in line:
                steps_area.insert(tk.END, line + "\n", "success")
            elif "[WARNING]" in line:
                steps_area.insert(tk.END, line + "\n", "warning")
            elif "[ERROR]" in line:
                steps_area.insert(tk.END, line + "\n", "error")
            else:
                steps_area.insert(tk.END, line + "\n")
            steps_area.see(tk.END)
            steps_area.config(state=tk.DISABLED)

        # Genera resumen IA
        ai_summary = ai_generate_summary(resumen)

        # Muestra resultado final en GUI
        output_area.config(state=tk.NORMAL)
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, f"== VulnScanPro ({url}) ==\n\n")
        output_area.insert(tk.END, ai_summary)
        output_area.config(state=tk.DISABLED)

        # Guardar reporte seguro para Windows
        safe_url = re.sub(r'[\\/*?:"<>|]', "_", url)
        filename = f"reporte_{safe_url}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n\n")
            f.write(ai_summary)

        status_label.config(text=f"Escaneo completado. Reporte guardado: {filename}", fg="green")
        play_sound(900, 300)
        scan_button.config(state=tk.NORMAL)

    threading.Thread(target=task, daemon=True).start()

# ==============================
# Limpiar pantalla
# ==============================
def clear_output():
    """Limpia los textos de logs y resultados en la GUI."""
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.config(state=tk.DISABLED)
    steps_area.config(state=tk.NORMAL)
    steps_area.delete("1.0", tk.END)
    steps_area.config(state=tk.DISABLED)
    status_label.config(text="Pantalla limpia", fg="blue")

# ==============================
# Configuración GUI
# ==============================

root = tk.Tk()
root.title("VulnScanPro - Hackathon Edition")
root.geometry("950x750")
root.configure(bg="#f9fafb")

# Frame superior: URL y botones
frame_top = tk.Frame(root, bg="#f9fafb", pady=10)
frame_top.pack(fill="x")
tk.Label(frame_top, text="URL objetivo:", bg="#f9fafb").pack(side="left", padx=10)
entry_url = tk.Entry(frame_top, width=55)
entry_url.pack(side="left", padx=5)
scan_button = tk.Button(frame_top, text="Iniciar Escaneo", bg="#2196F3", fg="white", command=run_scan)
scan_button.pack(side="left", padx=5)
clear_button = tk.Button(frame_top, text="Limpiar", bg="#d32f2f", fg="white", command=clear_output)
clear_button.pack(side="left", padx=5)

# Frame opciones de escaneo
frame_opts = tk.Frame(root, bg="#f9fafb")
frame_opts.pack(fill="x", padx=10, pady=5)
var_info = tk.BooleanVar(value=True)
var_xss = tk.BooleanVar(value=True)
var_sqli = tk.BooleanVar(value=True)
var_forms = tk.BooleanVar(value=True)
var_headers = tk.BooleanVar(value=True)
var_robots = tk.BooleanVar(value=True)
var_tech = tk.BooleanVar(value=True)

tk.Checkbutton(frame_opts, text="Info", variable=var_info, bg="#f9fafb").pack(side="left", padx=8)
tk.Checkbutton(frame_opts, text="XSS", variable=var_xss, bg="#f9fafb").pack(side="left", padx=8)
tk.Checkbutton(frame_opts, text="SQLi", variable=var_sqli, bg="#f9fafb").pack(side="left", padx=8)
tk.Checkbutton(frame_opts, text="Formularios", variable=var_forms, bg="#f9fafb").pack(side="left", padx=8)
tk.Checkbutton(frame_opts, text="Cabeceras HTTP", variable=var_headers, bg="#f9fafb").pack(side="left", padx=8)
tk.Checkbutton(frame_opts, text="robots.txt", variable=var_robots, bg="#f9fafb").pack(side="left", padx=8)
tk.Checkbutton(frame_opts, text="Tecnologías", variable=var_tech, bg="#f9fafb").pack(side="left", padx=8)

# Frame central: logs y resultados
frame_center = tk.Frame(root, bg="#f9fafb")
frame_center.pack(fill="both", expand=True, padx=10, pady=10)

frame_steps = tk.LabelFrame(frame_center, text="Proceso del Escaneo", bg="white", fg="#222", padx=8, pady=8)
frame_steps.pack(side="left", fill="both", expand=True, padx=(0,5))
steps_area = scrolledtext.ScrolledText(frame_steps, bg="white", fg="#111", wrap="word", state=tk.DISABLED)
steps_area.pack(fill="both", expand=True)
steps_area.tag_config("info", foreground="#0a64a4")
steps_area.tag_config("success", foreground="#2e7d32")
steps_area.tag_config("warning", foreground="#ed6c02")
steps_area.tag_config("error", foreground="#d32f2f")

frame_output = tk.LabelFrame(frame_center, text="Resumen IA", bg="white", fg="#222", padx=8, pady=8)
frame_output.pack(side="left", fill="both", expand=True, padx=(5,0))
output_area = scrolledtext.ScrolledText(frame_output, bg="white", fg="#111", wrap="word", state=tk.DISABLED)
output_area.pack(fill="both", expand=True)

# Label de estado
status_label = tk.Label(root, text="Listo para escanear", bg="#f9fafb", fg="blue")
status_label.pack(pady=5)

# Inicia GUI
root.mainloop()
