# PIPELINE COMPLETO — COPIE E COLE NO CLAUDE CODE

## SETUP
```
cd ~/Downloads/soulju-playbook-agents
mkdir -p output
claude
```

---

## PASSO 1 — CORRIGIR CAP 2 (já temos a V2, só adicionar as correções)

```
Leia context.md. Leia output/cap02_framework.md (a versão V2 com 12.326 palavras). Leia prompts/fix_cap02.md e execute TODAS as 5 correções descritas. Mantenha 100% do conteúdo técnico da V2 e apenas ADICIONE os elementos indicados. Salve como output/cap02_framework_FINAL.md
```

## QA DO CAP 2
```
Leia agents/qa_review.md. Revise output/cap02_framework_FINAL.md nas 4 dimensões (científica, regulatória, clínica, editorial). Salve em output/review_cap02.md
```

## REVISÃO ESTRATÉGICA DO CAP 2 (Jobs/Musk)
```
Leia agents/strategic_visionary.md. Aplique os 5 filtros ao output/cap02_framework_FINAL.md. Salve em output/strategic_review_cap02.md
```

## REVISÃO COMERCIAL DO CAP 2
```
Leia agents/commercial_brand.md. Gere os 3 outputs (frases de impacto, claims por produto, oportunidades comerciais) a partir de output/cap02_framework_FINAL.md. Salve em output/commercial_review_cap02.md
```

> Se o QA ou a revisão estratégica apontar correções:
```
Leia output/review_cap02.md e output/strategic_review_cap02.md. Aplique TODAS as correções no output/cap02_framework_FINAL.md. Sobrescreva o arquivo.
```

---

## PASSO 2 — CAP 7 (Bioquímica Deep)
```
Leia context.md. Leia output/cap02_framework_FINAL.md para manter coerência de terminologia e profundidade. Leia data/Playbook_Técnico_da_SoulJu_draft_apoio.docx, data/27032026_HeroFormulas.xlsx, e todas as análises completas em data/. Execute agents/cap07_bioquimica.md com profundidade IGUAL ou SUPERIOR ao Cap 2. Mínimo 6000 palavras. Salve em output/cap07_bioquimica.md
```

### QA + Estratégico + Comercial (repetir para cada capítulo):
```
Leia agents/qa_review.md. Revise output/cap07_bioquimica.md. Salve em output/review_cap07.md
```
```
Leia agents/strategic_visionary.md. Revise output/cap07_bioquimica.md. Salve em output/strategic_review_cap07.md
```
```
Leia agents/commercial_brand.md. Gere outputs para output/cap07_bioquimica.md. Salve em output/commercial_review_cap07.md
```

---

## PASSO 3 — CAP 6 (Formulações)
```
Leia context.md. Leia output/cap02_framework_FINAL.md e output/cap07_bioquimica.md para coerência. Leia data/27032026_HeroFormulas.xlsx, data/120326_Formulacao_SoulJu_R1.xlsx, e todas as análises de produtos em data/. Execute agents/cap06_formulacoes.md. Mínimo 5000 palavras. Salve em output/cap06_formulacoes.md
```
> QA + Estratégico + Comercial (mesmo padrão)

---

## PASSO 4 — CAP 3 (Jornada Hormonal)
```
Leia context.md. Leia output/cap02_framework_FINAL.md para coerência. Leia data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx. Execute agents/cap03_jornada.md. Mínimo 5000 palavras. Salve em output/cap03_jornada.md
```
> QA + Estratégico + Comercial

---

## PASSO 5 — CAP 1 (Manifesto)
```
Leia context.md. Leia TODOS os capítulos já gerados em output/ para que o manifesto reflita o conteúdo real. Execute agents/cap01_manifesto.md. Mínimo 2500 palavras. Salve em output/cap01_manifesto.md
```
> QA + Estratégico + Comercial

---

## PASSO 6 — CAPS 4 e 5 (Data Science + Personas)
```
Leia context.md. Leia data/SoulJu_MVP_Decision_Report.xlsx e data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx. Execute agents/cap04_datascience.md. Mínimo 3500 palavras. Salve em output/cap04_datascience.md
```
```
Leia context.md. Leia data/SoulJu_MVP_Decision_Report.xlsx e data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx. Leia output/cap02_framework_FINAL.md para coerência. Execute agents/cap05_personas.md. Mínimo 3500 palavras. Salve em output/cap05_personas.md
```
> QA + Estratégico + Comercial para ambos

