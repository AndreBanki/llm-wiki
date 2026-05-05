---
title: "Projeto FINEP — Axis \"Mais Inovação Brasil\" 2026"
type: project
created: 2026-05-05
updated: 2026-05-05
sources: [Formulário _ Projeto Finep_Axis_2026.pdf]
tags: [altoqi, finep, subvenção-econômica, mais-inovação-brasil, p&d, altoqi-axis, altoqi-check, altoqi-visus, trl, construção-4.0, bim, openbim, ia, agentes-ia, proposta]
---

# Projeto FINEP — Axis "Mais Inovação Brasil" 2026

Proposta de subvenção econômica submetida ao programa **FINEP/MCTI "Mais Inovação Brasil"**, Linha 4 — Moradia e Espaços Públicos Sustentáveis. O projeto formaliza a evolução tecnológica do **AltoQi Axis** como plataforma de inteligência da construção, estruturada em seis componentes técnicos com progressão de TRL 2 → 7.

> Esta página documenta a **proposta de projeto** — escopo, arquitetura, roadmap e contexto. Para a descrição AS-IS de cada linha de produto envolvida, ver as páginas de produto referenciadas abaixo.

---

## Contexto do Programa

| Campo | Valor |
|---|---|
| **Programa** | Mais Inovação Brasil (FINEP/MCTI) |
| **Linha** | Linha 4 — Moradia e Espaços Públicos Sustentáveis |
| **Instrumento** | Subvenção Econômica |
| **Proponente** | AltoQi Tecnologia em Informática |
| **Ano de submissão** | 2026 |
| **Documento formal** | Formulário de Apresentação de Proposta (FAP) — 42 páginas |
| **Fonte primária** | [[bim-construction/altoqi-finep-axis-2026]] |

---

## Problema Central

**"Baixa capacidade de aprendizagem operacional"** — dados de cada obra permanecem dispersos; decisões não retroalimentam projetos futuros; cada obra começa do zero.

A raiz técnica do problema: o BIM está concentrado nas fases iniciais do empreendimento (concepção e projeto), com adoção ainda baixa nas fases de construção e operação. Consequência: a informação não acompanha o ciclo de vida completo, criando um abismo entre o modelo virtual e a execução física.

Diagnóstico de base do FAP: o projeto não trata apenas de automatizar tarefas isoladas, mas de construir a infraestrutura de dados e interoperabilidade que permite transformar execução de obra em aprendizagem acumulada.

Ver: [[bim-construction/planejamento-preditivo-obras]], [[bim-construction/construcao-40]]

---

## Linhas de Produto Envolvidas

O projeto não é circunscrito a um único produto — ele propõe a evolução coordenada de três linhas de produto AltoQi, além da infraestrutura transversal do Axis:

| Linha de Produto | Papel no Projeto | TRL (componente) | Página AS-IS |
|---|---|---|---|
| **AltoQi Axis — CDE + Orquestração** | Infraestrutura central: repositório de dados + orquestração de workflows BIM (Componentes a e b) | 5→7 / 4→7 | [[projects/altoqi-axis]] |
| **Plataforma CHECK** | Verificação automatizada de conformidade BIM com IA; maior salto de TRL do projeto (Componente c) | 3→7 | [[projects/altoqi-check]] |
| **AltoQi Visus Planning / Coleta / Entrega** | Coleta de dados de campo e integração com plataformas governamentais (Componentes d e e) | 4→7 / 4→7 | [[projects/altoqi-visus-planning]] |
| **Agentes Especializados de IA** | Camada de inteligência sobre os dados estruturados dos demais componentes (Componente f) | 3→7 | [[projects/altoqi-axis]] |

---

## Arquitetura de Solução: Seis Componentes

A solução é estruturada em duas camadas arquiteturais. Esse framing é central para a leitura correta da proposta: os componentes não são módulos independentes, mas partes de um fluxo em que dados estruturados vêm primeiro e inteligência vem depois.

| Camada | Função | Resultado esperado |
|---|---|---|
| **Interna (a-e)** | Estruturação inteligente dos dados, interoperabilidade e governança | Fonte única de verdade para projeto, obra, conformidade e gestão |
| **Externa (f)** | Operação de agentes especializados de IA sobre a base estruturada | Alertas preditivos, automação de rotinas e aprendizado contínuo entre obras |

