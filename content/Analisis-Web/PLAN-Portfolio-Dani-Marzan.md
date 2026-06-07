---
title: "PLAN: Portfolio Dani Marzán — Estilo Viszen Simplificado"
---

# PLAN: Portfolio Dani Marzán — Estilo Viszen Simplificado
> Análisis profundo + Plan de implementación
> Fecha: 2026-06-04

---

## 1. ANÁLISIS DEL EFECTO VISZEN

### 1.1 Qué hace que funcione

La web de Viszen no es solo bonita — es una **máquina de_scroll**:

1. **Scroll como narrativa**: cada sección aparece con timing perfecto. El scroll no es mover contenido, es **dirigir la atención**.
2. **Dark + minimal**: fondo negro (#0a0a0a), texto claro (#e0e0e0), CERO ruido visual. Cada elemento que aparece tiene peso.
3. **Tipografía como hero**: Oswald bold ocupa pantalla completa. El texto ES el diseño.
4. **Canvas 3D genera intriga**: no entiendes qué es exactamente, pero sabes que hay algo vivo detrás.

### 1.2 El efecto que hay que replicar (sin el peso)

El efecto core es: **"slides que van bajando con revelación progresiva"**. No es un scroll normal — es un **scroll controlado** donde:

- Cada sección ocupa **exactamente 100vh** (pantalla completa)
- Al hacer scroll, la sección actual **se desvanece/eleva** y la nueva **aparece desde abajo**
- El contenido de cada sección tiene **timing escalonado**: primero el titular, luego el subtítulo, luego los detalles
- Hay una **navegación lateral/fija** que indica en qué sección estás

### 1.3 Qué sobra (y hay que quitar)

| Elemento Viszen | Por qué sobra |
|----------------|---------------|
| Three.js partículas/fluido | 500KB+ de JS, GPU intensivo, no aporta al mensaje |
| GLTFLoader de modelos 3D | Requiere archivos GLB pesados, lazy loading complejo |
| Morphing de geometrías | Impresionante pero nadie lo nota conscientemente |
| DRACOLoader | Solo para comprimir modelos 3D que no necesitamos |
| Mouse-follow particles | Distrae del contenido |

---

## 2. LA ALTERNATIVA LIGERA

### 2.1 Efecto "3D rotatorio" sin Three.js

El efecto 3D de Viszen se puede replicar con **CSS 3D transforms + GSAP**:

```css
/* Pseudo-3D con CSS puro */
.card-3d {
  transform: perspective(1000px) rotateY(-5deg) rotateX(2deg);
  transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}
.card-3d:hover {
  transform: perspective(1000px) rotateY(0deg) rotateX(0deg) scale(1.02);
}
```

Esto da sensación de profundidad sin WebGL. Combinado con:
- **Gradientes sutiles** que simulan iluminación
- **Sombras dinámicas** que reaccionan al hover
- **Parallax de capas** (fondo más lento que primer plano)

### 2.2 Efecto "texto a la derecha con distintos colores"

Cada sección alterna layout:

```
Sección impar:  [Texto izq] [Visual der]
Sección par:    [Visual izq] [Texto der]
```

Con colores de acento que rotan por sección:
- Sección 1: Azul (#3b82f6)
- Sección 2: Verde (#22c55e)
- Sección 3: Naranja (#f59e0b)
- Sección 4: Rosa (#ec4899)

### 2.3 Scroll controlado (el corazón del efecto)

```javascript
// GSAP ScrollTrigger — scroll "snap" suave
gsap.utils.toArray("section").forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    start: "top top",
    end: "bottom top",
    snap: {
      snapTo: 1,
      duration: {min: 0.2, max: 0.6},
      ease: "power1.inOut"
    }
  });
});

// Revelación de contenido por sección
gsap.from(section.querySelectorAll(".reveal"), {
  y: 60,
  opacity: 0,
  duration: 0.8,
  stagger: 0.15,
  ease: "power3.out",
  scrollTrigger: {
    trigger: section,
    start: "top 80%",
    toggleActions: "play none none reverse"
  }
});
```

---

## 3. ARQUITECTURA DEL PROYECTO

### 3.1 Estructura de archivos

```
web_danimarzan/
├── index.html          # Todo en un solo archivo (simplicidad)
├── style.css           # Estilos (puede ser inline en index.html)
├── script.js           # GSAP + animaciones
├── assets/
│   ├── daniphoto.jpg   # Foto de Dani
│   └── projects/       # Screenshots de proyectos
│       ├── project1.jpg
│       ├── project2.jpg
│       └── project3.jpg
└── README.md
```

### 3.2 Secciones (slides)

| # | Sección | Contenido | Layout | Color acento |
|---|---------|-----------|--------|--------------|
| 1 | **Hero** | Logo "DM" + tagline + scroll indicator | Centrado | Blanco |
| 2 | **Servicios** | 4 cards: Vídeo, Redes, Web, Formación | 2x2 grid | Azul |
| 3 | **Portfolio** | 3 proyectos con preview | Texto izq / Visual der | Verde |
| 4 | **Sobre mí** | Bio + foto + stats | Visual izq / Texto der | Naranja |
| 5 | **Contacto** | Formulario + links | Centrado | Rosa |

### 3.3 Peso estimado

| Archivo | Tamaño |
|---------|--------|
| HTML | ~12KB |
| CSS | ~15KB |
| JS (GSAP CDN) | ~90KB (cached) |
| Fuentes (2 weights) | ~40KB |
| Imágenes optimizadas | ~150KB |
| **TOTAL** | **~307KB** |

---

## 4. ESPECIFICACIONES TÉCNICAS

### 4.1 HTML — Estructura base

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dani Marzán — Creador de Contenido</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@200;400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Loader -->
  <div id="loader">
    <div class="loader-logo">DM</div>
  </div>

  <!-- Navegación lateral -->
  <nav id="side-nav">
    <a href="#hero" class="nav-dot active" data-label="Inicio"></a>
    <a href="#servicios" class="nav-dot" data-label="Servicios"></a>
    <a href="#portfolio" class="nav-dot" data-label="Portfolio"></a>
    <a href="#sobre-mi" class="nav-dot" data-label="Sobre mí"></a>
    <a href="#contacto" class="nav-dot" data-label="Contacto"></a>
  </nav>

  <!-- Secciones -->
  <main>
    <section id="hero" class="slide">
      <div class="slide-content">
        <h1 class="hero-title">
          <span class="line">DANI</span>
          <span class="line accent">MARZÁN</span>
        </h1>
        <p class="hero-subtitle reveal">Hago que te encuentren en internet</p>
        <div class="hero-cta reveal">
          <a href="#servicios" class="btn-primary">Ver servicios</a>
          <a href="#portfolio" class="btn-secondary">Portfolio</a>
        </div>
      </div>
      <div class="scroll-indicator">
        <div class="mouse">
          <div class="wheel"></div>
        </div>
        <span>Scroll</span>
      </div>
    </section>

    <section id="servicios" class="slide">
      <div class="slide-content layout-split">
        <div class="col-text">
          <h2 class="section-title"><span class="accent-blue">01.</span> Servicios</h2>
          <p class="section-desc">Contenido que convierte. Diseño que impresiona.</p>
        </div>
        <div class="col-cards">
          <div class="card reveal" data-color="blue">
            <div class="card-icon">🎬</div>
            <h3>Vídeo</h3>
            <p>Profesional, corporativo, educativo</p>
          </div>
          <div class="card reveal" data-color="green">
            <div class="card-icon">📱</div>
            <h3>Redes</h3>
            <p>Estrategia + contenido + gestión</p>
          </div>
          <div class="card reveal" data-color="orange">
            <div class="card-icon">🌐</div>
            <h3>Web</h3>
            <p>Diseño + desarrollo + SEO</p>
          </div>
          <div class="card reveal" data-color="pink">
            <div class="card-icon">🎓</div>
            <h3>Formación</h3>
            <p>Sesiones online personalizadas</p>
          </div>
        </div>
      </div>
    </section>

    <section id="portfolio" class="slide">
      <div class="slide-content layout-split alt">
        <div class="col-visual">
          <div class="project-showcase reveal">
            <div class="project-slide active" data-project="1">
              <div class="project-image placeholder-img"></div>
            </div>
          </div>
        </div>
        <div class="col-text">
          <h2 class="section-title"><span class="accent-green">02.</span> Portfolio</h2>
          <div class="project-list">
            <div class="project-item active reveal" data-project="1">
              <h3>Vídeo Corporativo ESA</h3>
              <p>Vídeo institucional para la Agencia Espacial Europea</p>
              <span class="tag">Vídeo</span><span class="tag">Corporativo</span>
            </div>
            <div class="project-item reveal" data-project="2">
              <h3>Gestión Redes Sociales</h3>
              <p>Estrategia de contenido para e-commerce DTC</p>
              <span class="tag">Redes</span><span class="tag">Estrategia</span>
            </div>
            <div class="project-item reveal" data-project="3">
              <h3>Formación FP Online</h3>
              <p>Producción audiovisual para formación profesional</p>
              <span class="tag">Educación</span><span class="tag">Vídeo</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="sobre-mi" class="slide">
      <div class="slide-content layout-split">
        <div class="col-text">
          <h2 class="section-title"><span class="accent-orange">03.</span> Sobre mí</h2>
          <p class="section-desc">Soy Dani, 26 años, de La Palma. Ex-portero, ahora creador de contenido y freelancer digital.</p>
          <p class="section-desc">Equipo profesional (Black Magic 4K, DJI Mini 3 Pro, Blue Yeti) + DaVinci Resolve + Remotion para crear contenido que destaca.</p>
          <div class="stats reveal">
            <div class="stat"><span class="stat-num">60K</span><span class="stat-label">YouTube subs</span></div>
            <div class="stat"><span class="stat-num">48K</span><span class="stat-label">TikTok</span></div>
            <div class="stat"><span class="stat-num">7M+</span><span class="stat-label">Visitas</span></div>
          </div>
        </div>
        <div class="col-visual">
          <div class="profile-frame reveal">
            <div class="profile-image placeholder-photo"></div>
          </div>
        </div>
      </div>
    </section>

    <section id="contacto" class="slide">
      <div class="slide-content centered">
        <h2 class="section-title"><span class="accent-pink">04.</span> Hablemos</h2>
        <p class="section-desc">¿Tienes un proyecto? Cuéntame.</p>
        <form class="contact-form reveal" action="#" method="POST">
          <input type="text" name="name" placeholder="Nombre" required>
          <input type="email" name="email" placeholder="Email" required>
          <textarea name="message" placeholder="¿En qué puedo ayudarte?" rows="4" required></textarea>
          <button type="submit" class="btn-primary">Enviar mensaje</button>
        </form>
        <div class="social-links reveal">
          <a href="https://youtube.com/@SoyPorteroYT" target="_blank">YouTube</a>
          <a href="https://tiktok.com/@soyporteroyt" target="_blank">TikTok</a>
          <a href="https://instagram.com/danimarzan" target="_blank">Instagram</a>
          <a href="https://linkedin.com/in/danimarzan" target="_blank">LinkedIn</a>
        </div>
      </div>
    </section>
  </main>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
```

### 4.2 CSS — Estilos clave

```css
/* === RESET & BASE === */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --bg: #0a0a0a;
  --bg-light: #141414;
  --text: #e0e0e0;
  --text-muted: #888888;
  --accent-blue: #3b82f6;
  --accent-green: #22c55e;
  --accent-orange: #f59e0b;
  --accent-pink: #ec4899;
  --font-display: 'Oswald', sans-serif;
  --font-body: 'Inter', sans-serif;
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--text);
  overflow-x: hidden;
  line-height: 1.6;
}

/* === LOADER === */
#loader {
  position: fixed;
  inset: 0;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  transition: opacity 0.6s var(--ease-out), visibility 0.6s;
}
#loader.hidden {
  opacity: 0;
  visibility: hidden;
}
.loader-logo {
  font-family: var(--font-display);
  font-size: 4rem;
  font-weight: 700;
  color: var(--text);
  animation: pulse 1.5s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

/* === SIDE NAV === */
#side-nav {
  position: fixed;
  right: 2rem;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.nav-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--text-muted);
  opacity: 0.4;
  transition: all 0.3s var(--ease-out);
  position: relative;
}
.nav-dot.active {
  background: var(--text);
  opacity: 1;
  transform: scale(1.3);
}
.nav-dot:hover::after {
  content: attr(data-label);
  position: absolute;
  right: 24px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.75rem;
  white-space: nowrap;
  color: var(--text-muted);
}