---

## PASSO 7 — CAPS 8, 9, 10, 11
```
Leia context.md e os capítulos já gerados. Execute agents/cap08_protocolos.md. Salve em output/cap08_protocolos.md
```
```
Leia context.md. Leia data/27032026_HeroFormulas.xlsx e data/Formulacao_Portfolio.xlsx. Execute agents/cap09_anvisa.md. Salve em output/cap09_anvisa.md
```
```
Leia context.md. Leia data/Estudo_Menopausa_Benchmark_SKU_5Eixos_v3_-_Copia.xlsx. Execute agents/cap10_benchmark.md. Salve em output/cap10_benchmark.md
```
```
Leia context.md. Leia todas as análises de produtos em data/ (P&Ls). Execute agents/cap11_financeiro.md. Salve em output/cap11_financeiro.md
```
> QA + Estratégico + Comercial para todos

---

## PASSO 8 — CAP 12 (Referências)
```
Leia context.md. Leia TODOS os capítulos em output/cap*.md. Compile todas as referências citadas. Execute agents/cap12_referencias.md. Salve em output/cap12_referencias.md
```
> QA apenas (não precisa de estratégico/comercial)

---

## PASSO 9 — INTEGRAÇÃO (coerência cross-chapter)
```
Leia agents/integrator.md. Leia TODOS os capítulos em output/cap*.md. Execute a verificação completa. Salve em output/integration_report.md
```
> Se houver inconsistências, corrija os capítulos afetados.

---

## PASSO 10 — DESIGN FINAL (PPTX)
```
Leia agents/design_compiler.md. Leia TODOS os capítulos aprovados em output/. Gere o PPTX premium com identidade SoulJu. Salve como output/SoulJu_Playbook_Tecnico_FINAL.pptx
```

---

## RESUMO DO PIPELINE POR CAPÍTULO

Para CADA capítulo, o fluxo é:

```
Gerar capítulo → QA (4 dimensões) → Estratégico (Jobs/Musk) → Comercial (brand)
     ↓                    ↓                    ↓                    ↓
  output/capXX.md    review_capXX.md    strategic_capXX.md    commercial_capXX.md
```

Se QA < 8/10 ou Estratégico identifica falhas → corrigir e re-rodar QA.

---

## AGENTES DISPONÍVEIS (17 total)

| Agente | Arquivo | Função |
|--------|---------|--------|
| Cap 1 Manifesto | agents/cap01_manifesto.md | Visão fundadora |
| Cap 2 Framework | agents/cap02_framework.md | 4 eixos metabólicos |
| Cap 3 Jornada | agents/cap03_jornada.md | Timeline FMP |
| Cap 4 Data Science | agents/cap04_datascience.md | NHANES + ML |
| Cap 5 Personas | agents/cap05_personas.md | 3 clusters |
| Cap 6 Formulações | agents/cap06_formulacoes.md | 7 produtos |
| Cap 7 Bioquímica | agents/cap07_bioquimica.md | Vias deep |
| Cap 8 Protocolos | agents/cap08_protocolos.md | Bundles |
| Cap 9 ANVISA | agents/cap09_anvisa.md | Regulatório |
| Cap 10 Benchmark | agents/cap10_benchmark.md | 19 SKUs |
| Cap 11 Financeiro | agents/cap11_financeiro.md | P&L |
| Cap 12 Referências | agents/cap12_referencias.md | Vancouver |
| **QA Review** | agents/qa_review.md | 4 dimensões, gate 8/10 |
| **Estratégico** | agents/strategic_visionary.md | Jobs/Musk filters |
| **Comercial** | agents/commercial_brand.md | Brand + claims |
| **Integrador** | agents/integrator.md | Coerência |
| **Design** | agents/design_compiler.md | PPTX final |

---

## FIX DO CAP 2 (prompt especial)
| Arquivo | prompts/fix_cap02.md | Correções V1+V2 merge |
