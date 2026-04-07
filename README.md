# SoulJu Playbook Generator — Multi-Agent System

## Setup (1 minuto)

```bash
cd soulju-playbook-agents
chmod +x run.sh
```

## Como Usar

### Método 1: Script automático (recomendado)
```bash
# Gerar todos os 12 capítulos
./run.sh all

# Gerar capítulos específicos
./run.sh 2          # Só o capítulo 2 (Framework Científico)
./run.sh 1 2 3      # Capítulos 1, 2 e 3

# Ver status
./run.sh status

# Compilar tudo em arquivo único
./run.sh compile
```

### Método 2: Claude Code direto (mais controle)
```bash
# Navegar para o diretório
cd soulju-playbook-agents

# Gerar um capítulo
claude -p "Leia o arquivo context.md para contexto completo. Depois leia agents/cap02_framework.md e execute TODAS as instruções contidas nele. Produza o conteúdo completo em Markdown e salve em output/cap02_framework.md"

# Gerar outro
claude -p "Leia context.md e execute agents/cap07_bioquimica.md. Salve em output/cap07_bioquimica.md"
```

### Método 3: Interativo (máximo controle)
```bash
cd soulju-playbook-agents
claude

# Dentro do Claude Code, digite:
> Leia context.md e agents/cap02_framework.md. Execute as instruções e salve o resultado em output/cap02_framework.md
```

## Ordem Recomendada de Geração

A ordem importa para referências cruzadas:

1. **Cap 2** — Framework Científico (espinha dorsal)
2. **Cap 7** — Bioquímica Deep (detalhe das vias)
3. **Cap 6** — Formulações (depende do framework)
4. **Cap 3** — Jornada Hormonal
5. **Cap 1** — Manifesto (melhor escrever depois do framework)
6. **Cap 4** — Data Science
7. **Cap 5** — Personas
8. **Cap 8** — Protocolos/Bundles
9. **Cap 9** — ANVISA
10. **Cap 10** — Benchmark
11. **Cap 11** — Financeiro
12. **Cap 12** — Referências (por último, compila tudo)

## Estrutura de Arquivos

```
soulju-playbook-agents/
├── CLAUDE.md          ← Instruções para Claude Code (lido automaticamente)
├── README.md          ← Este arquivo
├── context.md         ← Base de conhecimento compartilhada (TODOS os agentes leem)
├── run.sh             ← Script de execução automática
├── agents/            ← Prompts de cada agente/capítulo
│   ├── cap01_manifesto.md
│   ├── cap02_framework.md      ← O mais importante (8000+ palavras)
│   ├── cap03_jornada.md
│   ├── cap04_datascience.md
│   ├── cap05_personas.md
│   ├── cap06_formulacoes.md
│   ├── cap07_bioquimica.md     ← Segundo mais importante (6000+ palavras)
│   ├── cap08_protocolos.md
│   ├── cap09_anvisa.md
│   ├── cap10_benchmark.md
│   ├── cap11_financeiro.md
│   └── cap12_referencias.md
└── output/            ← Capítulos gerados (markdown)
    ├── cap01_manifesto.md
    ├── cap02_framework.md
    ├── ...
    └── SOULJU_PLAYBOOK_TECNICO_COMPLETO.md  ← Compilado final
```

## Nível de Exigência

Cada agente foi calibrado para produzir conteúdo nível:
- **Nestlé Health Science / DSM-Firmenich / Bayer**
- Vias metabólicas com enzimas e cofatores reais
- Evidências clínicas com autor, ano, n, resultado
- Tabelas detalhadas (carência → falha → sintoma → intervenção)
- Mínimo de palavras especificado por capítulo

## Estimativa de Output

| Capítulo | Palavras esperadas |
|----------|-------------------|
| Cap 1 Manifesto | 2.500+ |
| Cap 2 Framework | 8.000+ |
| Cap 3 Jornada | 5.000+ |
| Cap 4 Data Science | 3.500+ |
| Cap 5 Personas | 3.500+ |
| Cap 6 Formulações | 5.000+ |
| Cap 7 Bioquímica | 6.000+ |
| Cap 8 Protocolos | 4.000+ |
| Cap 9 ANVISA | 3.500+ |
| Cap 10 Benchmark | 3.000+ |
| Cap 11 Financeiro | 2.500+ |
| Cap 12 Referências | 2.500+ |
| **TOTAL** | **~49.000+** |

Isso equivale a ~100-120 páginas formatadas em documento final.

## Após Gerar

O output é Markdown. Para converter em PPTX premium com identidade SoulJu:
1. Use o arquivo compilado como input
2. Peça ao Claude (aqui ou no Code) para gerar o PPTX via pptxgenjs
3. Ou importe no Google Slides / Figma / Canva para design final

## Time Técnico (fictício, para autoria)

- **Dra. Marina Caldas** — PhD Bioquímica USP, pós-doc Harvard. Caps 1, 2, 6, 7
- **Dr. Rafael Andrade** — MD Endocrinologia UNIFESP. Caps 3, 8
- **Carolina Santos, MSc** — Data Science Insper. Caps 4, 5, 10, 11
- **Dra. Priscila Lima** — Farmacêutica UFRGS, ex-ANVISA. Caps 6, 9
- **Luísa Rezende, MSc** — Nutrição Funcional USP. Caps 1, 5, 8, 10
- **Thiago Moretti** — Design ESPM. Design editorial final

## Usar com OpenAI API (novo)

Se você quiser rodar os agentes via OpenAI (em vez do CLI `claude`), use o runner Python:

```bash
# 1) Defina a chave (sessão atual)
export OPENAI_API_KEY="sua_chave"

# opcional: escolher modelo
export OPENAI_MODEL="gpt-4.1-mini"

# 2) Rodar
python run_openai.py status
python run_openai.py 2
python run_openai.py all
python run_openai.py compile
```

Alternativamente, crie um arquivo `.env` na raiz com:

```env
OPENAI_API_KEY=sua_chave
OPENAI_MODEL=gpt-4.1-mini
```

> O script `run_openai.py` lê `.env` automaticamente.
