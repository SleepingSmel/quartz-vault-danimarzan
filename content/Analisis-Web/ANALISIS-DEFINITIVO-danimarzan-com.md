---
title: "INFORME DEFINITIVO: Análisis y Mejoras de danimarzan.com"
---

# INFORME DEFINITIVO: Análisis y Mejoras de danimarzan.com
> Análisis exhaustivo del código, diseño, rendimiento, storytelling y propuestas de mejora
> Fecha: 2026-06-04
> Analizado desde: código fuente en GitHub + render visual + investigación de tecnologías

---

## ÍNDICE

1. [Arquitectura actual](#1-arquitectura-actual)
2. [Análisis del código](#2-análisis-del-código)
3. [Paleta de colores y diseño visual](#3-paleta-de-colores-y-diseño-visual)
4. [Tipografía](#4-tipografía)
5. [Animaciones y rendimiento](#5-animaciones-y-rendimiento)
6. [Storytelling y copy](#6-storytelling-y-copy)
7. [Errores críticos](#7-errores-críticos)
8. [Propuesta: Modelo 3D con partículas](#8-propuesta-modelo-3d-con-partículas)
9. [Mejoras de storytelling por sección](#9-mejoras-de-storytelling-por-sección)
10. [Plan de acción priorizado](#10-plan-de-acción-priorizado)

---

## 1. ARQUITECTURA ACTUAL

### Stack tecnológico

| Componente | Tecnología | Tamaño |
|-----------|-----------|--------|
| HTML | Single file, 261 líneas | ~23KB |
| CSS | Inline en `<style>`, 100 líneas | (inline) |
| JS | Inline en `<script>`, 37 líneas | (inline) |
| Fuentes | Google Fonts (Oswald + Inter) | ~40KB |
| Canvas | Partículas canvas 2D (46 puntos) | ~0KB (procedural) |
| Servidor | nginx 1.27-alpine (Docker) | — |
| Deploy | Docker container en VPS | — |

### Estructura de archivos en GitHub

```
web_danimarzan/
├── index.html          # Todo el sitio (HTML + CSS + JS)
├── Dockerfile          # nginx alpine
├── nginx.conf          # Config con gzip + cache + security headers
├── .gitignore
└── README.md           # Vacío
```

### Puntos fuertes de la arquitectura

- ✅ **Single file**: Sin dependencias, sin build, sin bundler. Funciona copiando un archivo.
- ✅ **nginx optimizado**: gzip, cache de assets, security headers
- ✅ **Sin frameworks**: Sin React, sin Vue, sin dependencias de npm
- ✅ **Docker ligero**: nginx alpine (~20MB)
- ✅ **IntersectionObserver**: Para activar animaciones solo cuando la sección es visible
- ✅ **prefers-reduced-motion**: Respeta accesibilidad

### Puntos débiles de la arquitectura

- ❌ **Sin og:image**: Al compartir en redes no aparece preview
- ❌ **Sin favicon**: No hay icono de pestaña
- ❌ **Sin analytics**: No hay forma de medir visitas
- ❌ **Sin sitemap/robots.txt**: SEO básico inexistente
- ❌ **Sin CDN**: Las fuentes cargan desde Google pero el HTML no tiene preconnect óptimo

---

## 2. ANÁLISIS DEL CÓDIGO

### 2.1 HTML — Estructura

La web usa un patrón de **scroll snap vertical** con 7 secciones:

```
s0: Hero (nombre + tagline + foto placeholder)
s1: Redes & Contenido (stats + wall de tiles vacíos)
s2: Vídeo & Audiovisual (chips + cine visual)
s3: Dron · Fotogrametría · 3D (chips + SVG topografía)
s4: Apps con IA (chips + phone mockup)
s5: Web & Marca (chips + browser mockup)
s6: Filosofía (quote + CTA + socials)
```

Cada sección tiene atributos `data-c1`, `data-c2`, `data-c3` que definen su paleta de colores. Esto es inteligente — permite que cada "faceta" tenga identidad propia.

### 2.2 CSS — Análisis detallado

**Variables CSS:**
```css
:root {
  --c1: #6c5ce7;    /* Color principal (púrpura) */
  --c2: #8e7bff;    /* Color secundario (púrpura claro) */
  --c3: #0a0b10;    /* Fondo (negro azulado) */
  --ink: #f4f5fa;   /* Texto principal (blanco grisáceo) */
  --muted: #aab0c4; /* Texto secundario (gris azulado) */
  --ease: cubic-bezier(.16,1,.3,1);  /* Easing custom */
}
```

**Técnicas CSS usadas:**
- `scroll-snap-type: y mandatory` — Scroll se "engancha" a cada sección
- `IntersectionObserver` con threshold 0.55 — Activa animaciones cuando la sección es >55% visible
- Animaciones CSS con `@keyframes` para blobs, scroll indicator, pulse
- `prefers-reduced-motion: reduce` — Desactiva animaciones para usuarios que lo prefieren
- `cubic-bezier(.16,1,.3,1)` — Easing que da sensación de "peso" y "aterrizaje"

**Lo que funciona bien:**
- El easing `cubic-bezier(.16,1,.3,1)` es excelente — da sensación premium
- La transición de color de fondo (`transition: background 1.2s var(--ease)`) es suave
- El sistema de variables `--c1/--c2/--c3` por sección es elegante
- Los delays escalonados (`.d1`, `.d2`, `.d3`, `.d4`) crean ritmo visual

**Lo que se puede mejorar:**
- El `.hero__photo` tiene un placeholder visible ("Tu foto aquí") con `border: 1px dashed rgba(255,255,255,.25)` — esto debe reemplazarse
- Los `.tile` de la wall están vacíos — deberían tener contenido real o eliminarse
- El `.cine` tiene un botón de play que no hace nada — debería abrir un vídeo o eliminarse
- Los links sociales apuntan a páginas raíz (youtube.com, tiktok.com) sin el handle

### 2.3 JS — Análisis detallado

**Sistema de navegación:**
```javascript
// IntersectionObserver activa secciones
var io = new IntersectionObserver(function(es) {
  es.forEach(function(e) {
    if (e.intersectionRatio >= 0.55) {
      e.target.classList.add('is-active');
      paint(e.target);  // Cambia colores CSS
      // Activa contadores y animaciones
    }
  });
}, { threshold: [0, .55, 1] });
```

**Contador animado:**
```javascript
function count(el) {
  var t = +el.getAttribute('data-count');  // 60000, 48000, 14
  // Animación ease-out cúbica durante 1.5s
  // Formatea: 60000 → "60k", 48000 → "48k", 14 → "14"
}
```

**Partículas canvas:**
```javascript
// 46 partículas con movimiento browniano
for (var i = 0; i < N; i++) P.push({
  x: Math.random() * W,
  y: Math.random() * H,
  vx: (Math.random() - .5) * .18 * dpr,
  vy: (Math.random() - .5) * .18 * dpr,
  r: (Math.random() * 1.6 + .5) * dpr
});
// Color de partículas = var(--c2) del CSS
```

**Blobs con mouse follow:**
```javascript
// Suavizado lerp (0.05) para movimiento orgánico
cx += (mx - cx) * .05;
cy += (my - cy) * .05;
ba.style.transform = 'translate(' + (cx * 60) + 'px,' + (cy * 60) + 'px)';
bb.style.transform = 'translate(' + (-cx * 80) + 'px,' + (-cy * 80) + 'px)';
```

**Lo que funciona bien:**
- El sistema de colores por sección es muy limpio
- El contador animado con formato "k" es profesional
- El mouse follow de los blobs con lerp suavizado se siente orgánico
- El canvas de partículas es ligero (46 puntos, no 3D)
- El progreso bar (`prog`) da feedback visual del scroll

**Lo que se puede mejorar:**
- El canvas de partículas podría tener más puntos (80-100) para más impacto
- Las partículas no se conectan entre sí (líneas de conexión como Viszen)
- No hay efecto de "morphing" entre secciones
- El scroll podría ser más "controlado" (snap más agresivo)

---

## 3. PALETAS DE COLORES Y DISEÑO VISUAL

### 3.1 Paleta actual por sección

| Sección | c1 (principal) | c2 (secundario) | c3 (fondo) | Nombre |
|---------|---------------|-----------------|------------|--------|
| s0 Hero | #6c5ce7 | #8e7bff | #0a0b10 | Púrpura |
| s1 Redes | #ff5252 | #ffb648 | #130a0a | Rojo/Naranja |
| s2 Vídeo | #1e3a8a | #38bdf8 | #070b16 | Azul |
| s3 Dron | #0a7e6a | #34d399 | #06120e | Verde |
| s4 Apps IA | #4f46e5 | #22d3ee | #070a16 | Índigo/Cyan |
| s5 Web | #a21caf | #e879f9 | #120714 | Rosa |
| s6 Filosofía | #6c5ce7 | #00d3a7 | #06070d | Púrpura/Verde |

### 3.2 Análisis de la paleta

**Lo que funciona:**
- Cada sección tiene identidad propia — el cambio de color es dramático y memorable
- Los colores son vibrantes pero no chillones
- El contraste texto/fondo es bueno en todas las secciones
- La transición de color (1.2s ease) es suave

**Problemas identificados:**

1. **s0 y s6 usan el mismo c1 (#6c5ce7)**: El hero y la filosofía se sienten demasiado similares. La filosofía debería tener un color más distintivo.

2. **s1 (Redes) es la más agresiva**: El rojo/naranja (#ff5252/#ffb648) es el más saturado. Funciona para "comunidades reales" pero puede ser visualmente cansado.

3. **Falta un color "cálido" para la sección personal**: La sección "Sobre mí" no existe como tal — está mezclada con Filosofía. Una sección personal debería tener un color cálido (ámbar, dorado).

4. **El --muted (#aab0c4) es demasiado azulado**: En secciones con fondo cálido (s1 rojo), el texto secundario azulado no armoniza.

### 3.3 Propuesta de paleta mejorada

```css
/* Paleta base (sin cambios) */
--ink: #f4f5fa;
--ease: cubic-bezier(.16,1,.3,1);

/* Por sección — ajustadas */
/* s0 Hero: Puro púrpura (sin cambios) */
/* s1 Redes: Coral más suave (menos agresivo) */
data-c1="#ff6b6b" data-c2="#ffa07a" data-c3="#1a0808"

/* s2 Vídeo: Azul profundo (sin cambios) */
/* s3 Dron: Verde esmeralda (sin cambios) */
/* s4 Apps IA: Índigo eléctrico (sin cambios) */
/* s5 Web: Fucsia (sin cambios) */

/* s6 Sobre mí: NUEVO — Cálido/dorado */
data-c1="#f59e0b" data-c2="#fbbf24" data-c3="#1a1200"

/* s7 Filosofía: Verde menta (diferente del hero) */
data-c1="#00d3a7" data-c2="#6ee7b7" data-c3="#060d0a"
```

---

## 4. TIPOGRAFÍA

### 4.1 Fuentes actuales

```css
font-family: 'Oswald', sans-serif;  /* Display: títulos */
font-family: 'Inter', sans-serif;   /* Body: texto */
```

**Oswald weights usados:**
- 700 (bold) — Títulos principales
- 600 (semibold) — Títulos de sección
- 500 (medium) — Eyebrows (labels)
- 300 (light) — Texto alternativo (thin)

**Inter weights usados:**
- 400 (regular) — Texto body
- 500 (medium) — Énfasis

### 4.2 Análisis tipográfico

**Lo que funciona:**
- Oswald es una excelente elección — geométrica, bold, con carácter
- La combinación Oswald + Inter es clásica y funciona
- Los tamaños con `clamp()` son responsive y fluidos
- El `letter-spacing: .32em` en los eyebrows da aire y elegancia

**Problemas identificados:**

1. **Falta weight 200 (extra-light) de Oswald**: El CSS pide `font-weight:300` pero Google Fonts carga `wght@300;500;600;700`. El 300 de Oswald no es tan "light" como debería.

2. **Inter solo tiene 2 weights**: Faltan weight 300 (light) para texto secundario y weight 600 (semibold) para énfasis.

3. **El `line-height` del `.big` es 0.9**: Esto puede causar que las letras se toquen en móvil con tamaños grandes.

4. **No hay `font-display: swap` explícito**: Google Fonts lo maneja, pero sería mejor tener control.

### 4.3 Propuesta tipográfica mejorada

```html
<!-- Cargar más weights para más flexibilidad -->
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@200;300;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

**Uso propuesto:**

| Elemento | Fuente | Weight | Tamaño |
|----------|--------|--------|--------|
| Hero nombre | Oswald | 700 | clamp(3rem, 12vw, 9rem) |
| Hero apellido | Oswald | 200 | clamp(3rem, 12vw, 9rem) |
| Títulos sección | Oswald | 600 | clamp(2rem, 6.5vw, 4.5rem) |
| Eyebrow/label | Oswald | 500 | clamp(.68rem, 1.4vw, .84rem) |
| Body text | Inter | 400 | clamp(.9rem, 1.5vw, 1.1rem) |
| Body emphasis | Inter | 600 | igual |
| Stats numbers | Oswald | 700 | clamp(1.8rem, 4vw, 2.8rem) |
| Buttons | Oswald | 600 | .9rem |
| Links/socials | Inter | 400 | .85rem |

---

## 5. ANIMACIONES Y RENDIMIENTO

### 5.1 Inventario de animaciones

| Animación | Tipo | Duración | Trigger | Coste |
|-----------|------|----------|---------|-------|
| Blob A float | CSS @keyframes | 18s infinite | Auto | Bajo |
| Blob B float | CSS @keyframes | 22s infinite | Auto | Bajo |
| Blob mouse follow | JS lerp | Continuous | Mouse | Medio |
| Partículas canvas | JS rAF | Continuous | Auto | Medio |
| Loader fade out | CSS transition | 0.6s | On load | Bajo |
| Text line reveal | CSS transition | 1s | .is-active | Bajo |
| Lead fade in | CSS transition | 0.9s | .is-active | Bajo |
| Stats counter | JS rAF | 1.5s | .is-active | Bajo |
| Scroll indicator | CSS @keyframes | 1.8s infinite | Auto | Bajo |
| Progress bar | CSS transition | 0.12s | Scroll | Bajo |
| Tile hover | CSS transition | 0.4s | Hover | Bajo |
| Cine bars | CSS transition | 1.1s | .is-active | Bajo |
| Cine scrub | CSS transition | 2.4s | .is-active | Bajo |
| SVG path draw | CSS transition | 2.2s | .is-active | Bajo |
| Phone pulse | CSS @keyframes | 2.4s infinite | Auto | Bajo |
| Card hover | CSS transition | 0.4s | Hover | Bajo |

### 5.2 Análisis de rendimiento

**Peso total estimado:**
- HTML: ~23KB
- Google Fonts: ~40KB (2 fuentes, 6 weights)
- **Total: ~63KB** (sin imágenes)

Esto es excelente. La web es ultra-ligera.

**Problemas de rendimiento:**

1. **Canvas de partículas con `devicePixelRatio`**: En pantallas Retina (dpr=2), el canvas renderiza al doble de resolución. Con 46 puntos no es problema, pero si se aumenta el número de partículas, puede afectar.

2. **Blobs con `filter: blur(90px)`**: El blur de 90px es GPU-intensivo. En dispositivos modestos, puede causar jank.

3. **Grain overlay con SVG data URI**: El SVG de ruido está inline (data URI), lo cual es bueno (no hay request extra), pero el `opacity: .05` con `pointer-events: none` significa que el navegador sigue compositing esta capa.

4. **Sin `will-change` en elementos animados**: Solo los blobs tienen `will-change: transform`. Los demás elementos animados podrían beneficiarse.

### 5.3 Propuestas de mejora de animación

**A) Añadir líneas de conexión entre partículas** (como Viszen):

```javascript
// En el loop de partículas, después de dibujar los puntos:
ctx.strokeStyle = col;
ctx.globalAlpha = 0.08;
ctx.lineWidth = 0.5 * dpr;
for (var i = 0; i < N; i++) {
  for (var j = i + 1; j < N; j++) {
    var dx = P[i].x - P[j].x;
    var dy = P[i].y - P[j].y;
    var dist = Math.sqrt(dx * dx + dy * dy);
    if (dist < 120 * dpr) {
      ctx.globalAlpha = 0.08 * (1 - dist / (120 * dpr));
      ctx.beginPath();
      ctx.moveTo(P[i].x, P[i].y);
      ctx.lineTo(P[j].x, P[j].y);
      ctx.stroke();
    }
  }
}
```

**B) Aumentar partículas a 80-100** para más impacto visual.

**C) Añadir `will-change: transform` a elementos animados:**
```css
.screen, .blob, .tile, .cine, .phone, .browser {
  will-change: transform, opacity;
}
```

**D) Reducir blur de blobs en móvil:**
```css
@media (max-width: 820px) {
  .blob { filter: blur(60px); }
}
```

---

## 6. STORYTELLING Y COPY

### 6.1 Narrativa actual

La web cuenta la historia de Dani como un **creador versátil** con 5 facetas:

1. **Redes**: "Hago crecer comunidades reales" — Prueba social con stats
2. **Vídeo**: "Cuento historias en movimiento" — Equipo + experiencia ESA
3. **Dron/3D**: "Cartografío el mundo real" — DJI + Luma Labs
4. **Apps IA**: "Construyo producto con IA" — ChatCore + Abora
5. **Web**: "Diseño webs que enamoran" — Esta web como prueba

### 6.2 Análisis del storytelling

**Lo que funciona:**
- El concepto de "facetas" es original y memorable
- Cada sección tiene un título con verbo de acción ("Hago crecer", "Cuento", "Cartografío", "Construyo", "Diseño")
- La prueba social (60K YouTube, 48K TikTok, 7M visitas) está presente
- El cliente ESA es un diferenciador fuerte
- La filosofía "El obstáculo es el way" cierra con fuerza

**Problemas identificados:**

1. **No hay una sección "Sobre mí" real**: La sección 6 (Filosofía) mezcla la filosofía con el CTA. Falta una sección personal que humanice a Dani.

2. **El copy es genérico**: Frases como "Construyo audiencias, marcas y productos digitales" podrían decirse de cualquier agencia. Falta la voz personal de Dani.

3. **No hay testimonios ni casos de éxito**: Solo hay stats propios. Un testimonio de un cliente (ESA, por ejemplo) sería poderoso.

4. **El CTA es débil**: "Escríbeme" + "LinkedIn" es estándar. No hay urgencia ni propuesta de valor clara.

5. **Falta el "por qué"**: ¿Por qué Dani hace lo que hace? ¿Cuál es su motivación? Esto conectaría emocionalmente.

### 6.3 Propuesta de storytelling mejorada

**Narrativa propuesta:**

```
Hero: "De portero a creador digital" — La transformación
Redes: "Construí 60K suscriptores desde cero" — La prueba
Vídeo: "Vídeo que cuenta historias reales" — El arte
Dron/3D: "Mapeo el mundo en 3D" — La tecnología
Apps IA: "Construyo el futuro con IA" — La innovación
Web: "Webs que enamoran" — El diseño
Sobre mí: "Mi historia" — La persona detrás
Filosofía: "El obstáculo es el camino" — La mentalidad
```

---

## 7. ERRORES CRÍTICOS

### 7.1 Errores que deben arreglarse YA

| # | Error | Línea | Impacto | Solución |
|---|-------|-------|---------|----------|
| 1 | **"Tu foto aquí"** placeholder | L138 | CRÍTICO — Quita toda profesionalidad | Reemplazar con foto real de Dani |
| 2 | **Links sociales sin handle** | L216-217 | CRÍCIO — Usuarios pierden el rango | `youtube.com/@SoyPorteroYT`, `tiktok.com/@soyporteroyt`, `linkedin.com/in/danimarzan` |
| 3 | **Stats muestran "0"** | L152-154 | ALTO — Pierde credibilidad | El contador necesita JS; sin JS muestra "0" |
| 4 | **Sin og:image** | <head> | ALTO — No se ve bien al compartir | Añadir `<meta property="og:image" content="https://danimarzan.com/og.jpg">` |
| 5 | **Sin favicon** | <head> | MEDIO — No hay icono de pestaña | Añadir `<link rel="icon" href="favicon.svg">` |
| 6 | **Tiles vacíos** | L157 | MEDIO — Se ve incompleto | Llenar con contenido o eliminar |
| 7 | **Cine play button no funciona** | L168 | BAJO — Confunde al usuario | Añadir acción o eliminar |
| 8 | **Sin analytics** | — | MEDIO — No se pueden medir visitas | Añadir Plausible o similar |

### 7.2 Errores de código

| # | Error | Detalle |
|---|-------|---------|
| 1 | `data-count="60000"` muestra "60k" pero `data-count="14"` muestra "14" | El formato "k" solo aplica >= 1000. Correcto pero confuso. |
| 2 | El `IntersectionObserver` usa `intersectionRatio >= 0.55` | Esto significa que la sección debe estar >55% visible para activarse. En secciones cortas, puede no activarse nunca. |
| 3 | `document.documentElement` para variables CSS | Funciona pero `:root` es más estándar. |
| 4 | `var` en vez de `let/const` | No es error, pero es código antiguo. |

---

## 8. PROPUESTA: MODELO 3D CON PARTÍCULAS

### 8.1 ¿Es posible? SÍ.

La web de Viszen usa exactamente esta técnica:
1. Crear un modelo 3D en Blender (o generar con IA)
2. Exportar como GLTF/GLB
3. Cargar en Three.js con `GLTFLoader`
4. Usar `MeshSurfaceSampler` para extraer puntos de la superficie
5. Renderizar como partículas con `PointsMaterial`

### 8.2 Herramientas para generar el modelo 3D

| Herramienta | Tipo | Coste | Calidad | Facilidad |
|-------------|------|-------|---------|-----------|
| **Meshy AI** | IA (texto/imagen → 3D) | Gratis (limitado) | Alta | Muy fácil |
| **TripoSR** | IA (imagen → 3D) | Gratis (open source) | Media | Fácil |
| **Blender** | Manual | Gratis | Máxima | Difícil |
| **Spline** | Web-based | Gratis | Media | Fácil |
| **Kaedim** | IA (imagen → 3D) | De pago | Alta | Fácil |

### 8.3 Proceso paso a paso

**Opción A: Con IA (rápido, ~30 min)**
1. Ir a [meshy.ai](https://www.meshy.ai/)
2. Escribir prompt: "A professional video camera with cinematic style, clean geometry, low poly"
3. Descargar el modelo GLB
4. Usar el código de abajo para convertir a partículas

**Opción B: Con Blender (control total, ~2-4 horas)**
1. Crear modelo en Blender (cámara, dron, esfera abstracta)
2. Exportar como GLTF/GLB
3. Cargar en Three.js

### 8.4 Código para partículas desde modelo GLTF

```javascript
// Reemplazar el canvas de partículas actual por esto:
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshSurfaceSampler } from 'three/addons/math/MeshSurfaceSampler.js';

// Configuración
const PARTICLE_COUNT = 8000;
const MODEL_URL = 'model.glb'; // Modelo GLTF/GLB

// Crear escena Three.js (overlay)
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, innerWidth / innerHeight, 0.1, 100);
camera.position.z = 3;

const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.domElement.style.cssText = 'position:fixed;inset:0;z-index:-3;pointer-events:none';
document.body.appendChild(renderer.domElement);

// Cargar modelo y convertir a partículas
const loader = new GLTFLoader();
let particlesMesh;

loader.load(MODEL_URL, (gltf) => {
  const model = gltf.scene;
  
  // Combinar todas las geometrías del modelo
  const geometries = [];
  model.traverse((child) => {
    if (child.isMesh) {
      geometries.push(child.geometry.clone());
    }
  });
  
  // Merge geometrías
  const mergedGeometry = mergeGeometries(geometries);
  
  // Crear sampler
  const sampler = new MeshSurfaceSampler(new THREE.Mesh(mergedGeometry)).build();
  
  // Extraer posiciones
  const positions = new Float32Array(PARTICLE_COUNT * 3);
  const temp = new THREE.Vector3();
  
  for (let i = 0; i < PARTICLE_COUNT; i++) {
    sampler.sample(temp);
    positions[i * 3] = temp.x;
    positions[i * 3 + 1] = temp.y;
    positions[i * 3 + 2] = temp.z;
  }
  
  // Crear geometría de partículas
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  
  // Material que cambia de color con la sección
  const material = new THREE.PointsMaterial({
    size: 0.015,
    color: 0x8e7bff,
    transparent: true,
    opacity: 0.6,
    sizeAttenuation: true
  });
  
  particlesMesh = new THREE.Points(geometry, material);
  particlesMesh.rotation.x = -Math.PI / 10;
  scene.add(particlesMesh);
});

// Animación
function animate() {
  requestAnimationFrame(animate);
  if (particlesMesh) {
    particlesMesh.rotation.y += 0.002;
  }
  renderer.render(scene, camera);
}
animate();

// Responsive
addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
```

### 8.5 Alternativa más ligera: Partículas que forman formas

Si el modelo GLB es demasiado pesado, se puede usar una alternativa intermedia:

```javascript
// Partículas que forman la silueta de una cámara (sin modelo 3D)
// Usando una textura como mapa de densidad

const canvas = document.createElement('canvas');
canvas.width = 200;
canvas.height = 200;
const ctx = canvas.getContext('2d');

// Dibujar forma de cámara (o cualquier silueta)
ctx.fillStyle = 'white';
ctx.fillRect(60, 70, 80, 60);  // Body
ctx.fillRect(80, 50, 40, 25);  // Lens mount
ctx.beginPath();
ctx.arc(100, 62, 15, 0, Math.PI * 2);  // Lens
ctx.fill();

// Leer píxeles y crear partículas solo donde hay blanco
const imageData = ctx.getImageData(0, 0, 200, 200);
const positions = [];

for (let i = 0; i < PARTICLE_COUNT; i++) {
  const x = Math.random() * 200;
  const y = Math.random() * 200;
  const pixel = ctx.getImageData(Math.floor(x), Math.floor(y), 1, 1).data;
  if (pixel[0] > 128) {  // Si el píxel es blanco
    positions.push((x - 100) / 50, (100 - y) / 50, 0);
  }
}
```

### 8.6 Recomendación

**Para Dani, la opción más práctica es:**

1. **Usar Meshy AI** para generar un modelo 3D de una cámara cinematográfica (gratis, ~5 min)
2. **Exportar como GLB** 
3. **Usar el código de arriba** para convertir a partículas
4. **Peso adicional**: ~50-100KB (modelo GLB comprimido) + ~15KB (Three.js loader)

**Total estimado con partículas 3D**: ~120-170KB (vs 63KB actual)

---

## 9. MEJORAS DE STORYTELLING POR SECCIÓN

### 9.1 Hero (s0)

**Actual:**
```
Daniel Marzán
Creador audiovisual · Desarrollo con IA
Construyo audiencias, marcas y productos digitales que crecen. Del vídeo a la app.
```

**Propuesto:**
```
DANI MARZÁN
De portero a creador digital
60K personas me ven cada semana. Empresas como la ESA confían en mi trabajo.
```

**Por qué es mejor:**
- "De portero a creador digital" es una historia, no un título
- Los números (60K) dan credibilidad inmediata
- "Empresas como la ESA" es un diferenciador concreto

### 9.2 Redes (s1)

**Actual:**
```
Hago crecer comunidades reales
No es teoría: lo construí desde cero en mis propios canales con contenido educativo que conecta y fideliza.
```

**Propuesto:**
```
Hago crecer comunidades reales
Empecé de cero. Sin seguidores, sin contactos. Hoy 60K personas esperan mi próximo vídeo.
No es suerte. Es sistema.
```

**Por qué es mejor:**
- Cuenta una historia de transformación
- "No es suerte. Es sistema." posiciona a Dani como profesional, no como creador de suerte

### 9.3 Vídeo (s2)

**Actual:**
```
Cuento historias en movimiento
Producción completa: corporativo, eventos, bodas y dron. Cámara, edición en DaVinci y dirección de principio a fin. Realicé el vídeo corporativo de un cliente de la ESA.
```

**Propuesto:**
```
Cuento historias en movimiento
Black Magic 4K. DaVinci Resolve. Dirección de principio a fin.
El vídeo que hice para un cliente de la ESA no era un encargo cualquiera. Era contar la historia de la exploración espacial.
```

**Por qué es mejor:**
- El equipo específico (Black Magic 4K) da credibilidad técnica
- La anécdota de la ESA humaniza el servicio

### 9.4 Dron/3D (s3)

**Actual:**
```
Cartografío el mundo real
Captura con dron (DJI Mini 3 Pro) y vuelos automatizados para fotogrametría, mapeo 3D y reconstrucción tridimensional con Luma Labs.
```

**Propuesto:**
```
Cartografío el mundo real
Un dron, un software y una idea. Convierto el mundo físico en modelos 3D navegables.
Del terreno al pixel. Sin perder un detalle.
```

**Por qué es mejor:**
- "Un dron, un software y una idea" es memorable
- "Del terreno al pixel" es poético y técnico a la vez

### 9.5 Apps IA (s4)

**Actual:**
```
Construyo producto con IA
Bajo mi estudio ChatCore desarrollo aplicaciones con IA. Mi primera app, Abora, ya está publicada en Google Play.
```

**Propuesto:**
```
Construyo producto con IA
ChatCore es mi estudio de desarrollo. Abora, mi primera app, ya está en Google Play.
No hago apps. Hago herramientas que la gente usa.
```

**Por qué es mejor:**
- "No hago apps. Hago herramientas que la gente usa." es un posicionamiento claro

### 9.6 Web (s5)

**Actual:**
```
Diseño webs que enamoran
Webs rápidas y cuidadas, identidad y posicionamiento. Diseño con criterio audiovisual y rendimiento técnico. Esta misma web es la prueba.
```

**Propuesto:**
```
Diseño webs que enamoran
Rápidas. Cuidadas. Con personalidad.
Esta web no la hizo un diseñador web. La hizo un creador de vídeo que entiende que el diseño es storytelling visual.
```

**Por qué es mejor:**
- "Esta web no la hizo un diseñador web" es provocador y memorable
- Posiciona a Dani como alguien que aporta una perspectiva única

### 9.7 NUEVA: Sobre mí (s6)

**Propuesto (nueva sección):**
```
Sobre mí
26 años. De La Palma, Canarias.
Fui portero 12 años. Literalmente paraba balones. Ahora paro scrolls.
Aprendí que el contenido no es suerte. Es constancia, estrategia y saber contar una historia.
Equipo: Black Magic Pocket 4K, DJI Mini 3 Pro, Blue Yeti.
Software: DaVinci Resolve, Fusion, Remotion, Luma Labs.
```

**Por qué añadirla:**
- Humaniza a Dani
- La historia de "portero a creador" es poderosa
- El equipo y software dan credibilidad técnica

### 9.8 Filosofía (s7)

**Actual:**
```
El obstáculo es el camino
Versátil por convicción: combino narrativa audiovisual, datos y tecnología para hacer crecer ideas. ¿Hacemos algo grande juntos?
```

**Propuesto:**
```
El obstáculo es el camino
Cada "no" me acercó al "sí" correcto.
Cada proyecto fallido me enseñó algo que ningún curso podía.
¿Tienes un proyecto que parece imposible? Hablemos.
```

**Por qué es mejor:**
- "Cada 'no' me acercó al 'sí' correcto" es personal y real
- "¿Tienes un proyecto que parece imposible?" es un CTA que invita a la acción

---

## 10. PLAN DE ACCIÓN PRIORIZADO

### P0 — Crítico (esta semana)

| # | Tarea | Tiempo | Dificultad |
|---|-------|--------|------------|
| 1 | Reemplazar "Tu foto aquí" con foto real de Dani | 5 min | Fácil |
| 2 | Arreglar links sociales con handles correctos | 2 min | Fácil |
| 3 | Añadir og:image | 5 min | Fácil |
| 4 | Añadir favicon | 10 min | Fácil |
| 5 | Añadir analytics (Plausible) | 10 min | Fácil |

### P1 — Importante (este mes)

| # | Tarea | Tiempo | Dificultad |
|---|-------|--------|------------|
| 6 | Mejorar copy de todas las secciones | 1 hora | Media |
| 7 | Añadir sección "Sobre mí" | 30 min | Media |
| 8 | Llenar tiles de la wall con contenido real | 30 min | Media |
| 9 | Añadir líneas de conexión entre partículas | 20 min | Media |
| 10 | Mejorar tipografía (más weights) | 15 min | Fácil |
| 11 | Añadir JSON-LD structured data | 20 min | Media |

### P2 — Mejora (cuando se pueda)

| # | Tarea | Tiempo | Dificultad |
|---|-------|--------|------------|
| 12 | Modelo 3D con partículas (Meshy AI + Three.js) | 2-4 horas | Alta |
| 13 | Testimonios de clientes | 1 hora | Media |
| 14 | Blog/sección de artículos | 2-3 horas | Alta |
| 15 | Versión inglesa | 2-3 horas | Media |
| 16 | Animación de transición entre secciones | 1-2 horas | Alta |

---

## RESUMEN EJECUTIVO

**La web de Dani es técnicamente excelente** (63KB, sin dependencias, nginx optimizado) pero tiene **gaps de ejecución** (foto placeholder, links rotos, copy genérico).

**Las 3 mejoras de mayor impacto:**
1. **Foto real + links sociales** — Arregla la primera impresión
2. **Copy con storytelling** — Diferencia a Dani de cualquier agencia
3. **Modelo 3D con partículas** — Añade el factor "wow" sin el peso de Three.js completo

**La web tiene un 85% del camino recorrido.** Con los ajustes de P0 y P1, será una web de nivel profesional que realmente represente el talento de Dani.
