import json
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


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
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY não encontrada no ambiente ou no .env")
    return api_key


def extract_output_text(response_json: dict) -> str:
    text_parts: list[str] = []

    for item in response_json.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                text_parts.append(content.get("text", ""))

    if text_parts:
        return "\n".join(part for part in text_parts if part)

    if "output_text" in response_json and isinstance(response_json["output_text"], str):
        return response_json["output_text"]

    return ""


def run_llm(prompt: str, model: str = "gpt-4.1-mini") -> str:
    api_key = get_api_key()

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
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"Erro HTTP na OpenAI API: {exc.code} - {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Erro de rede ao chamar OpenAI API: {exc}") from exc

    text = extract_output_text(data)
    if not text.strip():
        raise RuntimeError("Resposta sem texto útil da API.")

    return text
