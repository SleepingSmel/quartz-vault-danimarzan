---
title: "Análisis: Vibe Marketing 2026 — ¿Podemos aplicarlo a nuestro outreach B2B?"
---

# Análisis: Vibe Marketing 2026 — ¿Podemos aplicarlo a nuestro outreach B2B?

> **Video:** "La nueva forma de hacer marketing en 2026" — Benja (Imperium)
> **Link:** https://youtu.be/U5XdnPy42uE
> **Duración:** ~31 min | **Analizado:** 2026-06-06

---

## El concepto clave: Vibe Marketing

**Definición:** El humano dirige (visión, estrategia, tono) y los agentes IA ejecutan. Heredero del "vibe coding" de Andrej Carpati. Formalizado por Greg Eisenberg y Mark Circle en 2025. +2,600 practicantes en 47 países.

**La predicción central:** Un "vibe marketer" skilled superará a equipos de 10 personas para fines de 2026.

**Las 4 eras del marketing:**
1. **Tradicional (1950-1990):** Equipos enormes, costes altísimos,Sin métrica
2. **Digital (2000-2015):** Google Ads, SEO, Facebook Ads. Especialistas por canal
3. **Growth Hacking / No-Code (2015-2024):** Zapier, Make, N8N. Stack de 8-12 herramientas, $3,000/mes
4. **Vibe Marketing (2025-):** Cloud Code/Codex + agentes. Una persona + agentes IA. Stack mínimo

---

## Lo que Benja reemplazó (casos concretos)

### 1. Media Buyer ($600/mes) → Cloud Code + Meta Ads API
- Conectó su cuenta de Meta Ads a Cloud Code vía API
- Le dice: "Créame una campaña de retargeting para estas personas"
- El agente ejecuta, recomienda cambios, duplica creativos, adapta a países
- Resultado: $600/mes ahorrados, trabaja 24/7, alertas automáticas

### 2. Diseñador (part-time) → Cloud Code + ChatGPT Images 2
- 50 gráficos generados con ángulos que ya demostraron funcionar
- Se suben automáticamente a la cuenta
- Período de evaluación → se cortan los que no sirven
- Con GPT Image 2 ya no se nota que es IA

### 3. SDR (prospección en frío) → Apollo + Instantly + Cloud Code
- Buscar leads en Apollo (segmentables por industria)
- Precalentar correos en Instantly
- Personalizar correos con Cloud Code (el agente visita la web del lead y redacta)
- Reply rate: de 1% a 3-4% con personalización

### 4. Investigación de contenido → Playwright + Cloud Code 24/7
- Scrapea tendencias del nicho
- Compara con su contenido → detecta áreas de mejora
- Idea de contenidos basados en lo que está funcionando
- Funciona 24/7 con Cloud Code Routines

**Stack actual de Benja:**
- Cloud Code (agente orquestador)
- ChatGPT Plus (reemplazó Canva + Photoshop)
- Higgsfield (generación de imágenes)
- Apollo + Instantly (prospección — sigue pagándolos)
- Coste total: ~$300/mes (antes $3,000+)

---

## El Framework VIBE

| Capa | ¿Qué es? | ¿Quién lo hace? |
|------|----------|-----------------|
| **V** — Visión | Estrategia, ICP, oferta, ángulo | ⚠️ SOLO el humano |
| **I** — Insumos | Brand voice, ICP, pricing, casos de éxito, competidores (archivos .md) | Humano crea, agente usa |
| **B** — Brain | El modelo de lenguaje (Claude, GPT) + Cloud Code/Codex | Agente |
| **E** — Engine | La capacidad de ejecutar 24/7 (Cloud Routines, N8N) | Agente |

**Los 4 juntos = VIBE. Si falta uno, no es vibe marketing, es chatbot.**

---

## ¿Podemos aplicarlo a NUESTRO outreach B2B?

### Estado actual de nuestro outreach
- **Paso 1:** Buscar leads en Google (manual, lento)
- **Paso 2:** Investigar web del lead (semi-automático con Firecrawl)
- **Paso 3:** Calificar con rubric (manual)
- **Paso 4:** Escribir email personalizado (manual)
- **Paso 5:** Enviar (manual)

### Aplicación del Vibe Marketing a nuestro flujo

#### 🔴 V — Visión (nosotros, no delegable)
- **ICP:** Abogados de inmigración en Houston, Med Spas en Miami
- **Oferta:** "Me encargo de que tus clientes te encuentran en Instagram"
- **Ángulo:** Video audit personalizado + propuesta sin compromiso
- **Tono:** Directo, profesional, sin relleno — estilo Benja

