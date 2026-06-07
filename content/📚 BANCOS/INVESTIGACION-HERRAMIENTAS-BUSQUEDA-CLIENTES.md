---
title: "🔍 INVESTIGACIÓN: HERRAMIENTAS Y CAPACIDADES PARA BÚSQUEDA DE CLIENTES"
---

# 🔍 INVESTIGACIÓN: HERRAMIENTAS Y CAPACIDADES PARA BÚSQUEDA DE CLIENTES

> **Fecha:** 2026-06-02
> **Objetivo:** Mapear exactamente qué puede hacer Zor (IA) vs qué debe hacer Daniel (humano)
> **Estado:** Investigación completa

---

## PARTE 1: LO QUE YO PUEDO HACER (Zor/IA)

### ✅ CAPACIDAD 1: Buscar empresas con Firecrawl (TENGO ACCESO)

**Herramienta:** Firecrawl (ya está disponible en mis herramientas)

**Qué puedo hacer:**
- `firecrawl_search` — Buscar en Google "restaurants in Batumi Georgia" y obtener URLs, nombres, datos
- `firecrawl_scrape` — Entrar a la web de cada empresa y extraer: email, teléfono, redes sociales, descripción
- `firecrawl_map` — Mapear un sitio web completo para encontrar todas las páginas de contacto
- `firecrawl_extract` — Extraer datos estructurados de webs (emails, teléfonos, horarios)

**Limitaciones:**
- Firecrawl NO accede directamente a Google Maps (necesita una API separada)
- Firecrawl NO encuentra emails que no estén en la web
- Firecrawl NO verifica si un email es válido
- Firecrawl NO envía emails

**Coste para ti:** $0 (ya está incluido en mis herramientas)

### ✅ CAPACIDAD 2: Buscar en Google con Firecrawl Search

**Qué puedo hacer:**
- Buscar "restaurants in Batumi Georgia site:instagram.com" → Encuentra cuentas de Instagram
- Buscar "hotels in Batumi Georgia contact email" → Encuentra páginas de contacto
- Buscar "best gyms in Tbilisi Georgia" → Encuentra listados con datos
- Buscar "empresas de [sector] en [ciudad] LinkedIn" → Encuentra perfiles de LinkedIn

**Esto es GRATIS y lo puedo hacer AHORA MISMO**

### ✅ CAPACIDAD 3: Analizar webs de empresas

**Qué puedo hacer:**
- Entrar a la web de una empresa y analizar:
  - ¿Tiene blog? ¿Cuándo fue la última publicación?
  - ¿Tiene sección de testimonios?
  - ¿Tiene formulario de contacto?
  - ¿Qué tan profesional es su web?
  - ¿Tiene enlaces a redes sociales?
- Entrar a su Instagram/Facebook (si es público) y analizar:
  - ¿Cuándo fue la última publicación?
  - ¿Cuántos seguidores tiene?
  - ¿Responden comentarios?
  - ¿Qué calidad tienen las fotos?

### ✅ CAPACIDAD 4: Crear mensajes personalizados

**Qué puedo hacer:**
- Dado el nombre de una empresa + su web + sus redes → Crear un email personalizado
- Adaptar el tono según el tipo de negocio
- Incluir datos específicos de su negocio en el mensaje
- Crear variantes A/B para testing

### ✅ CAPACIDAD 5: Organizar datos en Google Sheets

**Qué puedo hacer:**
- Crear y mantener una hoja de cálculo con:
  - Nombre de la empresa
  - Email
  - Teléfono
  - Web
  - Instagram
  - Última publicación
  - Prioridad (🔴🟡🟢)
  - Estado del outreach
  - Notas

### ❌ LO QUE NO PUEDO HACER (limitaciones reales)

1. **No puedo enviar emails** — No tengo acceso a tu cuenta de Gmail
2. **No puedo acceder a Google Maps directamente** — Necesitarías darme acceso a una API o usar Outscraper tú
3. **No puedo verificar emails** — Necesitaría Hunter.io API o similar
4. **No puedo acceder a LinkedIn** — LinkedIn bloquea scraping
5. **No puedo hacer llamadas telefónicas**
6. **No puedo firmar contratos ni cobrar**

---

## PARTE 2: HERRAMIENTAS QUE NECITAS CREAR CUENTA (GRATIS)

### Herramienta 1: Outscraper (outscraper.com)
- **Para qué:** Scrapear Google Maps → Obtener nombre, teléfono, web, email de negocios
- **Gratis:** 500 registros/mes
- **Tú creas la cuenta** → Me das acceso o tú exportas el CSV y me lo pasas
- **Yo puedo:** Analizar el CSV, filtrar, crear mensajes

### Herramienta 2: Hunter.io (hunter.io)
- **Para qué:** Encontrar emails profesionales por dominio
- **Gratis:** 25 búsquedas/mes
- **API:** Sí, tiene API que YO puedo usar si me das el API key
- **Yo puedo:** Llamar a la API de Hunter para encontrar emails automáticamente

### Herramienta 3: Apollo.io (apollo.io)
- **Para qué:** Base de datos de empresas + emails + filtros avanzados
- **Gratis:** 10.000 créditos/mes
- **API:** Sí, tiene API
- **Yo puedo:** Llamar a la API de Apollo para buscar empresas por criterios

### Herramienta 4: Google Places API (opcional, de pago)
- **Para qué:** Acceso oficial a datos de Google Maps
- **Gratis:** $200 crédito/mes (gratis si no lo gastas)
- **Coste real:** ~$5-10 por cada 1000 búsquedas
- **Yo puedo:** Llamar a la API si me das las credenciales

