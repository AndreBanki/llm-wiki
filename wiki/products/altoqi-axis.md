---
title: AltoQi Axis
type: product
created: 2026-05-01
updated: 2026-05-01
sources: [Formulário _ Projeto Finep_Axis_2026.pdf]
tags: [altoqi, altoqi-axis, ia, agentes, automação, mcp, plataforma-programável, inteligência-preditiva, aprendizado-contínuo, objetos-dados-inteligentes, construção, produto]
---

Camada de inteligência artificial e automação do ecossistema AltoQi, lançada em 2026. Infraestrutura transversal que integra IA em todos os produtos da plataforma (Eberick, Builder, Visus) — não é um produto independente, é a camada de inteligência que atravessa todo o ecossistema.

---

## O que é

**Definição oficial:** "A infraestrutura de inteligência da construção, desenvolvida com experiências reais e aplicada às decisões do projeto à obra."

> "A construção exige inteligência integrada. Não ferramentas isoladas."

O Axis opera como uma **arquitetura única para toda a cadeia da construção**, eliminando rupturas entre sistemas e garantindo continuidade de dados e coerência decisória em escala. Um único ecossistema estruturado para transformar dados em decisões conectadas, inteligentes e sustentáveis.

---

## Seis Capacidades Centrais

| Capacidade | Descrição |
|---|---|
| **Orquestração de Fluxos de Trabalho** | Conecta regras, modelos e objetos de dados em fluxos operacionais estruturados; dispara ações e recomenda próximos passos com base em contexto e critérios técnicos |
| **Agentes de IA Especializados** | Agentes que apoiam decisões técnicas e operacionais em tempo real sobre dados estruturados — projetos, quantitativos, custos, planejamento, medição e execução. "Ampliando a capacidade técnica e analítica sem substituir o controle humano" |
| **Aprendizado Contínuo** | "Memória estruturada da engenharia à execução." Transforma decisões e padrões de sucesso em inteligência estruturada. "Cada nova obra passa a começar em um nível mais alto de maturidade." O conhecimento dos melhores profissionais evolui em vez de se perder |
| **Objetos de Dados Inteligentes** | Projetos, modelos BIM, contratos, itens orçamentários e medições organizados como objetos conectados e rastreáveis. "Informações técnicas e operacionais deixam de ser registros estáticos e passam a ser ativos inteligentes, prontos para gerar insights e apoiar decisões estratégicas" |
| **Inteligência Preditiva** | Antecipa riscos de prazos, custos e execução com base em padrões consolidados da operação |
| **Plataforma Programável** | Ambiente visual de orquestração com Nodes e MCP para criar automações, regras e fluxos personalizados. "Com Nodes e MCP, especialistas e agentes de IA podem estruturar rotinas inteligentes que conectam projetos, dados e processos" |

---

## Pilares de Design

1. Decisões orientadas por dados estruturados
2. Automação baseada em modelos e agentes
3. Governança e segurança *by design*
4. Previsibilidade operacional com análise preditiva

---

## Integração com o Ecossistema AltoQi

O Axis não é um produto standalone — é a camada de IA que se integra transversalmente a todos os produtos existentes:

### Produtos que o Axis potencializa

| Produto | Função base | Com Axis |
|---|---|---|
| **AltoQi Eberick** | Projeto estrutural em BIM | Verificações automatizadas; agentes especializados para dimensionamento |
| **AltoQi Builder** | Projetos de instalações em BIM | Agentes para detecção de conflitos; automação de rotinas de verificação |
| **AltoQi Visus** | Gestão digital da construção (7 módulos) | Inteligência preditiva, orquestração de fluxos, aprendizado contínuo |

### Integração por módulo Visus

| Módulo Visus | Com Axis |
|---|---|
| **Planning** | Alertas preditivos de risco; automação de sequenciamento |
| **Cost Management** | Objetos de dados inteligentes conectando orçamento a modelo |
| **Tracking** | Medições alimentam aprendizado contínuo |
| **Control Tower** | Dashboards cognitivos com IA preditiva |
| **Workflow** | Orquestração inteligente de processos |
| **Bid** | Agentes especializados para cotação |
| **Collab** | Continuidade de dados entre disciplinas |

---

## Arquitetura Técnica: Seis Componentes (Proposta FINEP 2026)

A proposta de subvenção econômica apresentada à FINEP (2026) descreve o Axis através de seis componentes técnicos, cada um com seu TRL atual e meta. Este framing é complementar — não substituto — às Seis Capacidades Centrais acima: as capacidades descrevem o que o produto entrega ao usuário; os componentes descrevem como ele é construído internamente.

