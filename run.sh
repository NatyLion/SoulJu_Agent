#!/bin/bash
# ═══════════════════════════════════════════════════════════
# SoulJu Playbook Generator — Runner para Claude Code
# ═══════════════════════════════════════════════════════════
#
# USO:
#   ./run.sh all          # Gera todos os 12 capítulos
#   ./run.sh 2            # Gera só o capítulo 2
#   ./run.sh 1 2 3        # Gera capítulos 1, 2 e 3
#   ./run.sh compile      # Junta tudo em arquivo único
#   ./run.sh status       # Mostra quais já foram gerados
#
# REQUISITO: Claude Code instalado e autenticado
# ═══════════════════════════════════════════════════════════

set -e
cd "$(dirname "$0")"
mkdir -p output

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${CYAN}═══════════════════════════════════════════${NC}"
echo -e "${YELLOW}  🧬 SoulJu Playbook Generator${NC}"
echo -e "${CYAN}  Multi-Agent System · 12 Capítulos${NC}"
echo -e "${CYAN}═══════════════════════════════════════════${NC}"
echo ""

# Mapeamento de agentes
declare -A AGENTS
AGENTS[1]="cap01_manifesto"
AGENTS[2]="cap02_framework"
AGENTS[3]="cap03_jornada"
AGENTS[4]="cap04_datascience"
AGENTS[5]="cap05_personas"
AGENTS[6]="cap06_formulacoes"
AGENTS[7]="cap07_bioquimica"
AGENTS[8]="cap08_protocolos"
AGENTS[9]="cap09_anvisa"
AGENTS[10]="cap10_benchmark"
AGENTS[11]="cap11_financeiro"
AGENTS[12]="cap12_referencias"

declare -A NAMES
NAMES[1]="Manifesto (Marina + Luísa)"
NAMES[2]="Framework Científico (Marina)"
NAMES[3]="Jornada Hormonal (Rafael)"
NAMES[4]="Data Science NHANES (Carolina)"
NAMES[5]="Personas (Luísa + Carolina)"
NAMES[6]="Formulações (Marina + Priscila)"
NAMES[7]="Bioquímica Deep (Marina)"
NAMES[8]="Protocolos/Bundles (Luísa + Rafael)"
NAMES[9]="ANVISA (Priscila)"
NAMES[10]="Benchmark (Luísa + Carolina)"
NAMES[11]="Financeiro (Carolina)"
NAMES[12]="Referências (Todos)"

# ── Função: gerar um capítulo ──
generate_chapter() {
    local num=$1
    local agent=${AGENTS[$num]}
    local name=${NAMES[$num]}
    local input="agents/${agent}.md"
    local outfile="output/${agent}.md"

    if [ ! -f "$input" ]; then
        echo -e "${RED}  ❌ Agente não encontrado: $input${NC}"
        return 1
    fi

    echo -e "${YELLOW}  🤖 Capítulo $num: $name${NC}"
    echo -e "     Prompt: $input"
    echo -e "     Output: $outfile"
    echo ""

    # Concatenar contexto + prompt do agente
    local full_prompt
    full_prompt=$(cat context.md; echo ""; echo "---"; echo ""; cat "$input")

    # Chamar Claude Code
    echo -e "     ${CYAN}⏳ Gerando...${NC}"
    local start_time=$(date +%s)

    # Usar claude com o prompt do agente
    echo "$full_prompt" | claude --output-format text > "$outfile" 2>/dev/null || {
        # Fallback: tentar com -p flag
        claude -p "$(cat "$input")" --output-format text > "$outfile" 2>/dev/null || {
            echo -e "     ${RED}❌ Erro na geração. Tentando método alternativo...${NC}"
            # Método alternativo: salvar prompt e chamar
            claude "Leia o arquivo $(pwd)/context.md para contexto. Depois leia $(pwd)/$input e execute as instruções. Salve o resultado em $(pwd)/$outfile" 2>/dev/null || {
                echo -e "     ${RED}❌ Falha. Execute manualmente:${NC}"
                echo -e "     ${YELLOW}cd $(pwd) && claude -p agents/${agent}.md${NC}"
                return 1
            }
        }
    }

    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    local chars=$(wc -c < "$outfile" 2>/dev/null || echo "0")

    echo -e "     ${GREEN}✅ Gerado: ${chars} caracteres em ${duration}s${NC}"
    echo ""
}