/* === SLIDES === */
.slide {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 8vw;
  position: relative;
  overflow: hidden;
}

.slide-content {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

/* === HERO === */
#hero {
  text-align: center;
}
.hero-title {
  font-family: var(--font-display);
  font-size: clamp(4rem, 15vw, 12rem);
  font-weight: 700;
  line-height: 0.9;
  letter-spacing: -0.02em;
  margin-bottom: 2rem;
}
.hero-title .line {
  display: block;
}
.hero-title .line.accent {
  font-weight: 200;
  color: var(--text-muted);
}
.hero-subtitle {
  font-size: clamp(1rem, 2.5vw, 1.5rem);
  color: var(--text-muted);
  margin-bottom: 3rem;
  font-weight: 300;
}
.hero-cta {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* === BUTTONS === */
.btn-primary {
  display: inline-block;
  padding: 1rem 2.5rem;
  background: var(--text);
  color: var(--bg);
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: none;
  cursor: pointer;
  transition: all 0.3s var(--ease-out);
  text-decoration: none;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(255,255,255,0.1);
}
.btn-secondary {
  display: inline-block;
  padding: 1rem 2.5rem;
  background: transparent;
  color: var(--text);
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: 1px solid var(--text-muted);
  cursor: pointer;
  transition: all 0.3s var(--ease-out);
  text-decoration: none;
}
.btn-secondary:hover {
  border-color: var(--text);
  transform: translateY(-2px);
}

/* === SCROLL INDICATOR === */
.scroll-indicator {
  position: absolute;
  bottom: 3rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  opacity: 0.6;
}
.mouse {
  width: 24px;
  height: 36px;
  border: 2px solid var(--text-muted);
  border-radius: 12px;
  position: relative;
}
.wheel {
  width: 3px;
  height: 8px;
  background: var(--text-muted);
  border-radius: 2px;
  position: absolute;
  top: 6px;
  left: 50%;
  transform: translateX(-50%);
  animation: scrollWheel 2s ease-in-out infinite;
}
@keyframes scrollWheel {
  0% { opacity: 1; transform: translateX(-50%) translateY(0); }
  100% { opacity: 0; transform: translateX(-50%) translateY(12px); }
}
.scroll-indicator span {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--text-muted);
}