| Comp. | Nome | TRL Atual → Meta |
|---|---|---|
| a | CDE *(Common Data Environment, ISO 19650-alinhado)* | 5→7 |
| b | Motor de Orquestração de Processos BIM | 4→7 |
| c | Plataforma CHECK *(verificação de conformidade BIM com IA)* | 3→7 |
| d | Sistema de Coleta de Informações da Construção | 4→7 |
| e | Ambiente de Entrega da Informação *(Transfere.GOV + Obras.GOV 2.0)* | 4→7 |
| f | Agentes Especializados de IA | 3→7 |

Componentes a–e formam a **camada interna** (estruturação dos dados → fonte única de verdade). Componente f é a **camada externa** (inteligência sobre esses dados → agentes e predição).

Ver detalhes: [[products/altoqi-check]] (Componente c), [[bim-construction/openbim-standards]] (padrões IDS/bSDD que sustentam o Componente c), [[bim-construction/bim-regulatorio-brasil]] (Componente e e o contexto regulatório brasileiro), [[bim-construction/sources/altoqi-finep-axis-2026]]

---

## Modelos de Negócio

| Modelo | Público-alvo |
|---|---|
| **SaaS** | Construtoras e incorporadoras (core) |
| **DaaS** *(Data as a Service)* | Mercado imobiliário, seguradoras, fintechs |
| **AIaaS com gain-sharing** | Grandes construtoras |
| **Plataforma Governamental** | Governo federal / estados |
| **Marketplace** | Ecossistema AEC |

---

## Relevância para o Wiki

O AltoQi Axis materializa, na prática de um produto brasileiro, vários conceitos documentados no wiki:

| Conceito do Wiki | Materialização no Axis |
|---|---|
| Construção 4.0 — processos determinísticos | Objetos de Dados Inteligentes + Orquestração de Fluxos |
| Arquiteto de Soluções — infraestrutura lógica | Plataforma Programável com Nodes e MCP |
| Planejamento preditivo — antevisão via dados | Inteligência Preditiva + Alertas de Risco |
| "Dados como diferencial" (Lazarin) | Aprendizado Contínuo — cada obra eleva a maturidade |
| Ontologia como camada operacional (Palantir) | Objetos de Dados Inteligentes como camada semântica |
| Agentes de IA com governança (wiki AI domain) | Agentes Especializados + governança by design |
| MCP (Model Context Protocol) | MCP explicitamente mencionado na plataforma programável |
| Fio Digital (Digital Thread) | Arquitetura única para toda a cadeia — do projeto à execução sem rupturas |

---

## Metadata

| Campo | Valor |
|---|---|
| Fabricante | AltoQi Tecnologia em Informática |
| Lançamento | 2026 |
| Tipo | Camada de IA transversal (não produto standalone) |
| URL | [lps.altoqi.com.br/axis](https://lps.altoqi.com.br/axis) |
| Produtos integrados | Eberick, Builder, Visus (Cost Management, Planning, Tracking, Control Tower, Workflow, Bid, Collab) |

---

## Related Pages

- [[products/altoqi-visus-planning]] — plataforma de planejamento 4D; principal módulo de gestão potencializado pelo Axis
- [[products/altoqi-check]] — Componente c da arquitetura técnica: verificação de conformidade BIM com IA
- [[products/altoqi-company]] — perfil institucional AltoQi: histórico FINEP, MPS.BR, portfólio
- [[bim-construction/construcao-40]] — paradigma que o Axis materializa como produto comercial
- [[bim-construction/openbim-standards]] — padrões IFC/IDS/BCF/bSDD que sustentam os componentes do Axis
- [[bim-construction/bim-regulatorio-brasil]] — contexto regulatório; Componente e integra com plataformas governamentais
- [[bim-construction/arquiteto-de-solucoes]] — perfil profissional que opera a plataforma programável do Axis
- [[bim-construction/planejamento-preditivo-obras]] — conceito de planejamento preditivo; Axis operacionaliza via Inteligência Preditiva
- [[bim-construction/jhonatan-lazarin-ia-gestao-obras]] — cinco frentes de IA na gestão de obras; Axis cobre todas
- [[bim-construction/eduardo-bandeira-ponte-logica]] — artigo acadêmico sobre Construção 4.0; Axis valida a visão de Bandeira
- [[bim-construction/sources/altoqi-finep-axis-2026]] — proposta FINEP 2026; fonte dos componentes técnicos, TRL e modelos de negócio
- [[ai-engineering/mcp-architecture]] — MCP como protocolo de orquestração; Axis adota MCP na plataforma programável
- [[ai-engineering/ontology-driven-architecture]] — "meaning precedes intelligence"; Objetos de Dados Inteligentes como camada semântica
- [[ai-engineering/ai-agent-governance]] — governança de agentes; Axis adota human-in-the-loop by design
