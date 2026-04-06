ANTES DE ESCREVER: Leia data/SoulJu_MVP_Decision_Report.xlsx (6 sheets com clusters, PPI, feature importance, sample rows) e data/SoulJu_Strategic_Doc_Tecnico_Posicionamento.docx.

Leia o arquivo context.md neste diretório para contexto completo da SoulJu.

Você é Carolina Santos, MSc Ciência de Dados Insper. Especialista NHANES, Random Forest, K-Means, SHAP. Nível: methods section de Nature Methods — reprodutível, rigoroso.

Escreva o CAPÍTULO 4 — SUPORTE TÉCNICO: MODELOS ML E DADOS NHANES.

## 4.1 Base de Dados
- NHANES-L 2021-2023, n=11.933, n clustering=7.491
- Variáveis: DEMO, SLQ, HSCRP, GLU, INS, GHB, TRIGLY, HDL, FERTIN, FOLATE, VID, TST, BMX
- Linkage por SEQN, target sono SLD012 (cobertura 70.3%)

## 4.2 Construção dos 6 Eixos Sintomáticos
- Z-scores por biomarcador → média por eixo → percentil 0-10
- Tabela: Eixo | Biomarcadores | Z-score formula | Interpretação
- Imputation: SimpleImputer (median), Scaling: StandardScaler

## 4.3 Clusterização K-Means
- k=3-7, seleção por silhouette, melhor k=3
- Perfil completo de cada cluster (tabela com todos os scores)
- Validação: silhouette score, elbow, estabilidade bootstrap

## 4.4 Modelos Preditivos de Sono
- RF Regressor: 400 árvores, max_depth=None, min_samples_leaf=5
- RF Classifier: target sleep_bad (≤6h), threshold 0.5
- Feature importance MDI por eixo
- Night Reset Fit Score: como foi calculado, resultado 2.5%

## 4.5 Pain Priority Index
- PPI = prevalência(P75) × severidade(top25)
- Resultado flat (2.18-2.20) — por quê
- Discriminação real nos clusters

## 4.6 Limitações e Reprodutibilidade
- Base inclui M/F todas idades (refinar para F 35-65)
- Cortisol ausente (DHEA-S proxy), vitamina D sazonal
- Pipeline Python pseudocódigo completo

TOTAL: 3500+ palavras. Salve como output/cap04_datascience.md
