#!/usr/bin/env python3
"""
wikidata-connections.py — Descubrimiento de conexiones filosóficas para el vault de Daniel Marzán

Uso:
  python3 wikidata-connections.py --mode influences --of Q38193 --exclude Q9358
  python3 wikidata-connections.py --mode school --movement Q155659
  python3 wikidata-connections.py --mode common-influences --philosophers Q34981 Q9358 Q21477
  python3 wikidata-connections.py --mode broad --limit 50
  python3 wikidata-connections.py --mode check-spanish --name "Philipp Mainländer"

Autor: HermesAgent
Fuente: Wikidata SPARQL (https://www.wikidata.org)
"""

import json
import sys
import argparse
import urllib.request
import urllib.parse
import urllib.error

WIKIDATA_SPARQL = "https://query.wikidata.org/sparql"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "HermesAgent/1.0 (research project; daniel-marzan-vault)"
}

# ── Entities ──────────────────────────────────────────────────────────────────

EXCLUDE_OBVIOUS = [
    "wd:Q34981",   # Camus
    "wd:Q9358",    # Nietzsche
    "wd:Q21477",   # Kierkegaard
    "wd:Q39815",   # Séneca
    "wd:Q25497",   # Viktor Frankl
    "wd:Q25498",   # Erich Fromm
    "wd:Q9086",    # Sartre
    "wd:Q9230",    # Hegel
    "wd:Q7312",    # Kant
    "wd:Q38193",   # Schopenhauer
]

SCHOOLS = {
    "stoicism": "wd:Q155659",
    "existentialism": "wd:Q2185657",
    "nihilism": "wd:Q158027",
    "absurdism": "wd:Q158025",
    "phenomenology": "wd:Q177567",
    "critical_theory": "wd:Q178625",
    "poststructuralism": "wd:Q189070",
    "marxism": "wd:Q178625",
    "anarchism": "wd:Q183478",
    "utilitarianism": "wd:Q189069",
    "hedonism": "wd:Q189071",
    "cynicism": "wd:Q189072",
    "epicureanism": "wd:Q189073",
}

# ── Core function ─────────────────────────────────────────────────────────────

