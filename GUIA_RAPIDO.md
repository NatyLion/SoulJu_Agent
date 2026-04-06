# 🧬 SoulJu Playbook — Guia Rápido Passo a Passo
## Para quem nunca rodou múltiplos agentes no Claude Code

---

## ANTES DE COMEÇAR

Você precisa ter:
- ✅ Claude Code instalado (`claude` funciona no terminal)
- ✅ Pasta `soulju-playbook-agents` descompactada
- ✅ Arquivos de dados na pasta `data/` (13 arquivos .docx/.xlsx/.pptx)

---

## PASSO 1 — ABRIR O TERMINAL

**Mac:** Abra o app "Terminal" (está em Aplicativos > Utilitários)
**Windows:** Abra "PowerShell" ou "Terminal" (busque na barra de tarefas)

---

## PASSO 2 — NAVEGAR ATÉ A PASTA DO PROJETO

Digite no terminal (ajuste o caminho se descompactou em outro lugar):

```
cd ~/Downloads/soulju-playbook-agents
```

Para confirmar que está no lugar certo, digite:

```
ls
```

Você deve ver: `CLAUDE.md  README.md  agents  context.md  data  run.sh`

---

## PASSO 3 — CRIAR A PASTA DE OUTPUT

```
mkdir -p output
```

---

## PASSO 4 — ABRIR O CLAUDE CODE

```
claude
```

O Claude Code vai iniciar e ler automaticamente o CLAUDE.md.
Você vai ver o prompt do Claude Code esperando seu comando.

---

## PASSO 5 — GERAR OS CAPÍTULOS (copie e cole cada comando)

### ⚡ CAPÍTULO 2 — Framework Científico (COMECE POR ESTE)
```
Leia o arquivo context.md neste diretório para contexto completo da SoulJu. Depois leia os seguintes arquivos de dados: data/Playbook_Técnico_da_SoulJu_draft_apoio.docx, data/27032026_HeroFormulas.xlsx, data/Femme-Lipidic-Fire-Analise-Completa.docx, data/Femme-Cellular-Analise-Completa.docx, data/Night-Reset-Analise-Completa.docx, data/Femme-Gut-Analise-Completa.docx. Agora leia agents/cap02_framework.md e execute TODAS as instruções contidas nele com profundidade máxima. O resultado deve ter no mínimo 8000 palavras em Markdown. Salve o resultado em output/cap02_framework.md
```

### 🔍 QA DO CAPÍTULO 2
```
Leia agents/qa_review.md para entender o processo de revisão. Depois leia output/cap02_framework.md e execute a revisão completa nas 4 dimensões (científica, regulatória, clínica, editorial). Dê nota 0-10 em cada. Salve o relatório em output/review_cap02.md
```

> Se a nota for ≥8 em todas as dimensões: prossiga para o próximo capítulo.
> Se alguma nota for <8: peça para corrigir:
```
Leia output/review_cap02.md. Corrija os problemas identificados no output/cap02_framework.md. Salve a versão corrigida sobrescrevendo output/cap02_framework.md
```

---

### 🔬 CAPÍTULO 7 — Bioquímica Deep Dive
```
Leia context.md. Leia data/Playbook_Técnico_da_SoulJu_draft_apoio.docx, data/27032026_HeroFormulas.xlsx, e todas as análises completas de produtos em data/. Também leia output/cap02_framework.md para manter coerência. Agora execute agents/cap07_bioquimica.md com profundidade máxima. Mínimo 6000 palavras. Salve em output/cap07_bioquimica.md
```

### 🔍 QA DO CAPÍTULO 7
```
Leia agents/qa_review.md. Revise output/cap07_bioquimica.md nas 4 dimensões. Salve em output/review_cap07.md
```

---

### 💊 CAPÍTULO 6 — Formulações
```
Leia context.md. Leia data/27032026_HeroFormulas.xlsx, data/120326_Formulacao_SoulJu_R1.xlsx, e todas as análises de produtos em data/. Leia output/cap02_framework.md para manter coerência. Execute agents/cap06_formulacoes.md. Mínimo 5000 palavras. Salve em output/cap06_formulacoes.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap06_formulacoes.md. Salve em output/review_cap06.md
```

---

### 🔄 CAPÍTULO 3 — Jornada Hormonal
```
Leia context.md. Leia data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx. Leia output/cap02_framework.md para coerência. Execute agents/cap03_jornada.md. Mínimo 5000 palavras. Salve em output/cap03_jornada.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap03_jornada.md. Salve em output/review_cap03.md
```

---

### 📜 CAPÍTULO 1 — Manifesto
```
Leia context.md. Leia todos os capítulos já gerados em output/cap02*.md, output/cap07*.md, output/cap06*.md, output/cap03*.md para que o manifesto reflita o conteúdo real do Playbook. Execute agents/cap01_manifesto.md. Mínimo 2500 palavras. Salve em output/cap01_manifesto.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap01_manifesto.md. Salve em output/review_cap01.md
```

---

### 📊 CAPÍTULO 4 — Data Science
```
Leia context.md. Leia data/SoulJu_MVP_Decision_Report.xlsx e data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx. Execute agents/cap04_datascience.md. Mínimo 3500 palavras. Salve em output/cap04_datascience.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap04_datascience.md. Salve em output/review_cap04.md
```

