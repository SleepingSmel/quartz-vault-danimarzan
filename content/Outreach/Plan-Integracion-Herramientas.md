---
title: Plan de Integración de Herramientas — Outreach B2B
---

# Plan de Integración de Herramientas — Outreach B2B

> **Fecha:** 2026-06-06
> **Objetivo:** Integrar las herramientas del tutorial de Vibe Marketing + herramientas gratuitas en nuestro flujo de outreach

---

## Herramientas del tutorial de Benja → Nuestra alternativa gratuita

| Herramienta de Benja | ¿Qué hace? | Nuestra alternativa gratuita | ¿Funciona igual? |
|---------------------|------------|----------------------------|------------------|
| **Apollo.io** (de pago) | Base de datos de empresas y emails | **Hunter.io free** (25 búsquedas/mes) + **Snov.io free** (50 créditos/mes) + **Outscraper Google Maps** (500 registros/mes) | Sí, combinamos 3 herramientas gratis para igualar Apollo |
| **Instantly.ai** (de pago) | Envío masivo de emails + calentamiento | **Snov.io free** (100 destinatarios/mes) + **Gmail propio** (500 emails/día) | Parcial — no tiene calentamiento automático, pero funciona para empezar |
| **Cloud Code** (Anthropic) | Agente IA orquestador | **Pi / Claude Code** (ya lo tenemos) | Sí, equivalente |
| **ChatGPT Images 2** | Generar imágenes para anuncios | **Firecrawl + Pi** (análisis) + **Canva free** (diseño básico) | Parcial — no generamos imágenes de anuncios, pero no es necesario ahora |
| **Playwright** | Navegar webs automáticamente | **Firecrawl** (ya está integrado) | Sí, Firecrawl hace lo mismo |
| **Meta Ads** | Anuncios en Facebook/Instagram | **No aplicable ahora** — buscamos contacto directo, no publicidad | N/A |
| **Higgsfield/Hixfield** | Generar vídeo/imagen con IA | **No necesario ahora** — no hacemos anuncios pagados | N/A |
| **Google Trends** | Investigar tendencias | **Firecrawl + Pi** (buscar tendencias manualmente) | Sí, con más trabajo manual |

---

## Stack definitivo gratuito

### Búsqueda de leads
1. **Outscraper Google Maps** (free) — Buscar negocios por zona + extraer datos
2. **Hunter.io** (free, 25 búsquedas/mes) — Encontrar emails
3. **Snov.io** (free, 50 créditos/mes) — Encontrar + verificar emails alternativos

### Investigación
4. **Firecrawl** (API key ya configurada) — Analizar webs de leads
5. **Pi / Claude Code** — Analizar datos, puntuar, escribir emails

### Envío
6. **Gmail propio** (hola@danimarzan.com) — Enviar emails (500/día)
7. **Snov.io** (free, 100 destinatarios/mes) — Alternativa de envío con seguimiento

### Organización
8. **Google Sheets** o **SQLite** (prospects.db) — Base de datos de leads
9. **Telegram** — Reportes diarios a Daniel

---

## Cómo conectar las herramientas en el flujo

