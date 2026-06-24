#!/usr/bin/env python3
"""SoulJu Playbook Generator — Runner usando OpenAI Responses API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output"
CONTEXT_FILE = ROOT / "context.md"

AGENTS = {
    1: "cap01_manifesto",
    2: "cap02_framework",
    3: "cap03_jornada",
    4: "cap04_datascience",
    5: "cap05_personas",
    6: "cap06_formulacoes",
    7: "cap07_bioquimica",
    8: "cap08_protocolos",
    9: "cap09_anvisa",
    10: "cap10_benchmark",
    11: "cap11_financeiro",
    12: "cap12_referencias",
}


def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def get_api_key() -> str:
    load_dotenv(ROOT / ".env")
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        print("❌ OPENAI_API_KEY não encontrada.")
        print("   Opção 1: export OPENAI_API_KEY='sua_chave'")
        print("   Opção 2: criar arquivo .env com OPENAI_API_KEY=sua_chave")
        sys.exit(1)
    return key


def extract_output_text(response_json: dict) -> str:
    # Compatível com formato de Responses API
    text_parts: list[str] = []
    for item in response_json.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                text_parts.append(content.get("text", ""))
    if text_parts:
        return "\n".join(part for part in text_parts if part)

    # Fallbacks defensivos
    if "output_text" in response_json and isinstance(response_json["output_text"], str):
        return response_json["output_text"]

    return ""


def call_openai(prompt: str, api_key: str, model: str) -> str:
    payload = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    }
                ],
            }
        ],
    }

    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"❌ Erro HTTP na OpenAI API: {e.code}")
        print(body)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ Erro de rede ao chamar OpenAI API: {e}")
        sys.exit(1)

    text = extract_output_text(data)
    if not text.strip():
        print("❌ Resposta sem texto útil da API.")
        print(json.dumps(data, ensure_ascii=False, indent=2)[:2000])
        sys.exit(1)
    return text


def generate_chapter(chapter_num: int, api_key: str, model: str) -> None:
    agent = AGENTS[chapter_num]
    input_file = ROOT / "agents" / f"{agent}.md"
    output_file = OUTPUT_DIR / f"{agent}.md"

    if not input_file.exists():
        print(f"❌ Agente não encontrado: {input_file}")
        sys.exit(1)
    if not CONTEXT_FILE.exists():
        print(f"❌ Arquivo de contexto não encontrado: {CONTEXT_FILE}")
        sys.exit(1)

    print(f"🤖 Gerando Capítulo {chapter_num}: {agent}")
    prompt = (
        f"{CONTEXT_FILE.read_text(encoding='utf-8')}\n\n---\n\n"
        f"{input_file.read_text(encoding='utf-8')}"
    )

    result = call_openai(prompt, api_key=api_key, model=model)
    output_file.write_text(result, encoding="utf-8")
    print(f"✅ Salvo em: {output_file}")


def show_status() -> None:
    print("\n📊 Status dos capítulos:\n")
    for i in range(1, 13):
        agent = AGENTS[i]
        outfile = OUTPUT_DIR / f"{agent}.md"
        if outfile.exists():
            content = outfile.read_text(encoding="utf-8", errors="ignore")
            words = len(content.split())
            print(f"✅ Cap {i} — {agent} ({words} palavras)")
        else:
            print(f"⏳ Cap {i} — {agent} (pendente)")


def compile_all() -> None:
    compiled = OUTPUT_DIR / "SOULJU_PLAYBOOK_TECNICO_COMPLETO.md"
    lines = [
        "# SoulJu — Playbook Técnico",
        "",
        "## A Bíblia Científica da Plataforma Metabólica Feminina",
        "",
        f"*Compilado em: {datetime.utcnow().strftime('%d/%m/%Y %H:%M UTC')}*",
        "",
        "---",
        "",
    ]
    total_words = 0

    for i in range(1, 13):
        agent = AGENTS[i]
        outfile = OUTPUT_DIR / f"{agent}.md"
        if not outfile.exists():
            print(f"⏳ Cap {i} pendente: {outfile.name}")
            continue
        text = outfile.read_text(encoding="utf-8", errors="ignore")
        lines.append(text)
        lines.append("\n---\n")
        total_words += len(text.split())
        print(f"✅ Cap {i} incluído")

    compiled.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📄 Compilado em: {compiled}")
    print(f"📊 Total de palavras: {total_words}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Runner OpenAI para os agentes SoulJu")
    parser.add_argument(
        "targets",
        nargs="*",
        help="Use: all | status | compile | lista de capítulos (1-12)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"),
        help="Modelo da OpenAI (default: OPENAI_MODEL ou gpt-4.1-mini)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not args.targets:
        print("Uso:")
        print("  python run_openai.py all")
        print("  python run_openai.py status")
        print("  python run_openai.py compile")
        print("  python run_openai.py 2")
        print("  python run_openai.py 1 2 3")
        return

    first = args.targets[0].lower()
    if first == "status":
        show_status()
        return
    if first == "compile":
        compile_all()
        return

    api_key = get_api_key()
    model = args.model

    if first == "all":
        for i in range(1, 13):
            generate_chapter(i, api_key=api_key, model=model)
        compile_all()
        return

    for target in args.targets:
        if not target.isdigit() or int(target) not in AGENTS:
            print(f"❌ Capítulo inválido: {target}. Use 1-12, all, status ou compile.")
            sys.exit(1)
        generate_chapter(int(target), api_key=api_key, model=model)


if __name__ == "__main__":
    main()