---

## PARTE 3: EL SISTEMA IDEAL — CÓMO TRABAJAR JUNTOS

### FLUJO DE TRABAJO:

```
PASO 1: Tú me das criterios
    ↓
PASO 2: Yo busco empresas con Firecrawl Search + Scrape
    ↓
PASO 3: Yo analizo cada empresa (web, redes, calidad)
    ↓
PASO 4: Yo filtro por prioridad (🔴🟡🟢)
    ↓
PASO 5: Yo creo mensajes personalizados
    ↓
PASO 6: Tú revisas y envías (o automatizas con Make/Zapier)
    ↓
PASO 7: Yo hago seguimiento y ajusto
```

### LO QUE TÚ ME TIENES QUE DAR:

1. **Criterios de filtrado:**
   - ¿Qué tipo de negocios? (restaurantes, gimnasios, clínicas, hoteles...)
   - ¿Qué zonas geográficas? (Batumi, Tbilisi, La Palma, España remoto...)
   - ¿Qué tamaño de empresa? (1-10 empleados, 10-50...)
   - ¿Qué presupuesto estimado tienen?
   - ¿Qué problemas específicos deben tener? (redes abandonadas, web mala...)

2. **Acceso a herramientas (opcional pero recomendado):**
   - API key de Hunter.io (para que yo busque emails automáticamente)
   - API key de Apollo.io (para que yo busque empresas por criterios)
   - Cuenta de Outscraper (para que tú exportes CSVs de Google Maps)

3. **Tu "pitch" base:**
   - ¿Qué servicios ofreces exactamente?
   - ¿Qué precios?
   - ¿Qué te hace diferente de otros gestores de redes?

---

## PARTE 4: PACK DE SERVICIOS — LO QUE DANIEL PUEDE VENDER

### Basado en lo que me has contado, esto es lo que podrías ofrecer:

**PACK "TEREGO" — Presencia Digital Completa (1000€/mes)**

| Servicio | Detalle |
|---|---|
| **Web** | Revisión/optimización de web existente (no creación desde 0) |
| **Vídeo** | 4 vídeos/mes (Reels/Shorts/TikTok) |
| **Redes sociales** | 12 posts/mes + stories diarias |
| **Plan de contenido** | Calendario mensual + estrategia |
| **Informe** | Métricas mensuales + recomendaciones |
| **Comunidad** | Respuesta a comentarios y mensajes |

**PACK "CRECIMIENTO" — Redes Sociales (600€/mes)**

| Servicio | Detalle |
|---|---|
| **Vídeo** | 4 vídeos/mes (Reels/Shorts) |
| **Redes sociales** | 12 posts/mes + stories |
| **Plan de contenido** | Calendario mensual |
| **Informe** | Métricas mensuales |

**PACK "BÁSICO" — Gestión de Redes (300€/mes)**

| Servicio | Detalle |
|---|---|
| **Redes sociales** | 8 posts/mes + stories |
| **Comunidad** | Respuesta a comentarios |
| **Plan de contenido** | Calendario básico |

**SERVICIOS ADICIONALES (extra):**
- Creación de web desde 0: 500-1500€ (una vez)
- Campaña de publicidad (Facebook/Instagram Ads): 200€/mes + presupuesto ads
- Fotografía profesional: 150€/sesión
- Branding (logo, colores, identidad): 300€ (una vez)

---

## PARTE 5: PRÓXIMOS PASOS

### INMEDIATO (esta semana):

1. **Tú:** Dime los criterios exactos de empresas que buscamos
2. **Yo:** Empiezo a buscar con Firecrawl Search + Scrape
3. **Tú:** Crea cuenta en Hunter.io (gratis) y me das el API key
4. **Yo:** Configuro la búsqueda automática de emails

### CORTO PLAZO (2 semanas):

1. **Yo:** Te entrego una lista de 50-100 empresas filtradas con datos completos
2. **Yo:** Te creo los mensajes personalizados para cada una
3. **Tú:** Revisas, ajustas y envías
4. **Yo:** Hago seguimiento y ajusto el proceso

### MEDIO PLAZO (1 mes):

1. **Tú:** Cierras 1-3 clientes
2. **Yo:** Documento el proceso como caso de éxito
3. **Tú:** Usas el caso de éxito para vender más
4. **Yo:** Escalo la búsqueda a más zonas/categorías

---

## RESUMEN: ¿QUÉ PUEDO HACER YO?

| Tarea | ¿Puedo hacerlo? | Herramienta |
|---|---|---|
| Buscar empresas en Google | ✅ SÍ | Firecrawl Search |
| Analizar webs de empresas | ✅ SÍ | Firecrawl Scrape |
| Extraer emails de webs | ✅ SÍ | Firecrawl Extract |
| Analizar Instagram/Facebook | ✅ SÍ | Firecrawl Scrape |
| Crear mensajes personalizados | ✅ SÍ | Mi capacidad de redacción |
| Organizar datos en Sheets | ✅ SÍ | Google Sheets |
| Encontrar emails por dominio | ⚠️ NECESITO API key | Hunter.io API |
| Buscar en Google Maps | ⚠️ NECESITO API o CSV | Google Places API / Outscraper |
| Enviar emails | ❌ NO | Necesitas tú o herramienta de email |
| Verificar emails | ⚠️ NECESITO API key | Hunter.io API |
| Acceder a LinkedIn | ❌ NO | LinkedIn bloquea scraping |
| Hacer llamadas | ❌ NO | Necesitas tú |

---

*Investigación completada por Zor — 2026-06-02*
*Siguiente paso: Daniel define criterios → Zor empieza a buscar*
