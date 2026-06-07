---
title: "MEGA DOCUMENTO: Flujo de Outreach B2B — Daniel Marzán"
---

# MEGA DOCUMENTO: Flujo de Outreach B2B — Daniel Marzán

> **Versión:** 2026-06-06
> **Propósito:** Guía completa para que el agente (Pi) ejecute el flujo de outreach de principio a fin, sin intervención humana excepto el envío final del email.
> **Estado:** Listo para implementar en cron job diario

---

## PARTE 1: VISIÓN Y ESTRATEGIA

### ¿Quién soy?
- **Nombre:** Daniel Marzán
- **Edad:** 26 años
- **Ubicación:** La Palma (Canarias), viviendo en Georgia (país)
- **Timezone:** GMT+4 (ideal para USA y Europa)
- **Idiomas:** Español nativo, inglés fluido

### ¿Qué ofrezco?
| Servicio | Precio | Descripción |
|----------|--------|-------------|
| Gestión de redes sociales | 500€/mes | Instagram + TikTok, contenido, community management |
| Vídeo + Redes | 1.200€/mes | Todo lo anterior + grabación y edición de vídeo |
| Web + Redes + Vídeo | 2.000€/mes | Paquete completo: web, redes, vídeo |
| Formación online | 500€/sesión | Clases de IA, vídeo, marketing, herramientas digitales |

### Mi diferenciador
- **Pitch:** "Me encargo de que tus clientes te encuentran en Instagram"
- **Experiencia demostrable:** @SoyPorteroYT — 60K YouTube, 48K TikTok, 7M+ visitas
- **Equipo:** Black Magic 4K, DJI Mini 3 Pro, Blue Yeti
- **Software:** DaVinci Resolve, Remotion, Claude Code
- **Formación:** Docente habilitado, Máster en Profesorado (UNIR), fundador de ChatCore/Abora

### Mi cliente ideal (ICP)

#### Nicho 1: Abogados de inmigración en Houston, Texas
- **Por qué:** Houston tiene enorme población hispana, muchos necesitan abogado de inmigración
- **Perfil:** Abogados o bufetes pequeños/medianos, web mediocre o inexistente, sin presencia activa en Instagram
- **Idioma del cliente final:** Español e inglés (bilingüe)
- **Tono del email:** Profesional pero cercano, en español

#### Nicho 2: Clínicas estéticas (Med Spas) en Miami, Florida
- **Por qué:** Miami es capital de estética, mercado enorme, competencia alta = necesitan diferenciación
- **Perfil:** Clínicas pequeñas/medianas, web sin optimizar, sin contenido en redes o contenido pobre
- **Idioma del cliente final:** Español e inglés (bilingüe)
- **Tono del email:** Profesional con energía, en español o inglés según el negocio

#### Nicho 3: Empresas de servicios locales en Florida (ampliación futura)
- **Perfil:** Empresas con web mala, sin redes, reseñas negativas o sin reseñas
- **Sectores:** Restaurantes, hoteles, inmobiliarias, clínicas dentales, gimnasios

---

## PARTE 2: HERRAMIENTAS GRATUITAS DISPONIBLES

### Stack actual (todo gratis o con plan free)

| Herramienta | Uso | Plan | Límite gratis |
|-------------|-----|------|---------------|
| **Hunter.io** | Encontrar emails de empresas | Free | 25 búsquedas/mes |
| **Snov.io** | Encontrar emails + verificar + enviar | Free | 50 créditos/mes + 100 destinatarios |
| **Firecrawl** | Analizar webs de leads | Ya disponible | Ilimitado (via API key) |
| **Google Maps Scraper** (Outscraper) | Buscar negocios locales | Free tier | 500 registros/mes |
| **Google Sheets** | Base de datos de leads | Free | Ilimitado |
| **Gmail/SMTP propio** | Enviar emails | Free | 500 emails/día (Gmail) |
| **Cloud Code / Pi** | Agente IA que investiga, califica, escribe | Ya disponible | Ilimitado |

### Herramientas que NO necesitamos (por ahora)
- **Apollo.io** → Caro, no necesario si usamos Google Maps + Hunter + Snov
- **Instantly.ai** → Caro, podemos enviar con Gmail propio (500/día) o Snov.io free
- **Meta Ads** → No es outreach frío, es publicidad de pago. No aplica ahora.
- **Playwright** → Ya lo tengo integrado en Firecrawl

---

## PARTE 3: FLUJO COMPLETO PASO A PASO

### FASE 1: BÚSQUEDA DE LEADS (Diaria — 30 min)

