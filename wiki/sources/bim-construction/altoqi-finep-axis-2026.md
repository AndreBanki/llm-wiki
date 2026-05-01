---
title: "AltoQi Axis — Formulário de Apresentação de Proposta FINEP 2026"
type: source
created: 2026-05-01
updated: 2026-05-01
source_url: https://docs.google.com/document/d/1jOValoo1mQn_ZsdjJX3a3hbLK1OCU4zC/edit#heading=h.sksfp4x72nyr
source_type: grant-application
author: AltoQi Tecnologia em Informática
published: 2026
pages: 42
tags: [altoqi, altoqi-axis, finep, subvenção-econômica, construção-4.0, bim, cde, openbim, iso-19650, ids, bsdd, agentes-ia, trl, regulatório, mpsbr, mais-inovação-brasil]
---

# AltoQi Axis — Formulário de Apresentação de Proposta FINEP 2026

Formulário de Apresentação de Proposta (FAP) submetido ao programa FINEP/MCTI **"Mais Inovação Brasil"**, Linha 4 – Moradia e Espaços Públicos Sustentáveis. Documento técnico formal (42 páginas) com profundidade inédita: TRL por componente, análise de mercado, mapa competitivo, estratégia de scale-up, modelos de negócio e histórico institucional — nenhum desses elementos aparece nas fontes públicas sobre o Axis.