#### 🟡 I — Insumos (creamos una vez, agente usa siempre)
Archivos .md cargados en el agente:
- `brand.md` — Brand voice de Dani, tono, diferenciadores
- `icp.md` — Perfil exacto del cliente ideal por nicho (abogados inmigración, med spas)
- `oferta.md` — Servicios, precios, casos de éxito
- `competidores.md` — Qué hacen otros en cada nicho
- `scripts.md` — Guiones de audit probados

#### 🟢 B — Brain (agente)
Nuestro agente Pi ya es el "brain". Lo que tenemos que hacer es cargarle los insumos (I) y darle herramientas vía MCP o scripts.

#### 🟢 E — Engine (ejecución 24/7)
Aquí es donde hay más potencial no explotado:

**Motor de prospección automática:**
1. Buscar leads en Google (con Firecrawl/scraping) → segmentar por ICP
2. Investigar cada web automáticamente → extraer datos clave
3. Puntuar con rubric ≥ 7/10
4. Generar audit video script personalizado
5. Enviar email con propuesta

**Todo esto YA LO HACEMOS, pero semi-manual. El "engine" lo haría 24/7.**

---

## Propuesta concreta: implementar Vibe Outreach

### Fase 1: Insumos (esta semana)
- [ ] Crear `brand-dani.md` — Brand voice, tono, diferenciadores
- [ ] Crear `icp-inmigracion.md` — Perfil abogado inmigración ideal
- [ ] Crear `icp-medspas.md` — Perfil Med Spa ideal
- [ ] Crear `oferta.md` — Servicios + precios + casos
- [ ] Crear `scripts-audit.md` — Guiones audit por nicho

### Fase 2: Automatizar la investigación (semana 2)
- [ ] Scraping automático de webs de leads (Firecrawl)
- [ ] Extraer: servicios, reseñas, redes sociales, web quality score
- [ ] Puntuar automáticamente con rubric
- [ ] GenerarDataListado filtrado (≥ 7/10)

### Fase 3: Personalización de emails (semana 3)
- [ ] Conectar investigación → escritura de emails
- [ ] Email menciona algo específicodel lead (su web, un review, su competencia)
- [ ] A/B testing automático

### Fase 4: Engine 24/7 (mes 2)
- [ ] Cloud Code Routines o cron jobs que ejecuten el flujo completo
- [ ] Reporte semanal de leads encontrados, emails enviados, respuestas
- [ ] Alertas cuando hay respuestas positivas

---

## Herramientas que necesitamos

| Herramienta | Uso | ¿La tenemos? |
|------------|-----|-------------|
| **Apollo.io** | Base de datos de leads | ⚠️ Key existe pero free no sirve |
| **Instantly** | Precalentar emails, envío masivo | ❌ No contratado |
| **Cloud Code / Codex** | Agente orquestador | ✅ Ya lo usamos (Claude Code) |
| **Firecrawl** | Scraping webs leads | ✅ Ya lo tenemos |
| **Hunter.io** | Encontrar emails | ✅ Key existe, 0 créditos |
| **Make / N8N** | Automatizaciones entre herramientas | ❌ No configurado |
| **Google Sheets** | Base de datos leads | ✅ Ya existe (prospects.db) |

---

## Riesgos y consideraciones

1. **Hunter tiene 0 créditos** — Necesita recarga o alternativa (Apollo free + extracción manual)
2. **Instantly** — Si enviamos muchos emails, necesitamos precalentar dominio primero (2 semanas)
3. **El "engine" no es gratis** — Cloud Code/Codex consumen tokens. Hay que presupuestar
4. **Calidad > Cantidad** — Benja pasó reply rate de 1% a 4% con personalización. Sin personalización = spam
5. **El humano sigue siendo crítico** — Si el ICP es genérico, el agente amplifica mediocridad

---

## Veredicto

**Sí, podemos aplicarlo.** De hecho, ya estamos haciendo "vibe outreach" semi-manualmente:
- Usamos Firecrawl como "engine" de investigación
- Usamos Pi como "brain" para calificar y escribir
- Los insumos (ICP, oferta) ya están definidos en el vault

**Lo que falta:** Conectar todo en un flujo automatizado 24/7 que:
1. Busque leads automáticamente
2. Los investigue y puntúe
3. Genere emails personalizados
4. Los envíe
5. Reporte resultados

El modelo de Benja aplicado a outreach B2B no es solo posible — es exactamente lo que estamos construyendo. Solo falta conectar las piezas.
