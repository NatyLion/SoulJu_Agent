from pathlib import Path
from scripts.llm_client import run_llm 

def run_agent(agent_file: str, task: str, output_file: str) -> str:
    agent_path = Path(agent_file)

    if not agent_path.exists():
        raise FileNotFoundError(f"Agent file não encontrado: {agent_file}")

    agent = agent_path.read_text(encoding="utf-8")

    prompt = f"""
{agent}

TAREFA:
{task}
"""

    result = run_llm(prompt)

    if not result or not result.strip():
        raise RuntimeError("Resposta vazia do modelo")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(result, encoding="utf-8")

    return result
