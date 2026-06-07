---
title: 📋 Playbook de Prospección Automatizada
---

# 📋 Playbook de Prospección Automatizada
## Hermes Agent → Dani Marzán

**Cliente:** Daniel Marzán
**Servicios:** Vídeo/Reels, gestión RRSS, desarrollo web
**Objetivo:** Hermes hace TODO el trabajo previo. Dani solo edita y envía.

---

## 1. Tu nicho (beachhead principal)

**Marcas DTC / e-commerce de EE.UU. del mercado hispano**
- Fundadores latinos o productos dirigidos a consumidor hispano
- Facturación estimada: $1M–$20M
- **Por qué este nicho:**
  - Viven del contenido → demanda recurrente (retainer mensual)
  - Tu bilingüismo = ventaja injusta (contenido en español auténtico)
  - Tienen presupuesto demostrable (si pagan anuncios, pagan contenido)
  - Decisor accesible (fundador o head of marketing)

**Carril secundario (20% del esfuerzo):**
- SaaS / startups pequeñas con funding reciente que necesiten vídeo explicativo/demo

---

## 2. Perfil de empresa ideal (ICP)

### Criterios de INCLUSIÓN (score ≥ 7/10 para pasar)

| Señal | Cómo detectarla | Puntos |
|-------|-----------------|--------|
| Facturación $1M–$20M | Tamaño equipo LinkedIn (5–80 emp.), tráfico web | 2 |
| Dolor de contenido visible | IG/TikTok <2 posts/semana, sin Reels, feed abandonado | 3 |
| Gasta en publicidad | Aparece en Meta Ad Library con anuncios activos | 2 |
| Sin equipo de vídeo interno | No hay "videographer" en LinkedIn; web sin vídeo | 1 |
| Mercado/idioma compatible | Web EN/ES; zona horaria América/Europa | 1 |
| Web pobre (upsell) | WordPress viejo, no responsive, diseño 2015 | 1 |

### Criterios de EXCLUSIÓN (descartar automáticamente)
- Equipo > 200 personas o < 3
- Ya tienen presencia de vídeo fuerte y reciente
- Agencias de marketing (competencia, no cliente)
- Sin redes sociales ni web localizable
- Sectores regulados pesados (farma, finanzas) en primera ronda

### Qué correos obtener (orden de prioridad)
1. Fundador/CEO (en marcas <30 empleados)
2. Head of Marketing / CMO / Marketing Manager
3. Brand / Content / Social Media Manager
4. Genérico marketing@ o hello@ (último recurso)

---

## 3. Pipeline (6 capas)

```
[1 SOURCING gratis] → [2 FILTRO/SCORING gratis] → [3 ENRIQUECIMIENTO créditos]
        → [4 INVESTIGACIÓN profunda gratis] → [5 BORRADOR LLM potente]
                → [6 ENTREGA a Dani: solo revisar y enviar]
```

### Capa 1 — Sourcing (0 créditos)
Fuentes en orden de calidad:
1. **Meta Ad Library** (facebook.com/ads/library) — filtra por país EE.UU. + palabras nicho
2. TikTok Creative Center / hashtags del sector
3. Google "marca + ecommerce + [Miami, Houston, LA]" + directorios DTC
4. Product Hunt / Hacker News (carril SaaS)
5. Crunchbase / AngelList público (funding reciente)
6. **Tu propia audiencia** — encuesta a 108K seguidores "¿tienes un negocio?"

### Capa 2 — Filtro y scoring (0 créditos)
Rellenar tabla ICP. Descarta < 7/10. Aquí muere el 60-70% sin gastar créditos.

### Capa 3 — Enriquecimiento (solo top ~25)
- Hunter.io Domain Search → emails + roles
- Hunter Email Verifier → solo confidence > 80%
- (Opcional) Apollo.io / RocketReach como respaldo

### Capa 4 — Investigación profunda (0 créditos)
Para cada empresa con email válido:
- Web: propuesta de valor, tono, idioma, blog/vídeo, calidad diseño
- Redes: frecuencia posteo, último post, Reels, seguidores, engagement
- **Dolor en una frase:** ej. "IG con 12K seguidores sin Reels desde marzo"
- **Gancho personal:** algo específico (producto, lanzamiento, post reciente)

### Capa 5 — Borrador (LLM potente)
Ver plantilla de prompt en sección 4. **NO usar el LLM gratis de Hermes para el texto final.**

### Capa 6 — Entrega a Dani
Registro con todos los campos. Estado: "Pendiente revisión". Dani edita 30 segundos, envía.

---

## 4. Plantilla de prompt enriquecido

```
Eres copywriter de cold outreach B2B. Escribe un email en [IDIOMA] de máximo 90 palabras.

REMITENTE: Daniel Marzán — creador audiovisual (60K YouTube, 48K TikTok),
ofrece Reels/contenido, gestión de RRSS y desarrollo web. Bilingüe ES/EN.
Portfolio: [URL_PORTFOLIO]  ·  CV: [URL_CV]

EMPRESA: [NOMBRE] — [qué hacen, sector, tamaño]
DOLOR DETECTADO: [frase concreta del problema]
GANCHO PERSONAL: [algo específico de su web/redes]
DESTINATARIO: [Nombre, cargo]

REGLAS:
- Abre con el gancho personal, NO con "Hola, me llamo".
- Conecta el dolor con UN resultado concreto que Dani puede dar.
- Tono cercano, profesional, cero relleno corporativo.
- Incluye el enlace al portfolio de forma natural y el CV como enlace.
- CTA suave: una llamada de 15 min, no pidas compra.
- NO menciones precio.
- Firma: Daniel Marzán + enlaces.

Devuelve: asunto (≤6 palabras) + cuerpo.
```