```
DÍA 9:00 AM — Cron job se activa

┌─────────────────────────────────────────────────────────────┐
│ PASO 1: BUSCAR LEADS                                        │
│                                                             │
│ Outscraper Google Maps → CSV con datos de empresas          │
│                                                             │
│ Nicho del día:                                              │
│ - L/M/V: Abogados inmigración Houston                      │
│ - M/J: Med Spas Miami                                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ PASO 2: ENCONTRAR EMAILS                                    │
│                                                             │
│ Para cada empresa del CSV:                                  │
│ 1. Hunter.io Email Finder (25/mes)                         │
│ 2. Si no encuentra → Snov.io Email Finder (50 créditos)    │
│ 3. Verificar con Snov.io Email Verifier                    │
│                                                             │
│ Resultado: lista de emails verificados                      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ PASO 3: ANALIZAR WEBS                                      │
│                                                             │
│ Para cada lead con email verificado:                        │
│ Firecrawl scrapea la web → Pi analiza:                      │
│ - Servicios, precios, testimonios                          │
│ - Calidad web (1-10)                                       │
│ - Presencia en redes                                       │
│ - Idioma (ES/EN)                                           │
│                                                             │
│ Pi puntúa con rubric (0-10)                                │
│ ≥ 7 = calificado | < 7 = descartado                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ PASO 4: ESCRIBIR EMAILS                                     │
│                                                             │
│ Para cada lead calificado:                                  │
│                                                             │
│ Pi escribe email personalizado:                             │
│ - Asunto específico                                        │
│ - Menciona algo de su web/redes                            │
│ - Propuesta clara (audit gratuito)                          │
│ - Llamada a la acción                                      │
│ - Link a YouTube + web                                     │
│                                                             │
│ Guardar en Google Sheet/DB                                  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ PASO 5: REPORTE A DANIEL                                    │
│                                                             │
│ Pi envía por Telegram:                                      │
│ - Leads encontrados: N                                      │
│ - Leads calificados: N                                      │
│ - Emails creados: N                                         │
│ - Preview de cada email                                     │
│                                                             │
│ Daniel revisa (15 min)                                      │
│ Aprueba todos o indica correcciones                         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ PASO 6: ENVÍO                                               │
│                                                             │
│ Daniel envía emails aprobados desde Gmail                   │
│ Máximo 20-30/día                                            │
│                                                             │
│ Pi registra: fecha envío, secuencia                         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ DÍA 3 Y DÍA 7: SEGUIMIENTO                                  │
│                                                             │
│ Pi prepara emails de seguimiento                            │
│ Daniel revisa y envía                                       │
│                                                             │
│ Sin respuesta después de 3 intentos → cerrado               │
└─────────────────────────────────────────────────────────────┘
```

---

## Configuración necesaria (hacer esta semana)

### 1. Crear cuenta Snov.io (gratis)
- Ir a snov.io
- Plan free: 50 créditos/mes + 100 destinatarios
- Guardar API key en `/opt/data/.env` como `SNOV_API_KEY`
- Instalar extensión de Chrome para buscar emails desde LinkedIn

### 2. Crear cuenta Outscraper (gratis)
- Ir a outscraper.com
- Plan free: 500 registros/mes
- Usar Google Maps Scraper para buscar negocios
- Exportar a CSV

### 3. Verificar email de contacto
- hola@danimarzan.com debe existir y funcionar
- Configurar en Gmail con firma profesional
- Probar envío de 5 emails de prueba

### 4. Crear Google Sheet de prospects
Columnas:
| empresa | web | email | telefono | rating | reseñas | nicho | fecha_encontrado | puntuacion | estado | email_creado | fecha_envio | respuesta |
|---------|-----|-------|----------|--------|---------|-------|-----------------|------------|--------|-------------|-------------|-----------|

Estados: encontrado → calificado → email_creado → aprobado → enviado → seguimiento_1 → seguimiento_2 → respondido / cerrado

### 5. Verificar créditos Hunter.io
- Ya tienes cuenta (HUNTER_API en .env)
- Plan free: 25 búsquedas/mes
- Usar con moderación en leads de mayor calidad

---

## Implementación del cron job

El cron job diario ejecutará un script de Python que:

1. Lee el nicho del día (alternando Houston/Miami)
2. Busca empresas en Google Maps (via Outscraper API o Firecrawl)
3. Encuentra emails (Hunter.io + Snov.io API)
4. Analiza webs (Firecrawl + Pi)
5. Puntúa con rubric
6. Genera emails personalizados (Pi)
7. Guarda todo en Google Sheet/SQLite
8. Envía reporte a Daniel por Telegram

**Frecuencia:** Diaria, 9:00 AM (hora Georgia)

**Tiempo estimado de ejecución:** 30-60 minutos automáticos

**Intervención humana:** 15 minutos de revisión + envío de emails
