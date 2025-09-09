# VulnScanPro - Hackathon Edition

**Escáner web seguro y profesional para demostraciones y hackathons.**

---

## ⚠️ Aviso de Responsabilidad

- **VulnScanPro solo simula pruebas de seguridad web** (XSS, SQLi, formularios, cabeceras HTTP, robots.txt, tecnologías web).  
- **No nos hacemos responsables** del uso indebido de esta herramienta.  
- Usar únicamente en entornos educativos, hackathons o sitios propios con autorización explícita.  

---

## 🔑 Requisitos de API

- Requiere **API Key de OpenAI** para generar resúmenes amigables con IA (modelo `gpt-4o-mini`).  
- La API es **de pago**; existe una versión gratuita con **uso limitado**.  
- Configura tu API Key como variable de entorno:  

```bash
export OPENAI_API_KEY="tu_api_key_aqui"   # Linux / Mac
setx OPENAI_API_KEY "tu_api_key_aqui"     # Windows
