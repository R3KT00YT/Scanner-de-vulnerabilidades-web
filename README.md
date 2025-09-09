# VulnScanPro - Hackathon Edition

**Escáner web seguro y profesional para demostraciones.**

---

## ⚠️ Aviso de Responsabilidad

- Este escáner **solo simula pruebas** de seguridad web.  
- **No nos hacemos responsables** del uso indebido de esta herramienta.  
- Requiere **API personalizada de ChatGPT (OpenAI)** para generar resúmenes.  
  - La API es de pago y existe una versión gratuita con uso limitado.  
- Usar únicamente en entornos educativos, hackathons o sitios propios con autorización explícita.

---

## 🛠️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/VulnScanPro.git
cd VulnScanPro
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

Ejecuta el script principal:

```bash
python vulnscan_gui.py
```

1. Ingresa la URL que deseas escanear.
2. Selecciona las opciones de escaneo: Info, XSS, SQLi, Formularios, Cabeceras HTTP, robots.txt, Tecnologías.
3. Presiona Iniciar Escaneo.
4. Visualiza los resultados y el resumen de IA en tiempo real.
5. Se genera automáticamente un reporte `.txt` seguro para Windows en la misma carpeta.

---

## 📂 Estructura del Proyecto

```
VulnScanPro/
├── vulnscan_gui.py               # Código principal
├── requirements.txt              # Dependencias del proyecto
├── reporte_<URL>_<fecha>.txt     # Reportes generados automáticamente
└── README.md                     # Documentación y guía de uso
```

---

## ⚙️ Funcionalidades

Simula pruebas de seguridad web:

- XSS
- SQLi
- Formularios
- Cabeceras HTTP
- robots.txt
- Enumeración de tecnologías web

Genera resumen amigable de resultados con IA.

Guarda reportes en `.txt` con nombre seguro para Windows.

GUI profesional con logs de proceso y resultados.

Sonidos opcionales al iniciar y finalizar el escaneo.

---

## 💡 Mejoras Futuras

- Barra de progreso y animaciones en la GUI.
- Logs exportables en HTML con colores.
- Escaneo real de cabeceras y robots.txt.
- Autenticación segura en la GUI.
- Soporte multiplataforma (Linux/Mac).

---

## 📌 Flujo de Trabajo

1. Ingreso de URL y selección de opciones.
2. Presionar Iniciar Escaneo.
3. Simulación de escaneo según opciones seleccionadas.
4. Generación de resumen IA (o simulado si falla la API).
5. Guardado de reporte en `.txt` seguro para Windows.
6. Visualización de logs y resumen en la GUI.
7. Sonidos opcionales de alerta de inicio y finalización.

---

## 🛡️ Seguridad

Este escáner solo simula pruebas.

No realizar ataques reales sin autorización.

Herramienta destinada a demostraciones,