/* === SECTION TITLES === */
.section-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 700;
  line-height: 1;
  margin-bottom: 1.5rem;
}
.section-title .accent-blue { color: var(--accent-blue); }
.section-title .accent-green { color: var(--accent-green); }
.section-title .accent-orange { color: var(--accent-orange); }
.section-title .accent-pink { color: var(--accent-pink); }
.section-desc {
  font-size: 1.1rem;
  color: var(--text-muted);
  max-width: 500px;
  margin-bottom: 3rem;
}

/* === LAYOUT SPLIT === */
.layout-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}
.layout-split.alt {
  direction: rtl;
}
.layout-split.alt > * {
  direction: ltr;
}

/* === CARDS === */
.col-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}
.card {
  background: var(--bg-light);
  padding: 2rem;
  border: 1px solid rgba(255,255,255,0.05);
  transition: all 0.4s var(--ease-out);
  position: relative;
  overflow: hidden;
}
.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--card-accent, var(--accent-blue));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s var(--ease-out);
}
.card:hover {
  transform: translateY(-4px);
  border-color: rgba(255,255,255,0.1);
}
.card:hover::before {
  transform: scaleX(1);
}
.card[data-color="blue"] { --card-accent: var(--accent-blue); }
.card[data-color="green"] { --card-accent: var(--accent-green); }
.card[data-color="orange"] { --card-accent: var(--accent-orange); }
.card[data-color="pink"] { --card-accent: var(--accent-pink); }
.card-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}
.card h3 {
  font-family: var(--font-display);
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.card p {
  font-size: 0.9rem;
  color: var(--text-muted);
}

/* === PROJECT LIST === */
.project-item {
  padding: 1.5rem 0;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  cursor: pointer;
  transition: all 0.3s var(--ease-out);
  opacity: 0.5;
}
.project-item.active {
  opacity: 1;
  padding-left: 1rem;
  border-left: 2px solid var(--accent-green);
}
.project-item h3 {
  font-family: var(--font-display);
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.3rem;
}
.project-item p {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 0.5rem;
}
.tag {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  background: rgba(255,255,255,0.05);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-right: 0.5rem;
  color: var(--text-muted);
}

/* === STATS === */
.stats {
  display: flex;
  gap: 3rem;
  margin-top: 2rem;
}
.stat {
  text-align: center;
}
.stat-num {
  display: block;
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--accent-orange);
}
.stat-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

