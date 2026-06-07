---
title: ⚡ Briefing Operativo — Thor (Hermes)
---

# ⚡ Briefing Operativo — Thor (Hermes)
## Prospección Automatizada para Dani Marzán

**Dirige:** Claude (Cowork) · **Ejecuta:** Thor · **Decide y envía:** Dani
**Fecha:** 2026-06-03
**Manda sobre el Playbook** en todo lo operativo. El Playbook es referencia; esto es el flujo real.

---

## 0. Diagnóstico — Las 3 cosas que deciden si funciona

1. **Entregabilidad** — Si el correo cae en spam, da igual lo bueno que sea → P0: dominio dedicado + warm-up
2. **Activos de venta** — El email lleva a una web; si no hay portfolio + Reels, no cierra → P1
3. **Calidad del filtro, no volumen** — 15 empresas perfectas > 60 mediocres → Validar scoring SIN gastar créditos

**Regla de oro:** No escalamos nada hasta que la primera tanda de 15-20 contactos dé señal. Mejor 1 ciclo medido que 4 a ciegas.

---

## 1. Orden de prioridades (NO saltarse)

| Prioridad | Quién | Acción | Estado |
|-----------|-------|--------|--------|
| **P0** | Dani | Dominio dedicado + SPF/DKIM/DMARC + warm-up (~2 sem) | ⬜ Pendiente |
| **P1** | Dani | Portfolio web + 2-3 Reels enlazables + CV | ⬜ Pendiente |
| **P2** | Thor | Sourcing + scoring primera tanda (0 créditos) → Dani valida filtro | ⬜ Pendiente |
| **P3** | Thor | Enriquecer top validado con Hunter + preparar notas | ⬜ Pendiente |

**Mientras P0/P1 maduran**, P2 avanza. Cuando el dominio esté caliente, ya tienes la munición lista.

---

## 2. Reparto de tareas

| Paso | Quién | Herramienta | Salida |
|------|-------|-------------|--------|
| 1. Sourcing 25-50 dominios | Thor | Firecrawl search/scrape | Lista cruda |
| 2. Scoring ICP ≥7/10 | Thor | Firecrawl extract (schema) | Tabla con score |
| 3. Enriquecer top ~15-20 | Thor | Hunter (créditos) | Email + contacto + confidence |
| 4. Investigar web+redes | Thor | Firecrawl | Dolor 1 frase + gancho |
| 5. Bloque de prompt | Thor | (rellena plantilla) | Bloque listo en nota |
| 6. Redactar email final | Dani + Claude | Cowork | Asunto + cuerpo |
| 7. Revisar y enviar | Dani | Gmail dominio nuevo | Correo enviado |

**Thor NUNCA envía correos ni redacta texto final.** Entrega termina en paso 5.

---

## 3. Firecrawl — Directrices concretas

### Sourcing
- Consultas por nicho + señal de presupuesto
- Ej.: "latino owned skincare brand" site:instagram.com
- Priorizar dominios con anuncios activos en Meta Ad Library

### Scoring con extracción estructurada
Schema JSON para cada dominio:
```json
{
  "empresa": "string",
  "sector": "string",
  "idioma_web": "ES|EN|otro",
  "tiene_video_propio": "boolean",
  "calidad_web": "alta|media|baja",
  "menciona_equipo_marketing": "boolean",
  "señal_de_dolor": "string (1 frase)"
}
```

### Redes
- Scrape perfil público IG/TikTok: seguidores, fecha último post, si usan Reels
- Si Firecrawl no entra: usa la web y marca "redes: no verificable"

### Contacto
- Map del dominio para /about, /team, /contact ANTES de gastar Hunter
- A veces el email del fundador está publicado → te ahorras el crédito

### Reglas de créditos
- Nunca Hunter en score <7
- Nunca verificar confidence <80%

---

## 4. Formato de salida — Nota Obsidian por empresa

**Ubicación:** `/Prospectos/NOMBRE-EMPRESA.md`

