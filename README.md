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

Instala las dependencias:

pip install -r requirements.txt

🚀 Uso

Ejecuta el script principal:

python vulnscan_gui.py


Ingresa la URL que deseas escanear.

Selecciona las opciones de escaneo: Info, XSS, SQLi, Formularios, Cabeceras HTTP, robots.txt, Tecnologías.

Presiona Iniciar Escaneo.

Visualiza los resultados y el resumen de IA en tiempo real.

Se genera automáticamente un reporte .txt seguro para Windows en la misma carpeta.

📂 Estructura del Proyecto
VulnScanPro/
├── vulnscan_gui.py               # Código principal
├── requirements.txt              # Dependencias del proyecto
├── reporte_<URL>_<fecha>.txt     # Reportes generados automáticamente
└── README.md                     # Documentación y guía de uso

⚙️ Funcionalidades

Simula pruebas de seguridad web:

XSS

SQLi

Formularios

Cabeceras HTTP

robots.txt

Enumeración de tecnologías web

Genera resumen amigable de resultados con IA.
Guarda reportes en .txt con nombre seguro para Windows.
GUI profesional con logs de proceso y resultados.
Sonidos opcionales al iniciar y finalizar el escaneo.

💡 Mejoras Futuras

Barra de progreso y animaciones en la GUI.

Logs exportables en HTML con colores.

Escaneo real de cabeceras y robots.txt.

Autenticación segura en la GUI.

Soporte multiplataforma (Linux/Mac).

📌 Flujo de Trabajo

Ingreso de URL y selección de opciones.

Presionar Iniciar Escaneo.

Simulación de escaneo según opciones seleccionadas.

Generación de resumen IA (o simulado si falla la API).

Guardado de reporte en .txt seguro para Windows.

Visualización de logs y resumen en la GUI.

Sonidos opcionales de alerta de inicio y finalización.

🛡️ Seguridad

Este escáner solo simula pruebas.

No realizar ataques reales sin autorización.

Herramienta destinada a demostraciones, hackathons y entornos educativos.