#### Paso 1.1: Definir el nicho del día
Alternar entre:
- Lunes/Miércoles/Viernes: Abogados de inmigración en Houston
- Martes/Jueves: Med Spas en Miami
- Sábado: Revisión y limpieza de base de datos

#### Paso 1.2: Buscar empresas con Google Maps Scraper
1. Ir a Outscraper Google Maps Scraper (free tier)
2. Buscar: "immigration lawyer Houston Texas" o "med spa Miami Florida"
3. Extraer: nombre, dirección, teléfono, web, reseñas, rating
4. Exportar a CSV
5. Alternativa: buscar manualmente en Google Maps y extraer datos con Firecrawl

#### Paso 1.3: Encontrar emails con Hunter.io + Snov.io
1. Para cada empresa de la lista, buscar email con Hunter.io (25 búsquedas/mes)
2. Si Hunter no tiene, usar Snov.io Email Finder (50 créditos/mes)
3. Verificar email con Snov.io Email Verifier (incluido en créditos)
4. Priorizar emails de contacto directo (info@, hello@, nombre@)

#### Paso 1.4: Volcar a base de datos
Crear/actualizar Google Sheet o SQLite con:
- Empresa | Web | Email | Teléfono | Rating | Reseñas | Nicho | Fecha encontrado | Estado

**Estado inicial:** "encontrado"

---

### FASE 2: INVESTIGACIÓN Y CALIFICACIÓN (Diaria — 1 hora)

#### Paso 2.1: Analizar web del lead con Firecrawl
Para cada lead con email verificado:
1. Scrapear la web del negocio con Firecrawl
2. Extraer:
   - Servicios que ofrecen
   - Precios (si están visibles)
   - Testimonios/casos de éxito
   - Calidad de la web (1-10)
   - Presencia en redes (tiene Instagram? está activo?)
   - Idioma de la web (español, inglés, bilingüe)

#### Paso 2.2: Puntuar con rubric

**Rubric de calificación (máximo 10 puntos):**

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Web mediocre/inexistente | 0-3 | Web mala = 3, web regular = 2, web buena = 0 |
| Sin redes sociales activas | 0-2 | No tiene = 2, tiene pero inactiva = 1, activa = 0 |
| Reseñas negativas o sin reseñas | 0-2 | Sin reseñas = 2, negativas = 1, positivas = 0 |
| Nicho alineado | 0-3 | Abogado inmigración = 3, Med Spa = 3, otro = 0 |
| **TOTAL** | **0-10** | **≥ 7 = pasa, < 7 = descartado** |

#### Paso 2.3: Actualizar estado en base de datos
- ≥ 7 puntos → Estado: "calificado"
- < 7 puntos → Estado: "descartado" + razón

---

## PARTE 3: CREACIÓN DEL EMAIL PERSONALIZADO (Diaria — 1 hora)

### Técnicas obligatorias (método Isra Bravo)

Cada email DEBE incluir estas 9 técnicas:

1. **Tono auténtico y cercano** — Escribe como si hablaras con un amigo. Oraciones cortas, humor, preguntas retóricas, vulnerabilidad.
2. **Expectativa y urgencia** — Motiva a actuar. Límites de tiempo. Palabras como "ahora", "última oportunidad".
3. **Desmitificación del marketing tradicional** — Rompe reglas. Declaraciones audaces. Explica por qué tu enfoque es diferente.
4. **Historias personales y anécdotas** — Comparte experiencias propias. Cada historia tiene una lección. Vulnerabilidad + humor.
5. **Enfoque en el cliente ideal** — Conecta con quienes valoran tu oferta. No temas alejar a quienes no encajan.
6. **Promesas de valor claras y contundentes** — Beneficios específicos sin ambigüedades. Ejemplos o testimonios reales.
7. **Bonus o regalos** — Aumenta el valor de la oferta. Bonus útil y relevante con tiempo limitado.
8. **Estructura simple y rompedora** — Frases cortas, listas, negritas. Fácil de leer en 30 segundos.
9. **Llamadas a la acción directas y repetitivas** — CTA en puntos estratégicos. Verbos de acción. Repetir la CTA.

### Paso 3.1: Investigar al contacto
1. Buscar el nombre del dueño/abogado en la web o LinkedIn
2. Buscar su perfil de Instagram (si existe)
3. Notar algo específico: un post reciente, un logro, un evento, su foto, su historia

### Paso 3.2: Escribir el email

**Estructura del email (aplicando las 9 técnicas):**

