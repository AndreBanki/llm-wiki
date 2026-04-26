---
title: AltoQi Visus Planning
type: product
created: 2026-04-26
updated: 2026-04-26
sources: [gt-antac-visus-planning-objeto-aprendizagem.md, Planejamento de obra 4.0_ algoritmos que otimizam cronogramas e antecipam gargalos _ LinkedIn.pdf, linkedin-post-jhonatan-lazarin-ia-gestao-obras, linkedin-alexander-mattos-contratos-engenharia-2026-04-25]
tags: [altoqi, visus-planning, bim, planejamento-4d, simulacao, cronograma, eap, ifc, construção, produto]
---

Plataforma BIM de planejamento de obras da AltoQi. Integra modelo federado IFC, EAP, orçamento e cronograma 4D em um único ambiente — da simulação da sequência construtiva ao rastreamento planejado vs. executado.

---

## O que é

AltoQi Visus Planning é o módulo de planejamento da suíte Visus (AltoQi). Permite:

1. Importar o **modelo federado** (múltiplos IFCs: arquitetura, estrutura, instalações, canteiro)
2. Definir a **EAP** (estrutura analítica de projeto) usando as propriedades dos elementos IFC como critérios de hierarquia
3. Construir o **cronograma** com predecessoras, setorização e calendário de obra
4. **Simular** a sequência construtiva em animação 4D
5. **Acompanhar** o planejado vs. executado com percentuais e datas reais
6. Gerar **relatórios** integrados ao orçamento (curva S, histograma de mão de obra, Excel)

---

## Posicionamento nas Cinco Frentes de IA

| Frente | Status no Visus Planning |
|---|---|
| 1 — Planejamento e previsão | ✅ Core do produto |
| 2 — Controle financeiro em tempo real | ✅ Via integração com Visus Cost Management |
| 3 — Gestão de equipes / produtividade | 🔶 Histograma de mão de obra disponível |
| 4 — Execução e monitoramento | ✅ Rastreamento planejado vs. executado (v2024) |
| 5 — Análise e melhoria contínua | 🔶 Potencial via relatórios; não é frente principal |

---

## Workflow Operacional (versão 2024)

### Abas e integração

O produto tem três abas principais integradas em torno da mesma EAP:

```
Quantitativo ←→ Orçamento ←→ Planejamento
     ↑
  (EAP definida aqui)
```

**Regra crítica:** a EAP é sempre definida na aba de **Quantitativo**. Qualquer alteração de hierarquia vai lá — não na aba de Planejamento.

### Passo 1 — Modelo federado

- Criar projeto a partir de IFC (diretório local ou Visus Colab)
- Aplicar ou criar template de tipologia
- Adicionar todos os IFCs disciplinares
- Gerir status: 🟢 atualizado / ⚠️ desatualizado / 🔴 caminho inválido
- Ativar/desativar modelos e elementos individualmente

### Passo 2 — Análise de metadados

- Aba **Metadados**: todas as propriedades do elemento IFC + propriedades geométricas calculadas pelo Visus
- Propriedades geométricas calculadas: área de projeção (superior/lateral/frontal), altura e largura da caixa delimitadora
- Edição de entidade IFC possível (reclassificação local — não modifica o IFC original; perdida se o IFC for recarregado)

### Passo 3 — EAP

- Configuração de até 5 níveis hierárquicos
- Critérios por nível: qualquer propriedade dos metadados (disciplina, pavimento, entidade, ambiente, etc.)
- Estrutura típica: Disciplina → Elemento → Pavimento → Setor

### Passo 4 — Setorização

Quando o IFC não tem propriedade de setor:
1. Identificar coordenadas X/Y de elementos na extremidade de cada setor (aba Metadados)
2. Filtrar elementos por condição `X > valor` ou `X < valor`
3. Preencher campo **Ambiente** como identificador de setor
4. O campo Ambiente torna-se critério disponível na EAP

### Passo 5 — Cronograma

- Configurar calendário (jornada, feriados, turno reduzido)
- Definir datas de início e duração para cada atividade
- Predecessoras:
  - **TI (Término a Início):** padrão — começa quando a anterior termina
  - **II (Início a Início):** atividades começam juntas
  - **Latência:** espera N dias após a predecessora
  - Múltiplas predecessoras: atividade aguarda N condições

### Passo 6 — Simulação 4D

- **Data específica:** estado da obra em um dia escolhido (executado = cor sólida, em execução = transparente)
- **Play:** animação da sequência completa (duração configurável)
- Validação: identificar serviços fora de sequência durante a animação
- Limitação: sem exportação nativa de vídeo (usar captura de tela externa em tela cheia)

### Passo 7 — Rastreamento Planejado vs. Executado

| Aba | Conteúdo |
|---|---|
| Planejado | Datas e durações previstas |
| Executado | Datas reais + percentual de execução |
| Ambos | Comparativo; identifica descolamentos |

### Passo 8 — Relatórios

| Relatório | Integração |
|---|---|
| Curva S | Orçamento + cronograma |
| Histograma de mão de obra | Composições orçamentárias (horas ou custo por período) |
| Orçamento por etapa de obra | EAP + valores; exportado como Excel editável |

---

## Dimensão Contratual

O tipo de contrato determina **o que precisa de visibilidade** e **para quem** no Visus Planning:

| Tipo de Contrato | Foco no Visus | Stakeholder primário |
|---|---|---|
| Turn-key / EPC | Avanço físico, variações de escopo, interfaces, gargalos | Gestão da contratada |
| Preço Unitário | Medições, quantidades executadas, produtividade | Fiscal do dono + contratada |
| Administração / Cost Plus | Custos, eficiência de equipe, horas alocadas | Dono da obra |
| Aliança / IPD | Visibilidade total para todos os parceiros | Todos |

Ver [[bim-construction/tipos-contrato-engenharia]] para a análise completa.

---

## Contexto de Adoção no Brasil

O Projeto Construa Brasil (MDIC) produziu objetos de aprendizagem BIM gratuitos usando o Visus Planning como ferramenta de referência para planejamento 4D — indicativo do posicionamento do produto no ecossistema BIM brasileiro de capacitação acadêmica e profissional.

---

## Related Pages

- [[bim-construction/gt-antac-visus-planning-objeto-aprendizagem]] — tutorial completo dos 4 módulos
- [[bim-construction/planejamento-preditivo-obras]] — conceito de planejamento preditivo
- [[bim-construction/tipos-contrato-engenharia]] — dimensão contratual
- [[bim-construction/bim-coordination]] — coordenação de modelos federados
- [[bim-construction/jhonatan-lazarin-ia-gestao-obras]] — cinco frentes de IA na gestão de obras
- [[bim-construction/alexander-mattos-contratos-engenharia]] — contratos como variável de produto