### Secuencia de seguimiento (3 borradores de golpe)
- **Email 1:** Gancho + dolor + CTA llamada
- **Email 2 (día +3):** "Te dejo un caso/ejemplo" + Reel relevante
- **Email 3 (día +7):** Cierre corto "¿lo dejo aquí o te encaja una llamada?"

---

## 5. Formato de registro (Google Sheet / Notion / CSV)

| Columna | Descripción |
|---------|-------------|
| Empresa | Nombre |
| Web | URL |
| Sector | DTC, SaaS, etc. |
| Tamaño | Empleados |
| Score | 0-10 |
| Dolor | 1 frase concreta |
| Gancho | Algo específico |
| Contacto | Nombre + cargo |
| Email | Verificado |
| Confidence | % Hunter |
| Idioma | EN / ES |
| Estado | Pendiente/Listo/Enviado/Respondió/Llamada/Cliente |
| Asunto | ≤6 palabras |
| Borrador 1 | Email principal |
| Borrador F/U 1 | Follow-up 1 |
| Borrador F/U 2 | Follow-up 2 |
| Fecha | |

**Estados:** Pendiente revisión → Listo para enviar → Enviado → Respondió → Llamada → Cliente

---

## 6. APIs e integraciones

| Función | Herramienta | Nota |
|---------|-------------|------|
| Emails por dominio | Hunter.io | Ya lo usas. Gratis 25-50/mes |
| Respaldo contactos | Apollo.io / RocketReach | Cuando Hunter falla |
| Señal gasto en ads | Meta Ad Library | Mejor filtro "puede pagar" |
| Tráfico/tamaño web | SimilarWeb / BuiltWith | Estimar facturación |
| Datos empresa/funding | Crunchbase básico | Carril SaaS |
| Verificación email | Hunter Verifier / NeverBounce | Solo confidence >80% |
| Redacción final | API Claude o GPT | NO el LLM gratis de Hermes |
| Registro/CRM | Google Sheets API o Notion API | Donde Hermes deposita leads |
| Envío | Gmail — solo Dani | Hermes NUNCA envía |

---

## 7. Instrucciones maestras para Hermes

```
ROL: Eres mi agente de prospección. Tu objetivo es entregarme cada día/semana
una lista de empresas listas para contactar, con el borrador de email ya escrito.
Yo solo reviso y envío. TÚ NUNCA ENVÍAS CORREOS.

NICHO: Marcas DTC/e-commerce de EE.UU. del mercado hispano ($1M–$20M).
Carril secundario (máx 20%): SaaS con funding reciente que necesite vídeo.

PROCESO (sigue el orden, no gastes créditos antes de filtrar):
1. SOURCING (0 créditos): reúne 60–100 dominios desde Meta Ad Library,
   TikTok, Google y Crunchbase. Prioriza los que tengan anuncios activos.
2. SCORING (0 créditos): puntúa cada uno con la rúbrica ICP. Descarta <7/10.
3. ENRIQUECE (créditos) solo el top 25: Hunter Domain Search + Verifier.
   Quédate solo con emails confidence >80% de fundador o marketing.
4. INVESTIGA (0 créditos) cada empresa con email válido: web, redes,
   frecuencia de posteo, dolor en 1 frase, gancho personal.
5. BORRADOR: rellena la plantilla de prompt y pásala a un LLM potente
   (Claude/GPT), NO al modelo gratis. Genera email 1 + 2 follow-ups.
6. ENTREGA: crea una fila por empresa en el registro, estado
   "Pendiente revisión", con todos los campos rellenos.

REGLAS DE ORO:
- Nicho estrecho > lista grande. Calidad sobre cantidad.
- Nunca gastes un crédito de Hunter en una empresa con score <7.
- Cada email debe abrir con un gancho específico de ESA empresa.
- El CV va como enlace, nunca como adjunto.
- No menciones precio en el primer email.
- Reporta al final: nº dominios reunidos, nº que pasaron el filtro,
  nº con email válido, nº borradores listos, créditos gastados.
```

---

## 8. Métricas y objetivos

- **Objetivo realista:** 25 contactos/quincena → 5-10% respuesta → 1-2 llamadas
- Mide por nicho: si SaaS responde mejor que e-commerce, redirige el foco
- Revisa plantillas cada 20 envíos: qué asunto abre más, qué dolor responde mejor
- Precio: va en la llamada, NO en el email

---

## 9. Próximo paso

**Primera tanda:** Hermes reúne 60 dominios desde Meta Ad Library + scoring ANTES de tocar Hunter. Así validamos el filtro sin gastar créditos.

---

## 🔗 CONEXIONES
- [[Banco de ideas — La Triple D - Mi generación]]
- [[Banco de ideas — Promesas rotas del sistema]]
- [[2026-06-03 - JESÚS G. MAESTRO - La felicidad es un timo]]
- [[ESTRATEGIA_CREDITOS]]
- [[hybrid_pipeline.py]]
- [[pipeline.py]]