```
Asunto: [Algo específico de su negocio]

Hola [Nombre],

[Historia personal breve — técnica 4]
"El año pasado tenía un negocio como el suyo. Buen producto, buen servicio, pero nadie lo conocía."

[Desmitificación — técnica 3]
"La mayoría de negocios creen que con tener una web ya es suficiente. No lo es."

[Promesa clara — técnica 6]
"Yo me encargo de que tus clientes te encuentran en Instagram. Contenido que atrae, vídeos que convierten."

[Enfoque en cliente ideal — técnica 5]
"Si tienes un negocio en [ciudad] y sabes que podrías llegar a más clientes pero no tienes tiempo, esto es para ti."

[Bonus — técnica 7]
"Si agendamos una llamada esta semana, te regalo un análisis gratuito de tu presencia online. Sin compromiso."

[CTA directa — técnica 9]
"¿Tienes 15 minutos esta semana? Te muestro cómo podría funcionar para tu negocio."

[Urgencia — técnica 2]
"Solo estoy tomando 3 clientes nuevos este mes."

Un saludo,
Daniel Marzán
danimarzan.com | YouTube: @SoyPortero (60K suscriptores)
```

**Reglas del email:**
- Máximo 150-200 palabras
- Sin emojis excesivos
- Sin lenguaje de venta agresivo
- Personalizado (mencionar algo específico del negocio)
- Con llamada a la acción clara y repetida
- Con link a resultados (YouTube, web)
- Tono cercano, no corporativo

### Paso 3.3: Guardar email en base de datos
- Estado: "email_creado"
- Contenido del email guardado en la fila del lead

---

### FASE 4: REVISIÓN HUMANA (Diaria — 15 min)

#### Paso 4.1: Revisar emails creados
Daniel revisa los emails creados el día anterior:
- ¿Suena natural?
- ¿Es personalizado?
- ¿El tono es correcto?
- ¿Hay errores?

#### Paso 4.2: Aprobar o corregir
- Aprobado → Estado: "aprobado"
- Necesita corrección → Estado: "revisión" + notas para el agente
- Rechazado → Estado: "rechazado" + razón

---

### FASE 5: ENVÍO (Diaria — Daniel lo hace manualmente)

#### Paso 5.1: Enviar emails aprobados
- Enviar desde Gmail personal (hola@danimarzan.com o similar)
- Máximo 20-30 emails/día (para no quemar el dominio)
- Espaciar envíos (no todos de golpe)
- Usar BCC para seguimiento

#### Paso 5.2: Registrar envío
- Estado: "enviado"
- Fecha de envío
- Número de secuencia (1 = primer contacto, 2 = seguimiento, etc.)

---

### FASE 6: SEGUIMIENTO (Día 3 y día 7 después del envío)

#### Día 3: Primer seguimiento
Si no ha respondido:
```
Asunto: Re: [Asunto original]

Hola [Nombre],

Solo quería asegurarme de que llegó mi mensaje anterior.

[Repetir la propuesta en 1 frase]

¿Tiene sentido para usted?

Saludos,
Daniel
```

#### Día 7: Segundo seguimiento
Si no ha respondido:
```
Asunto: Última vez — [Asunto original]

Hola [Nombre],

Sé que está ocupado, así que esta será mi última nota.

[Propuesta en 1 frase]

Si no es el momento, no hay problema. Le deseo mucho éxito con [nombre del negocio].

Saludos,
Daniel
```

#### Después del seguimiento:
- Si responde → Estado: "respondió" → Daniel gestiona la conversación
- Si no responde después de 3 intentos → Estado: "cerrado"

---

## PARTE 4: CRON JOB DIARIO

### Horario sugerido: 9:00 AM (hora de Georgia = GMT+4)

**Tareas del agente (Pi) cada mañana:**

1. **Buscar 10-15 nuevos leads** en el nicho del día (Google Maps + Hunter/Snov)
2. **Investigar y calificar** cada lead (Firecrawl + rubric)
3. **Crear emails personalizados** para los leads calificados (≥ 7 puntos)
4. **Generar reporte** con:
   - Leads encontrados hoy
   - Leads calificados hoy
   - Emails creados hoy
   - Leads pendientes de revisión
   - Resumen de la semana (total leads, emails enviados, respuestas)

5. **Enviar reporte a Daniel** por Telegram

### Formato del reporte diario:

```
📊 Reporte Outreach — [Fecha]

🔍 Leads encontrados hoy: [N]
✅ Leads calificados (≥7): [N]
📧 Emails creados: [N]
⏳ Pendientes de revisión: [N]

📈 Semana:
- Total leads en pipeline: [N]
- Emails enviados: [N]
- Respuestas recibidas: [N]
- Reuniones agendadas: [N]

📋 Leads para revisar hoy:
1. [Empresa] — [Email] — [Puntuación] — [Nicho]
2. [...]

¿Aprobados para enviar? Responde "todos" o indica cuáles.
```