| Comp. | Nome | TRL Atual → Meta | Descrição |
|---|---|---|---|
| **a** | CDE *(Common Data Environment)* | 5→7 | Repositório central ISO 19650-alinhado; gestão de versões, workflows de aprovação, integração com modelos IFC |
| **b** | Motor de Orquestração de Processos BIM | 4→7 | Orquestração de workflows multi-stakeholder; gatilhos automáticos por marcos do cronograma; usa BCF para issues vinculados a objetos do modelo |
| **c** | Plataforma CHECK | 3→7 | Verificação de conformidade BIM com IA; usa IDS e bSDD para validação automática contra requisitos do projeto |
| **d** | Sistema de Coleta de Informações da Construção | 4→7 | Coleta de dados de campo (formulários, fotos, IoT) vinculada ao modelo BIM; fecha o loop entre execução e modelo |
| **e** | Ambiente de Entrega da Informação | 4→7 | Dashboards de gestão + integração com plataformas governamentais (Transfere.GOV + Obras.GOV 2.0) |
| **f** | Agentes Especializados de IA | 3→7 | Operam sobre dados estruturados dos demais componentes para geração de insights, alertas preditivos e automação de rotinas |

### Leitura da Proposta: Componentes de P&D vs. Capacidades de Produto

O FAP descreve o projeto em **seis componentes técnicos** porque o objetivo do documento é demonstrar escopo de P&D, evolução de maturidade e redução de risco tecnológico. Isso não substitui a leitura de produto do Axis, que aparece no wiki como **seis capacidades** voltadas à proposta de valor e ao posicionamento comercial.

As duas leituras são complementares:

- **Capacidades** respondem "o que a plataforma entrega ao mercado".
- **Componentes** respondem "o que precisa ser desenvolvido, integrado e validado para entregar isso com TRL 7".

---

## Roadmap Sistêmico de TRL (2→7)

Além dos TRLs por componente, o enquadramento sistêmico trata o Axis como solução integrada que parte de TRL 2 e chega a TRL 7 ao final do projeto. A progressão é orientada por redução de risco tecnológico e evidência operacional a cada etapa.

### TRL 2 → 3 — Consolidação de Arquitetura
Consolidar a arquitetura integrada e eliminar ambiguidades de escopo técnico. Inclui definição de requisitos críticos, priorização de casos de uso de maior impacto e estabelecimento de base semântica comum com padrões openBIM (IFC, IDS, BCF, bSDD). Os experimentos nascem já integráveis ao sistema futuro.

### TRL 3 → 4 — Protótipos Funcionais em Laboratório
Provas de conceito convertidas em protótipos funcionais validados com dados sintéticos e históricos anonimizados. Métricas de desempenho definidas. Foco: acurácia, latência e estabilidade mínimas antes de exposição a cenários operacionais variáveis.

### TRL 4 → 5 — Integração e Validação em Ambiente Relevante
Módulos integrados em fluxo único e validados em ambiente representativo de obra real. Mitigação de risco via robustez de interoperabilidade openBIM, governança de dados por versionamento e auditoria, e qualificação contínua das entradas.

### TRL 5 → 6 — Demonstração Contínua em Pilotos Ampliados
Pilotos com funções críticas operando de forma contínua: atualização de dados de campo, verificação automatizada de conformidade, alertas preditivos e acionamento de workflows por eventos do cronograma. Monitoramento por indicadores técnicos e operacionais.

### TRL 6 → 7 — Protótipo Sistêmico em Ambiente Operacional Real
Sistema demonstrado com uso por perfis efetivos (engenharia, planejamento, gestão, conformidade) e integração com sistemas corporativos e plataformas governamentais. Comprovação por repetibilidade entre projetos e ganhos mensuráveis em previsibilidade, tempo de resposta, redução de retrabalho e confiabilidade da informação.

---

## Modelos de Negócio

