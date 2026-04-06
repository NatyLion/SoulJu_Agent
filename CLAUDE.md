# SoulJu Playbook Generator

## O que é
Sistema multi-agente para gerar o Playbook Técnico da SoulJu (12 capítulos).
Cada arquivo em `agents/` é um capítulo independente com contexto + prompt.

## Dados disponíveis na pasta `data/`
IMPORTANTE: Antes de gerar qualquer capítulo, LEIA os arquivos relevantes em `data/`:

| Arquivo | Conteúdo | Usado por |
|---------|----------|-----------|
| `context.md` (raiz) | Base de conhecimento completa | TODOS os agentes |
| `SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx` | Doc estratégico: NHANES, clusters, personas, roadmap | Caps 1,2,3,4,5 |
| `SoulJu_MVP_Decision_Report.xlsx` | 6 sheets: clusters k=3, PPI, feature importance, 5000 rows | Caps 4,5 |
| `27032026_HeroFormulas.xlsx` | 7 sheets: formulações Hero de todos os produtos | Caps 2,6,7 |
| `120326_Formulacao_SoulJu_R1.xlsx` | Formulações Padrão + Hero, 7 sheets | Caps 6,9 |
| `Femme-Lipidic-Fire-Analise-Completa.docx` | Análise Fire: tese, formulação, 5 pilares, P&L | Caps 2,6,7,11 |
| `Femme-Gut-Analise-Completa.docx` | Análise GUT: saciedade+microbioma+barreira, P&L | Caps 2,6,7,8,11 |
| `Night-Reset-Analise-Completa.docx` | Análise Night: Glicina hero, regenerador sistêmico, P&L | Caps 2,6,7,11 |
| `Femme-Cellular-Analise-Completa.docx` | Análise Cellular: NAD+, RiaGev, longevidade, P&L | Caps 2,6,7,11 |
| `Femme-Sculpt-PL-Investidores.docx` | Sculpt P&L 5 anos, unit economics | Caps 6,11 |
| `Estudo_Menopausa_Benchmark_SKU_5Eixos_v3_-_Copia.xlsx` | Benchmark 19 SKUs, scoring 5 eixos | Cap 10 |
| `Formulacao_Portfolio.xlsx` | Timeline, formulações Claude/GPT, ANVISA | Caps 6,9 |
| `Playbook_Técnico_da_SoulJu_draft_apoio.docx` | Draft com 4 eixos, matriz formulação, Krebs | Caps 2,7 |

## Como usar

### Gerar capítulo por capítulo (recomendado):
```bash
# Passo 1: Entrar no diretório
cd soulju-playbook-agents

# Passo 2: Gerar um capítulo (Claude Code lê context.md + data/ + prompt)
claude "Leia context.md para contexto geral. Depois leia os arquivos relevantes em data/ (use cat ou pandoc para .docx). Então execute as instruções em agents/cap02_framework.md. Produza o conteúdo completo e salve em output/cap02_framework.md"
```

### Gerar todos:
```bash
./run.sh all
```

## Regras para todos os agentes
- Idioma: Português BR
- Nível: Laboratórios globais (Nestlé Health Science, DSM-Firmenich)
- LEIA OS DADOS em data/ antes de escrever — use dados REAIS dos documentos, não invente
- Cada afirmação bioquímica deve ser rastreável a uma via real
- Incluir evidências clínicas (autor, ano, n, resultado)
- Formato: Markdown com tabelas
- Value proposition: estamos revolucionando, isso deve ser claro
- Mínimo de palavras: especificado em cada agente, RESPEITAR