# ── Função: status ──
show_status() {
    echo -e "${CYAN}  Status dos Capítulos:${NC}"
    echo ""
    for i in $(seq 1 12); do
        local agent=${AGENTS[$i]}
        local name=${NAMES[$i]}
        local outfile="output/${agent}.md"
        if [ -f "$outfile" ]; then
            local chars=$(wc -c < "$outfile")
            local words=$(wc -w < "$outfile")
            echo -e "  ${GREEN}✅ Cap $i${NC} — $name (${words} palavras)"
        else
            echo -e "  ${RED}⏳ Cap $i${NC} — $name (pendente)"
        fi
    done
    echo ""
}

# ── Função: compilar ──
compile_all() {
    local compiled="output/SOULJU_PLAYBOOK_TECNICO_COMPLETO.md"
    echo -e "${YELLOW}  📄 Compilando Playbook...${NC}"

    echo "# SoulJu — Playbook Técnico" > "$compiled"
    echo "" >> "$compiled"
    echo "## A Bíblia Científica da Plataforma Metabólica Feminina" >> "$compiled"
    echo "" >> "$compiled"
    echo "*Compilado em: $(date '+%d/%m/%Y %H:%M')*" >> "$compiled"
    echo "" >> "$compiled"
    echo "---" >> "$compiled"
    echo "" >> "$compiled"

    local total_words=0
    for i in $(seq 1 12); do
        local agent=${AGENTS[$i]}
        local outfile="output/${agent}.md"
        if [ -f "$outfile" ]; then
            cat "$outfile" >> "$compiled"
            echo "" >> "$compiled"
            echo "---" >> "$compiled"
            echo "" >> "$compiled"
            local w=$(wc -w < "$outfile")
            total_words=$((total_words + w))
            echo -e "  ${GREEN}✅ Cap $i incluído ($w palavras)${NC}"
        else
            echo -e "  ${RED}⏳ Cap $i pendente${NC}"
        fi
    done

    echo ""
    echo -e "${GREEN}  📄 Playbook compilado: $compiled${NC}"
    echo -e "${GREEN}  📊 Total: $total_words palavras${NC}"
    echo ""
}

# ── MAIN ──
case "${1:-}" in
    all)
        echo -e "${YELLOW}  Gerando TODOS os 12 capítulos...${NC}"
        echo ""
        for i in $(seq 1 12); do
            generate_chapter "$i"
        done
        compile_all
        ;;
    compile)
        compile_all
        ;;
    status)
        show_status
        ;;
    "")
        echo "Uso:"
        echo "  ./run.sh all          # Gera todos os 12 capítulos"
        echo "  ./run.sh 2            # Gera capítulo 2"
        echo "  ./run.sh 1 2 3        # Gera capítulos 1, 2 e 3"
        echo "  ./run.sh compile      # Junta tudo em arquivo único"
        echo "  ./run.sh status       # Mostra quais foram gerados"
        echo ""
        echo "Ou execute manualmente com Claude Code:"
        echo "  cd soulju-playbook-agents"
        echo '  claude -p "Leia context.md. Depois execute agents/cap02_framework.md. Salve em output/cap02_framework.md"'
        ;;
    *)
        # Gerar capítulos específicos
        for num in "$@"; do
            if [[ "$num" =~ ^[0-9]+$ ]] && [ "$num" -ge 1 ] && [ "$num" -le 12 ]; then
                generate_chapter "$num"
            else
                echo -e "${RED}  ❌ Capítulo inválido: $num (use 1-12)${NC}"
            fi
        done
        ;;
esac