```markdown
---
empresa: "Nombre SA"
web: "https://..."
sector: "e-commerce skincare"
tamaño: "12 empleados"
score: 8
idioma: "EN"
contacto_nombre: "Jane Doe"
contacto_cargo: "Founder"
email: "jane@marca.com"
confidence: 92
estado: "pendiente-revision"
fecha: 2026-06-08
---

## Dolor detectado
IG con 14K seguidores, sin publicar un Reel desde marzo.

## Gancho personal
Lanzaron sérum nuevo la semana pasada (post del 1 jun).

## Investigación
- Web: WordPress antiguo, sin vídeo. Oportunidad de upsell web.
- Redes: IG 14K / TikTok inexistente. Posteo <1/semana.
- Anuncios activos en Meta Ad Library: sí (3 creativos estáticos).

## Bloque de prompt enriquecido
[Este bloque lo rellena Thor con la plantilla del Playbook §4]
```

### Panel automático (nota Pipeline.md con Dataview)
```dataview
TABLE score, contacto_cargo, confidence, estado
FROM "Prospectos"
WHERE score >= 7
SORT score DESC
```

### Estados
`pendiente-revision` → `listo-enviar` → `enviado` → `respondio` → `llamada` → `cliente`

---

## 5. Infraestructura de email (P0 — Dani)

1. **Domicilio dedicado** (NO tu dominio principal). Ej.: danimarzan.pro o dani-studio.com
2. **Hostinger:** crear buzón + configurar SPF/DKIM/DMARC
3. **Warm-up (~2 sem):** empezar con 5-10 correos/día a contactos reales, subir volumen gradual
4. **Firma:** enlace al CV + portfolio, nunca adjunto

---

## 6. Ciclo semanal

| Día | Quién | Acción |
|-----|-------|--------|
| Semana 0 | Dani | Dominio + warm-up + portfolio |
| Lunes | Thor | 25-50 dominios + scoring (0 créditos) |
| Lunes pm | Dani | Revisar scoring, ajustar criterios |
| Martes | Thor | Enriquecer top validado con Hunter |
| Miércoles | Thor | Investigar + bloque de prompt |
| Jueves | Dani+Claude | Generar emails + enviar primera tanda |
| Viernes | Dani | Follow-up |

---

## 7. Directiva para pegar a Thor

```
ROL: Eres mi agente de prospección. Diriges tu trabajo según el Briefing.
Entregas notas de Obsidian listas; Dani redacta email final con Claude y envía.
TÚ NUNCA ENVÍAS CORREOS NI REDACTAS EL TEXTO FINAL.

STACK: Firecrawl (sourcing+investigación), Hunter (emails), Obsidian vía GitHub (registro).
No uses 'All Alpha' para texto final.

NICHO: marcas DTC/e-commerce de EE.UU. del mercado hispano ($1M–$20M).
Secundario (máx 20%): SaaS con funding que necesite vídeo.

PROCESO:
1. SOURCING (0 créditos): Firecrawl search → 25-50 dominios. Prioriza anuncios activos.
2. SCORING (0 créditos): Firecrawl extract con schema ICP. Descarta <7/10.
3. PARA antes de gastar créditos: deja lista puntuada para que Dani valide el filtro.
   NO sigas hasta su OK la primera vez.
4. ENRIQUECE (créditos) solo el top validado: map del dominio primero (email gratis
   si está publicado), luego Hunter. Solo confidence >80%, rol fundador/marketing.
5. INVESTIGA (0 créditos): web + redes. Dolor en 1 frase + gancho personal.
6. ENTREGA: una nota markdown por empresa en /Prospectos/ con frontmatter YAML
   completo, estado "pendiente-revision", y el bloque de prompt enriquecido relleno.
7. REPORTA: nº dominios, nº que pasaron filtro, nº con email válido, créditos gastados.

REGLAS:
- Calidad sobre volumen. Nicho estrecho.
- Nunca Hunter en score <7. Nunca verificar confidence <80%.
- Cada nota debe tener un gancho específico de ESA empresa.
- Primera tanda: máximo 15-20 contactos. Validamos antes de escalar.
```

---

## 8. Próximo paso inmediato

**Thor ejecuta:** 25-30 dominios desde Meta Ad Library + scoring (0 créditos).
**Entrega:** Notas en `/Prospectos/` con frontmatter.
**Dani valida** el filtro antes de que Thor gaste un solo crédito de Hunter.

**Dani paralelo:** Arrancar dominio de envío (§5). Es lo único que bloquea resultados.

---

## 🔗 Conexiones
- [[Playbook de Prospección Automatizada]]
- [[Pipeline de Prospección]]
- [[ESTRATEGIA_CREDITOS]]