**URL original:** [Formulário _ Projeto Finep_Axis_2026](https://docs.google.com/document/d/1jOValoo1mQn_ZsdjJX3a3hbLK1OCU4zC/edit#heading=h.sksfp4x72nyr)

---

## Problema Central

**"Baixa capacidade de aprendizagem operacional"** — dados de cada obra permanecem dispersos; decisões não retroalimentam projetos futuros; cada obra começa do zero.

Diagnóstico de base (citando publicação Springer): o BIM está concentrado nas fases iniciais (concepção e projeto), com adoção ainda baixa nas fases de construção e operação. Consequência: a informação não acompanha o ciclo de vida completo do empreendimento, criando um abismo entre o modelo virtual e a execução física.

---

## Arquitetura de Solução: Duas Camadas

| Camada | Função | Resultado |
|---|---|---|
| **Interna** | Estruturação inteligente dos dados → fonte única de verdade | CDE como hub central; todos os componentes alimentam e consultam o mesmo repositório |
| **Externa** | Agentes de IA personalizados com aprendizado contínuo | Inteligência preditiva por obra; cada obra eleva a maturidade do sistema |

---

## Seis Componentes Técnicos

| Comp. | Nome | TRL Atual → Meta | Descrição |
|---|---|---|---|
| a | **CDE** *(Common Data Environment)* | 5→7 | Repositório central ISO 19650-alinhado; gestão de versões, workflows de aprovação, integração com modelos IFC |
| b | **Motor de Orquestração de Processos BIM** | 4→7 | Orquestração de workflows multi-stakeholder; gatilhos automáticos por marcos do cronograma; usa BCF para issues vinculados a objetos do modelo |
| c | **Plataforma CHECK** | 3→7 | Verificação de conformidade BIM com IA; usa IDS e bSDD para validação automática contra requisitos do projeto; TRL de maior salto |
| d | **Sistema de Coleta de Informações da Construção** | 4→7 | Coleta de dados de campo (formulários, fotos, IoT) vinculada ao modelo BIM; fecha o loop entre execução e modelo |
| e | **Ambiente de Entrega da Informação** | 4→7 | Dashboards de gestão + integração com plataformas governamentais (Transfere.GOV + Obras.GOV 2.0) |
| f | **Agentes Especializados de IA** | 3→7 | Operam sobre dados estruturados dos demais componentes para geração de insights, alertas preditivos e automação de rotinas |

**Nota arquitetural:** Componentes a–e formam a camada interna (dados estruturados → fonte única de verdade). Componente f é a camada externa (inteligência sobre esses dados).

---

## Modelos de Negócio Planejados

| Modelo | Público-alvo | Descrição |
|---|---|---|
| **SaaS** | Construtoras e incorporadoras | Subscrição por usuário/projeto; core do produto |
| **DaaS** *(Data as a Service)* | Mercado imobiliário, seguradoras, fintechs | Dados anonimizados de desempenho de obras |
| **AIaaS com gain-sharing** | Grandes construtoras | Compartilhamento de ganhos gerados por inteligência preditiva |
| **Plataforma Governamental** | Governo federal / estados | Infraestrutura de gestão e monitoramento de obras públicas |
| **Marketplace** | Ecossistema AEC | Integrações de terceiros sobre a plataforma Axis |

---

## Padrões openBIM Adotados

| Padrão | Organismo | Uso no Axis |
|---|---|---|
| **IFC** *(Industry Foundation Classes)* | buildingSMART | Formato de troca de modelos entre disciplinas e sistemas; obrigatório pelo Decreto 10.306/2020 |
| **IDS** *(Information Delivery Specification)* | buildingSMART | Plataforma CHECK: define o que deve ser entregue em cada fase do projeto |
| **BCF** *(BIM Collaboration Format)* | buildingSMART | Motor de Orquestração: issues e comentários vinculados a objetos do modelo |
| **bSDD** *(buildingSMART Data Dictionary)* | buildingSMART | Plataforma CHECK: dicionário de propriedades para verificação de conformidade |

Ver: [[bim-construction/openbim-standards]]

---

## Ancoragem Regulatória Brasileira

| Instrumento | Ano | Relevância para Axis |
|---|---|---|
| **Estratégia BIM BR** | 2018 | Política nacional de BIM; Axis alinha-se às metas de digitalização até 2028 |
| **Decreto 10.306/2020** | 2020 | Obrigatoriedade progressiva de BIM em obras federais; abre mercado de governo para Componente e |
| **Lei 14.133/2021, art. 19** | 2021 | Nova Lei de Licitações: BIM previsto nas contratações públicas |
| **LGPD** | 2018 | Privacidade by design; modelos DaaS e AIaaS dependem de conformidade com LGPD |
| **ISO 19650** | — | Padrão internacional de gestão de informação BIM; CDE (Componente a) alinhado à 19650 |

Ver: [[bim-construction/bim-regulatorio-brasil]]

---

## Mapa Competitivo

| Segmento | Competidores | Diferencial Axis |
|---|---|---|
| CDE | Autodesk Construction Cloud, Bentley ProjectWise, Trimble Connect, BIMcloud | Integração nativa com ferramentas de projeto AltoQi (Eberick, Builder) + foco Brasil |
| Coordenação de modelos | Solibri, Revizto, BIMcollab | Plataforma CHECK com IA (não apenas clash detection) |
| Gestão de execução | Procore, Oracle Aconex | Pipeline completo do projeto à execução; aprendizado contínuo por obra |
| IA Generativa AEC | Autodesk Forma | Dados de obras reais de 70.000+ clientes como vantagem de treinamento |

---

## Perfil Institucional AltoQi (Resumo)

Ver página completa: [[products/altoqi-company]]

| Indicador | Valor |
|---|---|
| Anos de mercado | 37+ |
| Clientes ativos Visus | 10.000+ |
| Clientes totais históricos | 70.000+ |
| Certificação de processo | MPS.BR nível F (desde 2016) |
| Metodologia | SAFe agile + CI/CD |
| Histórico FINEP | AMPEG (1990s), PAPPE, Redes FINEP, Subvenção 2007 (~R$1,8M) |
| Prêmio | Premio FINEP Inovação Tecnológica 1999 (Eberick) |

---

## Delta em Relação ao Wiki Existente

### Adiciona
- Nome formal do problema: "baixa capacidade de aprendizagem operacional" (não existia no wiki)
- Seis componentes técnicos com TRL (distinto das "6 capacidades" de marketing de [[products/altoqi-axis]])
- Dois novos modelos de negócio: DaaS e AIaaS com gain-sharing
- Cluster openBIM: IDS, BCF, bSDD (IFC existia na wiki só como menção)
- Contexto regulatório brasileiro completo: Estratégia BIM BR, Decreto 10.306, Lei 14.133
- Brecha de ciclo de vida: BIM concentrado em fases iniciais, baixa adoção na construção/operação
- AltoQi como instituição: 37+ anos, histórico FINEP, MPS.BR

### Reforça
- Construção 4.0 / CDE / Fio Digital ([[bim-construction/construcao-40]])
- Planejamento preditivo como antídoto para o "zero reset" a cada obra ([[bim-construction/planejamento-preditivo-obras]])
- Axis como materialização da Construção 4.0 ([[products/altoqi-axis]])

### Reconcilia
- Dois framings do Axis: "6 capacidades" (marketing/produto) e "6 componentes" (P&D/FINEP) — complementares, diferentes audiências, ambos válidos

---

## Related Pages

- [[products/altoqi-axis]]
- [[products/altoqi-check]]
- [[products/altoqi-company]]
- [[products/altoqi-visus-planning]]
- [[bim-construction/construcao-40]]
- [[bim-construction/planejamento-preditivo-obras]]
- [[bim-construction/openbim-standards]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[bim-construction/eduardo-bandeira-ponte-logica]]
