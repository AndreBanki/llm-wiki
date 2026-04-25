---
title: Tipos de Contrato em Engenharia
type: concept
created: 2026-04-25
updated: 2026-04-25
sources: [linkedin-alexander-mattos-contratos-engenharia-2026-04-25]
tags: [contratos, engenharia, risco, epc, turn-key, empreitada, preço-unitário, administração, alocação-de-risco, visus-planning, stakeholders]
---

# Tipos de Contrato em Engenharia

O tipo de contrato define como o risco é alocado entre as partes em um projeto de engenharia — e, consequentemente, o que precisa ser gerenciado, monitorado e visível no planejamento. Contratos não são apenas modelos jurídicos: são modelos de alocação de risco, previsibilidade de resultado e geração (ou destruição) de valor.

> "Grande parte dos problemas em projetos de engenharia não nasce na execução. Nasce na forma como o contrato foi estruturado."
> — Alexander Mattos

---

## Princípio Central: Contrato como Modelo de Risco

Cada tipo de contrato responde à pergunta: **quem paga quando algo inesperado acontece?**

A resposta define:
- Qual parte tem incentivo para controlar custos e prazos
- Quais informações cada stakeholder precisa monitorar
- Quais aspectos do planejamento são críticos para quem
- Onde surgem disputas (claims) e por que

---

## Principais Modelos Contratuais

### Turn-key / EPC / Empreitada Integral

O modelo de maior integração: a contratada recebe o escopo completo e entrega o projeto funcional. Todo o risco de execução — prazo, custo, interfaces entre disciplinas — é absorvido pela contratada.

| Dimensão | Caracterização |
|---|---|
| Integração | Máxima (escopo, prazo, custo em bloco único) |
| Interfaces críticas | Sim — disciplinas e subcontratadas dependem entre si |
| Prazos | Tipicamente agressivos |
| Ponto de falha | Mudanças de escopo e erros de engenharia geram impacto direto no custo total |
| Risco para a contratada | Muito alto |
| Vulnerabilidade a mudanças | Alta |
| Visibilidade necessária para o dono | Baixa (pagamento por entrega) |
| Visibilidade necessária para a contratada | Total (avanço físico, interfaces, gargalos, variações) |

**Implicação para Visus Planning:** Produto voltado à gestão da contratada. O dono da obra tem poucos pontos de controle direto — os dashboards relevantes são os da equipe de gestão da contratada.

---

### Preço Unitário (Unit Price)

A contratada é remunerada por unidade de serviço executada (metro linear, m², ton, etc.). O risco de quantidade fica com o dono; o risco de custo unitário fica com a contratada.

| Dimensão | Caracterização |
|---|---|
| Risco de quantidade | Dono da obra |
| Risco de custo unitário | Contratada |
| Medição | Central — base de pagamento são as quantidades medidas e atestadas |
| Claims típicos | Divergências de medição; quantidades muito diferentes do previsto em contrato |
| Visibilidade necessária | Medições precisas, produtividade por atividade, avanço físico por item contratual |
| Stakeholder primário | Fiscal do dono + gestão da contratada |

---

### Administração / Cost Plus / Reembolso

A contratada é remunerada pelos custos reais incorridos mais uma margem (fixa ou percentual). O risco de custo total fica com o dono da obra.

| Dimensão | Caracterização |
|---|---|
| Risco de custo | Dono da obra |
| Incentivo de eficiência | Baixo para a contratada (quanto mais gasta, mais recebe, em modelos percentuais) |
| Variante com incentivo | Cost Plus com Fee Incentivado — bônus por economias |
| Visibilidade necessária | Todos os custos, eficiência da equipe, horas alocadas |
| Stakeholder primário | Dono da obra e seu fiscal |
| Aplicação típica | Obras com escopo indefinido no início; emergências; P&D |

---

### Aliança / Integrated Project Delivery (IPD)

Modelo colaborativo em que o risco e o lucro são compartilhados entre dono, projetistas e construtora. As partes têm ganhos alinhados — todos ganham quando o projeto vai bem, todos perdem quando vai mal.

| Dimensão | Caracterização |
|---|---|
| Risco | Compartilhado (pool de risco e lucro conjunto) |
| Incentivo de eficiência | Alto — todas as partes têm interesse no resultado total |
| Transparência necessária | Total — modelo requer livros abertos |
| Visibilidade necessária | Todos os dados para todos os parceiros |
| Aplicação típica | Projetos de alta complexidade; infraestrutura pública; obras hospitalares |
| Prevalência no Brasil | Baixa — modelo emergente, mais comum em Austrália e EUA |

---

## Matriz de Risco por Tipo de Contrato

| Tipo | Risco p/ Contratada | Risco p/ Dono | Vulnerabilidade a Mudanças | Complexidade de Claim |
|---|---|---|---|---|
| Turn-key / EPC | Muito alto | Baixo | Alta | Alta |
| Preço Unitário | Médio | Médio | Média | Média |
| Administração / Cost Plus | Baixo | Alto | Baixa | Baixa |
| Aliança / IPD | Compartilhado | Compartilhado | Baixa | Baixa |

---

## Implicações para Produto: AltoQi Visus Planning

O tipo de contrato determina **o que é relevante mostrar no planejamento** e **para quem**:

| Tipo de Contrato | Stakeholder que mais precisa do planejamento | Dados críticos |
|---|---|---|
| Turn-key / EPC | Gestão da contratada | Avanço físico, interfaces críticas, variações de escopo, gargalos de fornecimento |
| Preço Unitário | Fiscal do dono + contratada | Medições, quantidades executadas, produtividade por item |
| Administração | Dono da obra | Custos reais, horas alocadas, eficiência |
| Aliança / IPD | Todos os parceiros | Painel unificado de risco e desempenho |

**Insight de produto:** Uma ferramenta de planejamento de obra que não considera o tipo de contrato trata todos os stakeholders como iguais — o que leva a dashboards genéricos que servem a nenhum. A configuração de quais métricas são destacadas deve ser adaptável ao modelo contratual do projeto.

---

## Claim Management

**Claim** (ou "reivindicação contratual") é o mecanismo pelo qual uma parte solicita compensação pela outra quando eventos fora do previsto no contrato impactam custo ou prazo. A tipologia e frequência de claims varia diretamente com o tipo de contrato:

- **Turn-key/EPC:** claims por mudança de escopo, differing site conditions, force majeure
- **Preço Unitário:** claims por divergência de quantidades medidas
- **Administração:** claims raramente ocorrem (risco já está com o dono)

---

## Termos Relacionados

- **EPC** — Engineering, Procurement and Construction; variante Turn-key com as três fases (projeto, suprimento, construção) sob responsabilidade única
- **Empreitada Integral** — terminologia brasileira equivalente ao Turn-key; uma única contratada responsável por todo o escopo
- **FIDIC** — conjunto de contratos-padrão internacionais para engenharia civil (Yellow Book = EPC, Red Book = Preço Unitário, Silver Book = Turn-key mais rígido)
- **Differing Site Conditions** — condições de subsolo ou terreno diferentes das indicadas no contrato; causa frequente de claim em EPC
- **Claim Management** — disciplina especializada em identificar, quantificar, documentar e negociar reivindicações contratuais

---

## Related Pages

- [[bim-construction/planejamento-preditivo-obras]] — o que monitorar no planejamento depende do contrato
- [[bim-construction/bim-coordination]] — coordenação de interfaces críticas é mais relevante em contratos EPC/Turn-key
- [[bim-construction/alexander-mattos-contratos-engenharia]] — fonte primária deste conceito
