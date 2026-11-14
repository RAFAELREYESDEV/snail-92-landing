# SNAIL 92™ | Landing Page E-commerce Contra Entrega (Venezuela)

Landing page oficial de alta conversión para la **Crema Facial Mucina de Caracol 92%** (*Filtrado Bio-Activo Helix al 92%*) en Venezuela bajo modelo Cash on Delivery (Pago al Recibir).

## ✨ Características Principales
- **Estética Minimalista Apple-Style:** Alto contraste, fondo neutro ultra-limpio (`#FAFAFA`), tipografía *Inter*, acentos en amarillo vibrante (`#FACC15`) y botones con efecto glassmorphism.
- **Directorio Oficial Tealca (134 Sedes):** Selector dinámico categorizado por Estado para retiro en taquilla oficial o entrega directa a domicilio sin fricción.
- **Checkout Modal Pop-Up:** Flujo de captura en 2 pasos (Elección de tratamiento + Formulario validado) optimizado para móviles.
- **Tasa Oficial BCV:** Conversión automática en tiempo real de USD a Bolívares.
- **Integración WhatsApp Directa:** Despacho automatizado a operador de atención (Manuel) con orden estructurada.

## 🚀 Despliegue en Cloudflare Pages
1. Sube este repositorio a tu cuenta de GitHub (ej. `snail-92-landing`).
2. Ve al panel de [Cloudflare Dashboard](https://dash.cloudflare.com/) > **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3. Selecciona el repositorio `snail-92-landing`.
4. Configuración de Build:
   - **Framework preset:** `None` (Static HTML)
   - **Build command:** *(dejar vacío)*
   - **Build output directory:** `/` *(raíz)*
5. Haz clic en **Save and Deploy**. En menos de 30 segundos estará activa en tu subdominio `.pages.dev` con SSL global y CDN instantáneo.

## 📁 Estructura del Proyecto
```text
├── index.html                   # Landing page completa de producción
├── images/                      # Activos visuales y fotografías del producto
│   ├── modelo_hero.jpg
│   ├── hero_jar.jpg
│   ├── manos_abriendo_pote.jpg
│   ├── antes_despues_textura.jpg
│   └── caja_dimensiones.jpg
├── tealca_js_data.json          # Directorio maestro de sucursales Tealca
└── README.md
```
