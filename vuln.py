# vulnscan_core.py
import requests
from bs4 import BeautifulSoup
import urllib.parse

XSS_PAYLOADS = ["<script>alert(1)</script>", "'><img src=x onerror=alert(1)>"]
SQLI_ERRORS = ["sql syntax", "mysql_fetch", "ORA-01756", "unterminated", "quoted string"]
SQLI_PAYLOADS = ["'", "' OR '1'='1", "';--", "\" OR \"1\"=\"1"]
HEADERS = {"User-Agent": "Mozilla/5.0 (VulnScanPro)"}

def get_info(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        info = f"[INFO] Código de estado: {r.status_code}\n"
        info += f"[INFO] Servidor: {r.headers.get('Server', 'Desconocido')}\n"
        info += f"[INFO] Cookies: {r.cookies}\n"
        return info
    except Exception as e:
        return f"[ERROR] No se pudo conectar: {e}\n"

def scan_xss(url):
    results = "[XSS] Escaneo iniciado...\n"
    for payload in XSS_PAYLOADS:
        test_url = f"{url}?q={urllib.parse.quote(payload)}"
        try:
            r = requests.get(test_url, headers=HEADERS)
            if payload.lower() in r.text.lower():
                results += f"[VULNERABLE] Reflected XSS detectado con payload: {payload}\n"
        except:
            continue
    return results

def scan_sqli(url):
    results = "[SQLi] Escaneo iniciado...\n"
    for payload in SQLI_PAYLOADS:
        test_url = f"{url}?id={urllib.parse.quote(payload)}"
        try:
            r = requests.get(test_url, headers=HEADERS)
            if any(err in r.text.lower() for err in SQLI_ERRORS):
                results += f"[VULNERABLE] SQLi detectado con payload: {payload}\n"
        except:
            continue
    return results

def find_forms(url):
    try:
        r = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all("form")
    except:
        return []

def test_form_xss(forms, url):
    results = "[FORM-XSS] Escaneando formularios...\n"
    for form in forms:
        action = form.get("action")
        method = form.get("method", "get").lower()
        inputs = form.find_all(["input", "textarea"])
        data = {i.get("name"): XSS_PAYLOADS[0] for i in inputs if i.get("name")}
        target = urllib.parse.urljoin(url, action)
        try:
            if method == "post":
                r = requests.post(target, data=data, headers=HEADERS)
            else:
                r = requests.get(target, params=data, headers=HEADERS)

            if XSS_PAYLOADS[0] in r.text:
                results += f"[VULNERABLE] XSS en formulario: {target}\n"
        except:
            continue
    return results if "[VULNERABLE]" in results else "[FORM-XSS] No se detectaron vulnerabilidades.\n"