---

## PARTE 5: GESTIÓN DE RESPUESTAS

### Si el lead responde positivo:
1. Estado: "respondido_positivo"
2. Daniel gestiona la conversación personalmente
3. Proponer: videollamada de 15 min → audit gratuito → propuesta formal

### Si el lead responde negativo:
1. Estado: "respondido_negativo"
2. Agradecer y cerrar
3. No insistir

### Si el lead no respuesta después de 3 intentos:
1. Estado: "cerrado_sin_respuesta"
2. No volver a contactar en 90 días
3. Después de 90 días, se puede reactivar con un nuevo enfoque

---

## PARTE 6: MÉTRICAS Y OBJETIVOS

### Objetivo a 3 meses:
- **4-6 clientes activos**
- **Ingreso:** 2.000-4.000€/mes

### Métricas semanales a trackear:
| Métrica | Objetivo semanal |
|---------|------------------|
| Leads encontrados | 30-50 |
| Leads calificados | 15-25 |
| Emails enviados | 15-25 |
| Tasa de respuesta | 3-5% |
| Conversaciones iniciadas | 2-3 |
| Propuestas enviadas | 1-2 |
| Clientes cerrados | 0-1 |

### Funnel esperado:
- 100 leads encontrados → 50 calificados → 25 emails enviados → 1-2 respuestas → 0-1 cliente

---

## PARTE 7: ARCHIVOS Y RECURSOS

### Archivos en el vault:
- `Proyecto-Portfolio-Web-danimarzan.md` — Estado de la web
- `Analisis-Web/Vibe-Marketing-2026-Aplicacion-Outreach.md` — Análisis del video
- `Audios-Scripts/` — Scripts de audios generados

### Base de datos:
- **Google Sheet o SQLite:** `prospects.db` en `/opt/data/home/outreach/`
- **Columnas:** empresa, web, email, telefono, rating, reseñas, nicho, fecha_encontrado, puntuacion, estado, email_enviado, fecha_envio, respuesta

### Credenciales:
- **Hunter.io:** API key en `/opt/data/.env` como `HUNTER_API` (25 búsquedas/mes free)
- **Snov.io:** Crear cuenta free en snov.io (50 créditos/mes)
- **Outscraper:** Crear cuenta free (500 registros/mes)
- **Firecrawl:** API key ya configurada
- **Gmail:** hola@danimarzan.com (verificar que exista y funcione)

---

## PARTE 8: PRÓXIMOS PASOS INMEDIATOS

### Semana 1 (esta semana):
- [ ] Crear cuenta free de Snov.io
- [ ] Crear cuenta free de Outscraper
- [ ] Verificar que hola@danimarzan.com existe y puede enviar emails
- [ ] Crear Google Sheet de prospects con las columnas definidas
- [ ] Hacer primera búsqueda manual: 10 abogados de inmigración en Houston
- [ ] Calificar los 10 con el rubric
- [ ] Crear 3-5 emails personalizados
- [ ] Que Daniel revise y apruebe
- [ ] Enviar los primeros 3-5 emails

### Semana 2:
- [ ] Automatizar la búsqueda con cron job diario
- [ ] Procesar 15-20 leads
- [ ] Enviar 10-15 emails
- [ ] Primer seguimiento a los de la semana 1

### Semana 3-4:
- [ ] Procesar 30+ leads
- [ ] Enviar 20-25 emails
- [ ] Gestionar respuestas
- [ ] Cerrar primer cliente (objetivo)

---

## NOTAS FINALES

1. **El envío siempre lo hace Daniel.** Yo todo lo demás: buscar, investigar, calificar, escribir, reportar.

2. **El tono es clave.** No somos una agencia genérica. Somos un tipo con 60K en YouTube que sabe hacer contenido y quiere ayudar. Eso es lo que vende.

3. **La personalización es lo que diferencia.** Mencionar algo específico de cada negocio. Nunca emails masivos genéricos.

4. **La paciencia paga.** El primer cliente es el más difícil. Después, los casos de éxito hacen el trabajo.

5. **Iterar rápido.** Si algo no funciona (tema del email, enfoque, nicho), cambiarlo la semana siguiente. No esperar meses.

6. **El objetivo no es enviar 100 emails.** Es enviar 20 emails buenos que generen 1-2 conversaciones reales.
