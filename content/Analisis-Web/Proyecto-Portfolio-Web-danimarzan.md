---
title: Proyecto Portfolio Web — danimarzan.com
---

# Proyecto Portfolio Web — danimarzan.com

> Estado: Junio 2026
> Última actualización: 2026-06-06

## Repositorio GitHub

- **Repo:** `SleepingSmel/web_danimarzan` (privado)
- **Token:** `GITHUB_MYWEB_TOKEN` en `/opt/data/.env`
- **Deploy:** Dokploy auto-redespliega al hacer push a master
- **URL:** https://danimarzan.com

## Archivos en el repo

```
web_danimarzan/
├── .gitignore
├── Dockerfile
├── README.md
├── abora-logo.jpg
├── abora-ui.jpg
├── index.html          ← 536 líneas, ~55KB
└── nginx.conf
```

## Estado actual de la web LIVE (index.html)

### Estructura
- Single-page scroll con 7 secciones (scroll-snap)
- HTML + CSS + JS todo inline (sin frameworks)
- GSAP NO usado (solo CSS animations)
- Canvas con partículas + blobs de fondo
- i18n ES/EN integrado

### Secciones
1. **Hero** — "Daniel Marzán" + tagline "Empecé soñando con parar goles" + placeholder "Tu PNG (croma) aquí"
2. **Redes** — "No llegué a profesional. Llegué a 60.000." + stats (60k YT, 48k TK) + placeholders vídeo/reels
3. **Vídeo** — "Sin vídeo, no existes." + chips (Corporativo, Eventos, Bodas) + placeholder vídeo
4. **Web** — "Diseño webs que enamoran" + browser mockup animado
5. **Docencia** — "Enseño lo que domino" + timeline educación
6. **Apps IA** — "Debate con Marx. Lo programé yo." + Abora phone mockup
7. **Dron 3D** — "Cartografío el mundo, con un dron" + placeholder mapa
8. **Contacto** — "Hablemos." + email + LinkedIn + socials

### Placeholders pendientes (P1)
- **Foto/PNG en Hero** — línea 244: `Tu PNG (croma) aquí`
- **Vídeo principal** — `data-yt=""` vacío (líneas 262, 281)
- **Reels** — `data-yt=""` vacío (líneas 264-266)
- **Mapa 3D** — placeholder "Próximamente"

### Tecnologías
- CSS custom properties para temas por sección
- Canvas 2D para partículas de fondo
- CSS scroll-snap
- Intersection Observer para animaciones
- Sin dependencias externas (excepto Google Fonts)

## site_v12.html (en PC de Dani, NO en servidor)

Según los pendientes de Dani, existe un `site_v12.html` que:
- Tiene transición + demo de Abora
- Pendiente de revisar en navegador y aprobar
- Si se aprueba → copiar a `index.html` y hacer git push
- Dokploy auto-redespliega

### Acción requerida (de Dani)
- [ ] Revisar site_v12.html en navegador
- [ ] Aprobar transición + demo de Abora
- [ ] Dar OK para copiar v12 → index.html + git push

## Pendientes de Dani (de su lista)

### 🔴 P0 — Infraestructura email
- [ ] Decidir dominio de envío (danimarzan.com vs dedicado)
- [ ] Crear buzón en Hostinger
- [ ] Configurar SPF + DKIM + DMARC
- [ ] Empezar warm-up (5-10 correos/día, ~2 semanas)

### 🟠 P1 — Activos de venta
- [ ] Revisar site_v12.html → aprobar → publicar
- [ ] Añadir foto real (hero + "Sobre mí")
- [ ] Grabar 1 vídeo muestra "Cómo funciona el TPS" (60s)
- [ ] Crear link de reserva (Calendly)
- [ ] Reunir 2-3 Reels de muestra

### 🟡 P1 — Outreach
- [ ] Validar guiones audit 3 abogados
- [ ] Revisar calibración de Thor
- [ ] Dar OK a Hunter
- [ ] Grabar 3 audits en vídeo (Loom, 60-90s)
- [ ] Generar emails finales + enviar

### 🟢 P2 — Web siguiente nivel
- [ ] Trabajar textos copywriting/storytelling
- [ ] Decidir intensidad efecto transición
- [ ] (Opcional) Screen-recording de Abora
- [ ] Stop-motion PNG con bocadillos
- [ ] Chat IA en web (v2, después de que núcleo convierta)

## Análisis técnico del index.html actual

### ✅ Lo que funciona bien
- Diseño visual premium (dark theme, gradientes, animaciones fluidas)
- Responsive (media queries en 820px y 560px)
- i18n ES/EN completo
- Navegación por dots + flechas + teclado + touch
- Browser mockup con gags interactivos
- Phone mockup con Abora
- Rendimiento: todo inline, sin requests externas (excepto fonts)

### ⚠️ Issues detectados
1. **Foto placeholder** — Hero muestra "Tu PNG (croma) aquí" (línea 244)
2. **Vídeos vacíos** — `data-yt=""` en secciones 1, 2, 3 — no cargan thumbnails
3. **Reels vacíos** — Gradientes de color en lugar de thumbnails reales
4. **Mapa 3D placeholder** — "Próximamente" sin funcionalidad
5. **Email contacto** — `hola@danimarzan.com` (línea 346) — ¿existe este buzón?
6. **Sin Google Analytics / tracking**
7. **Sin meta OG image** — falta `og:image` para compartir
8. **Sin favicon real** — usa SVG inline (línea 13) — funciona pero no es profesional

### 🔧 Mejoras rápidas sugeridas
1. Reemplazar placeholder hero con foto real PNG (croma verde)
2. Conectar vídeos reales de YouTube (data-yt="VIDEO_ID")
3. Añadir `og:image` para compartir en redes
4. Verificar que hola@danimarzan.com existe y funciona
5. Añadir Calendly link en sección contacto

## Notas

- El repo usa Dokploy para auto-deploy (no GitHub Pages)
- El Dockerfile construye una imagen nginx estática
- Los cambios se reflejan al hacer push a master
- `site_v12.html` está en el PC de Dani, NO en el servidor ni en GitHub