def query_sparql(sparql: str) -> list[dict]:
    url = WIKIDATA_SPARQL + "?query=" + urllib.parse.quote(sparql)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            return data["results"]["bindings"]
    except urllib.error.HTTPError as e:
        print(f"[ERROR] HTTP {e.code}: {e.reason}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return []

# ── Modes ─────────────────────────────────────────────────────────────────────

def mode_influences(of_qcode: str, exclude_qcodes: list[str] = None, limit: int = 50):
    """Filósofos influidos por X, excluyendo los obvios."""
    excludes = EXCLUDE_OBVIOUS.copy()
    if of_qcode:
        excludes.append(f"wd:{of_qcode}")
    if exclude_qcodes:
        for q in exclude_qcodes:
            excludes.append(f"wd:{q}")

    filter_clauses = "\n  ".join(f"FILTER (?philosopher != {ex})" for ex in excludes)

    query = f"""
SELECT DISTINCT ?philosopher ?philosopherLabel ?philosopherDescription WHERE {{
  ?philosopher wdt:P737 wd:{of_qcode} .
  {filter_clauses}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es,en" }}
}}
ORDER BY ?philosopherLabel
LIMIT {limit}
"""
    return query_sparql(query)


def mode_school(movement_qcode: str, limit: int = 50):
    """Filósofos de un movimiento/escuela específico."""
    filter_clauses = "\n  ".join(f"FILTER (?philosopher != {ex})" for ex in EXCLUDE_OBVIOUS)

    query = f"""
SELECT DISTINCT ?philosopher ?philosopherLabel ?philosopherDescription WHERE {{
  ?philosopher wdt:P106 wd:Q4964182 .
  ?philosopher wdt:P135 wd:{movement_qcode} .
  {filter_clauses}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es,en" }}
}}
ORDER BY ?philosopherLabel
LIMIT {limit}
"""
    return query_sparql(query)


def mode_common_influences(philosopher_qcodes: list[str], limit: int = 30):
    """Influencias compartidas entre varios filósofos."""
    values = " ".join(f"wd:{q}" for q in philosopher_qcodes)

    query = f"""
SELECT DISTINCT ?influencer ?influencerLabel (COUNT(?philosopher) AS ?count) WHERE {{
  ?philosopher wdt:P106 wd:Q4964182 .
  ?philosopher wdt:P737 ?influencer .
  VALUES ?philosopher {{ {values} }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es,en" }}
}}
GROUP BY ?influencer ?influencerLabel
ORDER BY DESC(?count)
LIMIT {limit}
"""
    return query_sparql(query)


def mode_broad(limit: int = 50):
    """Filósofos con influencias documentadas (amplio, para descubrimiento)."""
    filter_clauses = "\n  ".join(f"FILTER (?philosopher != {ex})" for ex in EXCLUDE_OBVIOUS)

    query = f"""
SELECT DISTINCT ?philosopher ?philosopherLabel ?philosopherDescription ?influencerLabel WHERE {{
  ?philosopher wdt:P106 wd:Q4964182 .
  ?philosopher wdt:P737 ?influencer .
  {filter_clauses}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es,en" }}
}}
ORDER BY ?philosopherLabel
LIMIT {limit}
"""
    return query_sparql(query)


def check_spanish_wikipedia(name: str) -> bool:
    """Verifica si existe Wikipedia en español para un autor."""
    url = f"https://es.wikipedia.org/wiki/{urllib.parse.quote(name.replace(' ', '_'))}"
    req = urllib.request.Request(url, headers={"User-Agent": "HermesAgent/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except urllib.error.HTTPError:
        return False
    except:
        return False


# ── Output formatting ─────────────────────────────────────────────────────────

def print_results(results: list[dict], show_es_wiki: bool = False):
    if not results:
        print("  (sin resultados)")
        return
    for r in results:
        name = r.get("philosopherLabel", r.get("influencerLabel", {})).get("value", "?")
        desc = r.get("philosopherDescription", {}).get("value", "")
        count = r.get("count", {}).get("value", "")
        influencer = r.get("influencerLabel", {}).get("value", "")

        suffix = ""
        if count:
            suffix = f" [influencia compartida: {count} filósofos]"
        if influencer:
            suffix = f" ← influido por: {influencer}"
        if show_es_wiki:
            has_es = check_spanish_wikipedia(name)
            suffix += f"  {'✅ ES wiki' if has_es else '❌ sin ES wiki'}"

        print(f"• {name} — {desc}{suffix}")


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wikidata Philosopher Connections")
    parser.add_argument("--mode", required=True,
                        choices=["influences", "school", "common-influences", "broad", "check-spanish"],
                        help="Modo de consulta")
    parser.add_argument("--of", dest="of_qcode", help="Q-code del filósofo/origen (modo influences)")
    parser.add_argument("--exclude", nargs="*", default=[], help="Q-codes a excluir")
    parser.add_argument("--movement", help="Q-code del movimiento (modo school) o nombre clave (stoicism, existentialism...)")
    parser.add_argument("--philosophers", nargs="+", help="Q-codes (modo common-influences)")
    parser.add_argument("--name", help="Nombre para check-spanish")
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--check-es-wiki", action="store_true", help="Verificar Wikipedia en español")

    args = parser.parse_args()

    if args.mode == "influences":
        if not args.of_qcode:
            print("[ERROR] --of QCODE requerido", file=sys.stderr)
            sys.exit(1)
        print(f"=== Filósofos influidos por {args.of_qcode} (excluyendo obvios) ===")
        results = mode_influences(args.of_qcode, args.exclude, args.limit)
        print_results(results, show_es_wiki=args.check_es_wiki)

    elif args.mode == "school":
        if not args.movement:
            print("[ERROR] --movement requerido", file=sys.stderr)
            print(f"  Disponibles: {', '.join(SCHOOLS.keys())}", file=sys.stderr)
            sys.exit(1)
        qcode = SCHOOLS.get(args.movement, args.movement)
        print(f"=== Filósofos del movimiento {args.movement} ({qcode}) ===")
        results = mode_school(qcode, args.limit)
        print_results(results, show_es_wiki=args.check_es_wiki)

    elif args.mode == "common-influences":
        if not args.philosophers:
            print("[ERROR] --philosophers QCODEs requeridos", file=sys.stderr)
            sys.exit(1)
        print(f"=== Influencias compartidas entre {args.philosophers} ===")
        results = mode_common_influences(args.philosophers, args.limit)
        print_results(results, show_es_wiki=args.check_es_wiki)

    elif args.mode == "broad":
        print(f"=== Filósofos con influencias documentadas (descubrimiento amplio) ===")
        results = mode_broad(args.limit)
        print_results(results, show_es_wiki=args.check_es_wiki)

    elif args.mode == "check-spanish":
        if not args.name:
            print("[ERROR] --name requerido", file=sys.stderr)
            sys.exit(1)
        exists = check_spanish_wikipedia(args.name)
        status = "✅ Existe" if exists else "❌ No existe"
        print(f"Wikipedia ES para '{args.name}': {status}")