/* === PROFILE === */
.profile-frame {
  position: relative;
  aspect-ratio: 3/4;
  max-width: 350px;
  margin: 0 auto;
}
.profile-image {
  width: 100%;
  height: 100%;
  background: var(--bg-light);
  border: 1px solid rgba(255,255,255,0.05);
  /* background-image: url('assets/daniphoto.jpg'); */
  background-size: cover;
  background-position: center;
}

/* === CONTACT === */
.centered {
  text-align: center;
}
.contact-form {
  max-width: 500px;
  margin: 0 auto 3rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.contact-form input,
.contact-form textarea {
  padding: 1rem 1.5rem;
  background: var(--bg-light);
  border: 1px solid rgba(255,255,255,0.05);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 1rem;
  transition: border-color 0.3s;
}
.contact-form input:focus,
.contact-form textarea:focus {
  outline: none;
  border-color: var(--accent-pink);
}
.social-links {
  display: flex;
  gap: 2rem;
  justify-content: center;
}
.social-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  transition: color 0.3s;
}
.social-links a:hover {
  color: var(--text);
}

/* === REVEAL (GSAP target) === */
.reveal {
  opacity: 0;
  transform: translateY(40px);
}

/* === RESPONSIVE === */
@media (max-width: 768px) {
  .layout-split {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .layout-split.alt {
    direction: ltr;
  }
  .col-cards {
    grid-template-columns: 1fr;
  }
  .stats {
    gap: 1.5rem;
  }
  .stat-num {
    font-size: 1.8rem;
  }
  #side-nav {
    right: 1rem;
  }
  .slide {
    padding: 4rem 5vw;
  }
}
```

### 4.3 JS — Animaciones GSAP

```javascript
// === LOADER ===
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('loader').classList.add('hidden');
    initAnimations();
  }, 800);
});