---

### 👤 CAPÍTULO 5 — Personas
```
Leia context.md. Leia data/SoulJu_MVP_Decision_Report.xlsx e data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx. Execute agents/cap05_personas.md. Mínimo 3500 palavras. Salve em output/cap05_personas.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap05_personas.md. Salve em output/review_cap05.md
```

---

### 📦 CAPÍTULO 8 — Protocolos e Bundles
```
Leia context.md. Leia output/cap02_framework.md e output/cap06_formulacoes.md para coerência. Execute agents/cap08_protocolos.md. Mínimo 4000 palavras. Salve em output/cap08_protocolos.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap08_protocolos.md. Salve em output/review_cap08.md
```

---

### 📋 CAPÍTULO 9 — ANVISA
```
Leia context.md. Leia data/27032026_HeroFormulas.xlsx, data/120326_Formulacao_SoulJu_R1.xlsx, data/Formulacao_Portfolio.xlsx. Execute agents/cap09_anvisa.md. Mínimo 3500 palavras. Salve em output/cap09_anvisa.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap09_anvisa.md. Salve em output/review_cap09.md
```

---

### 🏆 CAPÍTULO 10 — Benchmark
```
Leia context.md. Leia data/Estudo_Menopausa_Benchmark_SKU_5Eixos_v3_-_Copia.xlsx. Execute agents/cap10_benchmark.md. Mínimo 3000 palavras. Salve em output/cap10_benchmark.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap10_benchmark.md. Salve em output/review_cap10.md
```

---

### 💰 CAPÍTULO 11 — Financeiro
```
Leia context.md. Leia data/Femme-Lipidic-Fire-Analise-Completa.docx, data/Femme-Gut-Analise-Completa.docx, data/Night-Reset-Analise-Completa.docx, data/Femme-Cellular-Analise-Completa.docx, data/Femme-Sculpt-PL-Investidores.docx. Execute agents/cap11_financeiro.md. Mínimo 2500 palavras. Salve em output/cap11_financeiro.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap11_financeiro.md. Salve em output/review_cap11.md
```

---

### 📚 CAPÍTULO 12 — Referências
```
Leia context.md. Leia TODOS os capítulos em output/cap*.md para compilar todas as referências citadas. Execute agents/cap12_referencias.md. Mínimo 2500 palavras. Salve em output/cap12_referencias.md
```

### 🔍 QA
```
Leia agents/qa_review.md. Revise output/cap12_referencias.md. Salve em output/review_cap12.md
```

---

## PASSO 6 — INTEGRAÇÃO (verificar coerência entre capítulos)

```
Leia agents/integrator.md. Depois leia TODOS os capítulos em output/cap*.md. Execute a verificação completa de coerência, terminologia, referências cruzadas e dados. Salve o relatório em output/integration_report.md
```

> Se houver inconsistências, corrija os capítulos afetados antes de prosseguir.

---

## PASSO 7 — DESIGN E COMPILAÇÃO FINAL

```
Leia agents/design_compiler.md. Leia TODOS os capítulos aprovados em output/cap*.md. Gere o script Node.js para criar o PPTX premium com identidade SoulJu. Salve o script em output/generate_playbook_final.js e execute-o para gerar output/SoulJu_Playbook_Tecnico_FINAL.pptx
```

---

## DICAS IMPORTANTES

### ⏱️ Tempo estimado
- Cada capítulo: 3-8 minutos para gerar
- Cada QA: 2-3 minutos
- Total estimado: 2-3 horas para o Playbook completo

### 💡 Se o Claude Code travar ou der erro
- Digite `/clear` para limpar o contexto
- Tente novamente com o mesmo comando
- Se persistir, saia com `Ctrl+C` e rode `claude` novamente

### 💡 Se um capítulo ficou curto demais
Peça para expandir:
```
Leia output/cap02_framework.md. O conteúdo está abaixo do mínimo de 8000 palavras. Expanda todas as seções que estão superficiais, especialmente as tabelas de vias metabólicas e as cadeias causais. Sobrescreva output/cap02_framework.md
```

### 💡 Se o QA reprovou
Peça para corrigir com feedback:
```
Leia output/review_cap02.md. Corrija TODOS os problemas listados no capítulo output/cap02_framework.md. Foque especialmente nas correções obrigatórias. Sobrescreva output/cap02_framework.md
```

### 💡 Para ver o que já foi gerado
```
Liste os arquivos em output/ e me diga o tamanho de cada um em palavras
```

### 📋 Checklist de progresso
Marque conforme for completando:

- [ ] Cap 2 gerado + QA aprovado
- [ ] Cap 7 gerado + QA aprovado
- [ ] Cap 6 gerado + QA aprovado
- [ ] Cap 3 gerado + QA aprovado
- [ ] Cap 1 gerado + QA aprovado
- [ ] Cap 4 gerado + QA aprovado
- [ ] Cap 5 gerado + QA aprovado
- [ ] Cap 8 gerado + QA aprovado
- [ ] Cap 9 gerado + QA aprovado
- [ ] Cap 10 gerado + QA aprovado
- [ ] Cap 11 gerado + QA aprovado
- [ ] Cap 12 gerado + QA aprovado
- [ ] Integração verificada
- [ ] Design PPTX gerado
- [ ] ✅ PLAYBOOK COMPLETO!
