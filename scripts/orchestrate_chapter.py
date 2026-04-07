from pathlib import Path
import re
from run_agent import run_agent
from llm_client import run_llm

THRESHOLD = 8

def extract_scores(text):
    def find(label):
        m = re.search(label + r".*?([0-9]+(?:\.[0-9])?)\/10", text, re.IGNORECASE)
        return float(m.group(1)) if m else 0

    return {
        "cientifica": find("NOTA CIENT"),
        "regulatoria": find("NOTA REGULAT"),
        "clinica": find("NOTA CL"),
        "editorial": find("NOTA EDITORIAL"),
    }

def approved(scores):
    return all(v >= THRESHOLD for v in scores.values())

def main(cap_num):
    cap = f"output/cap{cap_num}_bioquimica.md"
    review = f"output/review_cap{cap_num}.md"

    # LOOP QA
    for i in range(3):
        print(f"🔍 QA ROUND {i+1}")

        review_text = run_agent(
            "agents/qa_review.md",
            f"Leia {cap} e revise conforme instruções.",
            review
        )

        scores = extract_scores(review_text)
        print("Notas:", scores)

        if approved(scores):
            print("✅ Aprovado")
            break

        # rewrite
        chapter_text = Path(cap).read_text()

        rewrite_prompt = f"""
Reescreva o capítulo corrigindo TODOS os problemas da review.

CAPÍTULO:
{chapter_text}

REVIEW:
{review_text}
"""

        new_version = run_llm(rewrite_prompt)
        Path(cap).write_text(new_version)

    # pós aprovação
    run_agent("agents/feminine_voice.md", f"Leia {cap}", f"output/feminine_voice_cap{cap_num}.md")
    run_agent("agents/commercial_brand.md", f"Leia {cap}", f"output/commercial_review_cap{cap_num}.md")
    run_agent("agents/strategic_visionary.md", f"Leia {cap}", f"output/strategic_review_cap{cap_num}.md")

    run_agent(
        "agents/compliance_filter.md",
        f"Leia output/feminine_voice_cap{cap_num}.md e output/commercial_review_cap{cap_num}.md",
        f"output/compliance_filter_cap{cap_num}.md"
    )

    print("🚀 Pipeline completo")

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
