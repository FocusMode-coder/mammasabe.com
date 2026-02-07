# Mamma Sabe - Landing Page

Landing page mobile-first para exposición de marca de alimentos plant-based.

## 📁 Estructura del Proyecto

```
MammaSabe/
├── index.html              # Página principal
├── styles.css              # Estilos CSS
├── i18n.js                 # Sistema de traducciones (5 idiomas)
├── app.py                  # Servidor Flask con keep-alive
├── requirements.txt        # Dependencias Python
├── render.yaml             # Configuración para Render
├── Procfile                # Comando de inicio para Render
├── .gitignore              # Archivos a ignorar en Git
├── assets/                 # Imágenes extraídas del PDF
│   ├── p01_img001.jpeg
│   ├── p13_img001.jpeg    # Medallones 
│   ├── p13_img002.jpeg    # Falafel
│   └── ...
├── extract_images.py       # Script de extracción de imágenes
└── BrochureFINAL_MammaSabe.pdf
```

## 🎨 Características

- ✅ Mobile-first, responsive
- ✅ **Multi-idioma**: Inglés (default), Español, Francés, Alemán, Portugués
- ✅ Selector de idiomas sticky en la parte superior
- ✅ Imágenes reales de productos del PDF
- ✅ Botones expandibles con info detallada
- ✅ Formulario de captura de emails
- ✅ Paleta de colores cálida y mediterránea
- ✅ Sin frameworks, sin build tools
- ✅ **Servidor con keep-alive** para Render (evita dormir el sitio)
- ✅ Listo para deploy en Render

## 🌍 Sistema de Idiomas

La landing page soporta 5 idiomas:
- **🇬🇧 Inglés** (EN) - Idioma por defecto
- **🇪🇸 Español** (ES)
- **🇫🇷 Francés** (FR)
- **🇩🇪 Alemán** (DE)
- **🇵🇹 Portugués** (PT)

### Cómo funciona:

1. El selector aparece arriba de todo (sticky)
2. Al cambiar idioma, TODO el contenido se traduce instantáneamente
3. La preferencia se guarda en localStorage
4. Sin recargar la página

### Agregar más idiomas:

Editá `i18n.js` y agregá un nuevo objeto con todas las traducciones:

```javascript
translations.it = {
    hero: {
        title: "Cibo Vero,<br>Impatto Vero",
        subtitle: "Innovazione plant-based dall'Argentina al mondo"
    },
    // ... resto de traducciones
}
```

Luego agregá el botón en `index.html`:
```html
<button class="lang-btn" data-lang="it">🇮🇹 IT</button>
```

## 📧 Configurar Captura de Emails

### Opción 1: Formspree (Recomendado - Gratis)

1. Ve a [formspree.io](https://formspree.io) y crea una cuenta gratis
2. Crea un nuevo formulario
3. Copia tu Form ID (algo como `mabcdxyz`)
4. En `index.html` línea ~145, reemplaza:
   ```html
   <form class="email-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
   Por:
   ```html
   <form class="email-form" action="https://formspree.io/f/mabcdxyz" method="POST">
   ```

**Ventajas:**
- Gratis hasta 50 envíos/mes
- Los emails llegan directo a tu inbox
- No necesitas backend
- Confirmación automática

### Opción 2: Google Forms + Google Sheets

1. Crea un Google Form
2. Usa un servicio como [form-to-google-sheets](https://github.com/jamiewilson/form-to-google-sheets)
3. Los datos se guardan en una hoja de cálculo

### Opción 3: Netlify Forms

Si deployás en Netlify, solo agregá `netlify` al form:
```html
<form name="contact" method="POST" data-netlify="true">
```

## 🚀 Deploy en Render

### Deployment con Keep-Alive (Recomendado)

Este proyecto incluye un servidor Python con sistema keep-alive para evitar que el sitio se duerma en el plan gratuito de Render.

1. **Conectá tu repositorio GitHub a Render**
2. **Tipo:** Web Service (no Static Site)
3. **Configuración:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn server:app`
4. **Variables de entorno:**
   - Después del primer deploy, añadí la variable: `RENDER_URL` = `https://tu-sitio.onrender.com`
5. **Deploy!**

El servidor hace un auto-ping cada 14 minutos para mantener el sitio activo 24/7.

### Alternativamente: Static Site (se duerme después de 15 min)

1. Tipo: **Static Site**
2. Build command: (vacío)
3. Publish directory: `.`
4. Deploy!

## 🖼️ Cambiar Imágenes de Productos

Las imágenes actuales son:
- **Medallones**: `assets/p13_img001.jpeg`
- **Falafel**: `assets/p13_img002.jpeg`
- **Hero background**: `assets/p01_img001.jpeg`

Para cambiar, editá en `index.html` las rutas src de las imágenes, o en `styles.css` línea 113 para el hero.

## 🎨 Personalizar Colores

En `styles.css` líneas 6-12, cambiá las variables CSS:

```css
:root {
    --primary-red: #D94B3A;
    --cream-bg: #FAF7F2;
    --dark-green: #1F4D45;
    --charcoal: #2A2A2A;
}
```

## 📱 Preview Local

Simplemente abrí `index.html` en tu navegador, o usá Live Server en VS Code.

## ✉️ Contacto

hello@mammasabe.com
