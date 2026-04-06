# PROMPT PARA CORRIGIR O CAPÍTULO 2 NO CLAUDE CODE
# Cole este texto no Claude Code após navegar até a pasta do projeto

Leia os seguintes arquivos nesta ordem:

1. context.md (contexto completo da SoulJu)
2. output/cap02_framework.md (versão V2 atual — 12.326 palavras, esta é a BASE)
3. data/Cap02.docx (versão V1 — documento regulatório com elementos úteis)

Agora execute estas correções na V2, mantendo 95% do conteúdo original da V2 e incorporando apenas 3 elementos da V1:

## CORREÇÃO 1 — Adicionar seção de rastreabilidade (da V1)
Ao final do capítulo, ANTES das referências, adicione:

### Cadeia de Rastreabilidade Científica
Para cada afirmação neste capítulo, a cadeia de evidência segue:
Fonte primária (PubMed/NHANES) → Mecanismo de via (enzima + cofator) → Nó molecular (acetil-CoA/NAD⁺/GSH/α-KG) → Função do eixo → Hipótese de suporte funcional → Comunicação não-terapêutica

Nenhuma afirmação neste documento diagnostica, trata, cura ou previne doença. Todas as intervenções são enquadradas como suporte à função fisiológica.

## CORREÇÃO 2 — Adicionar seção de limitações (da V1)
Após a rastreabilidade, adicione:

### Limitações e Riscos Metodológicos
1. Hierarquia de evidência: algumas conexões via-ingrediente são de alta plausibilidade biológica mas não confirmadas por RCTs em todas as subpopulações femininas.
2. Risco de atribuição em sistemas multi-ingrediente: a coerência mecanística por via não isola efeitos de compostos individuais em protocolos reais.
3. Transportabilidade NHANES: rankings de feature importance podem variar por faixa etária, geografia e definição fenotípica.
4. Heterogeneidade hormonal: perimenopausa/menopausa são biologicamente diversas; direcionalidade de efeito pode variar por status basal.
5. Drift regulatório: limites de wordng ANVISA podem variar por jurisdição e requerem revisão jurídico-regulatória contínua.

## CORREÇÃO 3 — Adicionar notas regulatórias nos heroes
Em CADA hero ingredient que faz analogia farmacológica (GlucoVantage® "mesma via da metformina", CoQ10 "forma ativa", etc.), adicione em itálico ao final:

*(Nota regulatória: analogia mecanística de uso técnico interno — comunicação ao consumidor deve seguir claims permitidos ANVISA IN 28/76. Cf. RDC 429/2020.)*

## CORREÇÃO 4 — Reforçar introdução com visão revolucionária
Na introdução "Por Que 4 Eixos, Não 1 Suplemento", adicione após o primeiro parágrafo:

"Steve Jobs dizia que design não é como algo parece — é como algo funciona. A SoulJu aplicou este princípio à bioquímica feminina: não redesenhamos a embalagem de um suplemento. Redesenhamos a arquitetura de intervenção. Partimos dos dados (NHANES n=11.933), identificamos os 4 eixos que determinam a saúde metabólica da mulher, e construímos formulações que atuam nos pontos exatos onde as vias falham. Assim como Elon Musk decompôs o custo de um foguete por matéria-prima para provar que era possível reduzir 10x, nós decompomos cada sintoma feminino até a enzima e o cofator que falham — e intervimos ali, com dose terapêutica e ingrediente patenteado. O resultado não é um suplemento melhor. É uma categoria nova."

## CORREÇÃO 5 — Fechamento visceral
Ao final da seção "Plataforma, Não Suplemento", adicione:

"Este capítulo contém 14.000 palavras de mecanismo molecular. Cada enzima é real. Cada cofator é rastreável. Cada estudo tem autor, ano e n. Nenhum concorrente no mercado brasileiro possui este nível de fundamentação bioquímica — porque nenhum concorrente partiu dos dados para construir os produtos. Eles partiram do marketing. Nós partimos das mitocôndrias.

A mulher que toma um suplemento genérico está jogando nutrientes contra a parede esperando que algo grude. A mulher que usa SoulJu está restaurando 4 sistemas biológicos interconectados com a precisão de quem conhece cada enzima pelo nome.

Isso não é otimização. É revolução metabólica."

## INSTRUÇÕES FINAIS
- Mantenha TODO o conteúdo técnico da V2 intacto (tabelas, EC numbers, evidências, cadeias causais)
- Apenas ADICIONE as 5 correções acima nos pontos indicados
- NÃO remova, simplifique ou "suavize" nenhum conteúdo técnico
- O documento deve ficar com ~13.500-14.000 palavras
- Salve como output/cap02_framework_FINAL.md