| Modelo | Público-alvo | Descrição |
|---|---|---|
| **SaaS** | Construtoras e incorporadoras | Subscrição por usuário/projeto; core do produto |
| **DaaS** *(Data as a Service)* | Mercado imobiliário, seguradoras, fintechs | Dados anonimizados de desempenho de obras |
| **AIaaS com gain-sharing** | Grandes construtoras | Compartilhamento de ganhos gerados por inteligência preditiva |
| **Plataforma Governamental** | Governo federal / estados | Infraestrutura de gestão e monitoramento de obras públicas |
| **Marketplace** | Ecossistema AEC | Integrações de terceiros sobre a plataforma Axis |

---

## Padrões openBIM Adotados

Os padrões openBIM não aparecem no FAP como detalhe de interoperabilidade apenas. Eles funcionam como a base técnica que torna verificável, auditável e escalável a proposta.

| Padrão | Papel no Projeto | Componente mais diretamente dependente |
|---|---|---|
| **IFC** *(Industry Foundation Classes)* | Formato de troca e estruturação de modelos entre disciplinas e sistemas; base da interoperabilidade do ecossistema | **a** CDE / **d** Campo / **e** Entrega |
| **IDS** *(Information Delivery Specification)* | Especifica formalmente o que deve ser entregue em cada fase; transforma requisito de informação em regra verificável | **c** CHECK |
| **BCF** *(BIM Collaboration Format)* | Encapsula issues, comentários e viewpoints vinculados aos objetos do modelo; suporta workflows multi-stakeholder | **b** Orquestração |
| **bSDD** *(buildingSMART Data Dictionary)* | Dicionário de propriedades para validação semântica e conformidade | **c** CHECK |

Sem esse cluster openBIM, a proposta perderia a capacidade de conectar projeto, execução, conformidade e inteligência em um fluxo único.

---

## Ancoragem Regulatória

| Instrumento | Ano | Relevância |
|---|---|---|
| **Estratégia BIM BR** | 2018 | Política nacional de BIM; o projeto alinha-se às metas de digitalização até 2028 |
| **Decreto 10.306/2020** | 2020 | Obrigatoriedade progressiva de BIM em obras federais; abre mercado de governo para Componente e |
| **Lei 14.133/2021, art. 19** | 2021 | Nova Lei de Licitações: BIM previsto nas contratações públicas |
| **LGPD** | 2018 | Privacidade by design; modelos DaaS e AIaaS dependem de conformidade |
| **ISO 19650** | — | Gestão de informação BIM; CDE (Componente a) alinhado à norma |

Ver: [[bim-construction/bim-regulatorio-brasil]], [[bim-construction/openbim-standards]]

---

## Mapa Competitivo

| Segmento | Competidores | Diferencial Axis |
|---|---|---|
| CDE | Autodesk Construction Cloud, Bentley ProjectWise, Trimble Connect, BIMcloud | Integração nativa com ferramentas AltoQi + foco Brasil |
| Coordenação de modelos | Solibri, Revizto, BIMcollab | CHECK com IA (não apenas clash detection) |
| Gestão de execução | Procore, Oracle Aconex | Pipeline completo do projeto à execução; aprendizado contínuo por obra |
| IA Generativa AEC | Autodesk Forma | Dados de obras reais da base instalada AltoQi como vantagem de treinamento |

---

## Related Pages

- [[projects/altoqi-company]] — perfil institucional e histórico FINEP do proponente
- [[projects/altoqi-axis]] — linha de produto Axis: AS-IS e visão (Componentes a, b, f)
- [[projects/altoqi-check]] — Plataforma CHECK: AS-IS e visão (Componente c)
- [[projects/altoqi-visus-planning]] — Visus Planning: AS-IS e visão (Componentes d, e)
- [[projects/mpd-visus-evolucao-plataforma]] — proposta aplicada de evolução do Visus em cliente enterprise; valida o eixo procurement + gestão contratual de execução
- [[bim-construction/altoqi-finep-axis-2026]] — fonte primária: FAP completo (42 páginas)
- [[bim-construction/visus-evolucao-mpd-analise-produto]] — análise operacional detalhada da MPD que complementa o framing do FAP no nível de fluxo de obra
- [[bim-construction/construcao-40]] — paradigma que o projeto materializa
- [[bim-construction/planejamento-preditivo-obras]] — problema central abordado
- [[bim-construction/openbim-standards]] — padrões IFC/IDS/BCF/bSDD que sustentam os componentes
- [[bim-construction/bim-regulatorio-brasil]] — contexto regulatório brasileiro