// === INIT ===
function initAnimations() {
  gsap.registerPlugin(ScrollTrigger);

  // === SIDE NAV ACTIVE STATE ===
  const sections = document.querySelectorAll('.slide');
  sections.forEach((section, i) => {
    ScrollTrigger.create({
      trigger: section,
      start: 'top center',
      end: 'bottom center',
      onEnter: () => updateNav(i),
      onEnterBack: () => updateNav(i)
    });
  });

  function updateNav(activeIndex) {
    document.querySelectorAll('.nav-dot').forEach((dot, i) => {
      dot.classList.toggle('active', i === activeIndex);
    });
  }

  // === SECTION REVEALS ===
  document.querySelectorAll('.slide').forEach(section => {
    const reveals = section.querySelectorAll('.reveal');
    if (reveals.length) {
      gsap.to(reveals, {
        y: 0,
        opacity: 1,
        duration: 0.8,
        stagger: 0.12,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: section,
          start: 'top 75%',
          toggleActions: 'play none none reverse'
        }
      });
    }
  });

  // === HERO LINES ===
  gsap.from('.hero-title .line', {
    y: 100,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: 'power3.out',
    delay: 0.3
  });

  // === SCROLL INDICATOR HIDE ===
  gsap.to('.scroll-indicator', {
    opacity: 0,
    scrollTrigger: {
      trigger: '#servicios',
      start: 'top 80%',
      toggleActions: 'play none none none'
    }
  });

  // === PROJECT INTERACTION ===
  const projectItems = document.querySelectorAll('.project-item');
  const projectSlides = document.querySelectorAll('.project-slide');
  projectItems.forEach(item => {
    item.addEventListener('click', () => {
      const projectId = item.dataset.project;
      projectItems.forEach(p => p.classList.remove('active'));
      item.classList.add('active');
      projectSlides.forEach(s => {
        s.classList.toggle('active', s.dataset.project === projectId);
      });
    });
  });

  // === CARD HOVER 3D TILT ===
  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = (y - centerY) / 20;
      const rotateY = (centerX - x) / 20;
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });

  // === SMOOTH SCROLL FOR NAV LINKS ===
  document.querySelectorAll('.nav-dot').forEach(dot => {
    dot.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(dot.getAttribute('href'));
      gsap.to(window, {duration: 0.8, scrollTo: target, ease: 'power3.inOut'});
    });
  });

  // === CONTACT FORM ===
  const form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('button');
      btn.textContent = 'Enviado ✓';
      btn.style.background = 'var(--accent-green)';
      setTimeout(() => {
        btn.textContent = 'Enviar mensaje';
        btn.style.background = '';
        form.reset();
      }, 2000);
    });
  }
}
```

---

## 5. PLAN DE IMPLEMENTACIÓN

### Fase 1: Estructura (30 min)
1. Crear `index.html` con la estructura completa
2. Crear `style.css` con todos los estilos
3. Verificar que se vea bien sin JS

### Fase 2: Animaciones (20 min)
1. Añadir GSAP via CDN
2. Implementar `script.js`
3. Probar scroll y reveals

### Fase 3: Contenido real (30 min)
1. Reemplazar placeholders con contenido real de Dani
2. Añadir foto de perfil
3. Añadir screenshots de proyectos

### Fase 4: Deploy (10 min)
1. Push a GitHub
2. Activar GitHub Pages
3. Verificar en móvil y desktop

---

## 6. CHECKLIST FINAL

- [ ] HTML semántico con 5 secciones
- [ ] CSS con variables, dark theme, responsive
- [ ] GSAP ScrollTrigger para reveals
- [ ] Loader con fade out
- [ ] Navegación lateral con dots
- [ ] Cards con hover 3D tilt
- [ ] Project list interactiva
- [ ] Formulario de contacto funcional
- [ ] Scroll indicator animado
- [ ] Responsive mobile-first
- [ ] Peso total < 400KB
- [ ] Deploy en GitHub Pages
