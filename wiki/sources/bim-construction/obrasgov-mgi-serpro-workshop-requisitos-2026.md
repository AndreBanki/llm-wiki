---
title: "ObrasGov MGI/SERPRO — Workshop de Requisitos do Módulo de Gestão de Obras (2026)"
type: source
created: 2026-05-12
updated: 2026-05-12
source_url: "https://github.com/AndreBanki/obrasgov-docs"
source_type: workshop-docs
author: MGI/DTPAP, SERPRO, AltoQi, S3eng
published: 2026-03-30/2026-04-01
tags: [obrasgov, mgi, serpro, transferegGov, gestao-obras, requisitos, produto-publico, federal, bim, pncp, sinapi, confea, monitora-gov, rbac, reprogramacao]
---

# ObrasGov MGI/SERPRO — Workshop de Requisitos do Modulo de Gestao de Obras (2026)

Extracao estruturada e aprofundada da pasta docs do repositorio obrasgov-docs, com foco no desenho de produto do modulo de Gestao de Obras para contexto federal (MGI/SERPRO), incluindo modelo operacional, regras, integrações e implicações de arquitetura.

---

## Contexto da Fonte

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/AndreBanki/obrasgov-docs |
| Escopo analisado | Pasta docs (fases, escopo, artefatos, perfis, administracao, integracoes, regras de negocio, RNFs) |
| Janela temporal do workshop | 30/03/2026 a 01/04/2026 |
| Abrangencia funcional | F0-F4 + reprogramacao transversal |
| Abrangencia institucional | Execucao direta e indireta (ecossistema ObrasGov + TransfereGov) |

---

## Metodo de Extracao Aplicado

1. Leitura das paginas estruturantes: index, escopo, etapas, artefatos, perfis, administracao, sistemas-integracoes.
2. Leitura dos detalhamentos de fase: F0, F1, F2, F3, F4, reprogramacao e transversais.
3. Leitura dos documentos de produto: regras de negocio, requisitos nao funcionais e requisitos por necessidade.
4. Consolidacao em eixos de produto reutilizaveis para comparacao inter-cenarios.

Critério de sintese: manter terminologia e intencao normativa do material original, priorizando o que impacta decisao de produto, arquitetura e governanca.

---

## Sintese Executiva

O projeto ObrasGov define um modulo de gestao tecnico-fisica de obras publicas acoplado ao ecossistema federal, com separacao explicita entre camada operacional da obra (ObrasGov) e camada juridico-financeira da parceria (TransfereGov). O desenho prioriza rastreabilidade regulatoria, snapshots imutaveis de orcamento, cadeia de assinaturas tecnicas, supervisao por marcos e trilha de auditoria.

O diferencial desta documentacao e a maturidade de engenharia de produto para governo: ha definicao de macrofases, atores, artefatos obrigatorios, regras testaveis por fase e RNFs com status (definido x pendente), reduzindo ambiguidade de escopo.

Framework identificado no material:

1. Modelo operacional (direta vs indireta)
2. Fases e macrofluxo
3. Entidades e perfis
4. Artefatos e estados de aprovacao
5. Integracoes com sistemas estruturantes
6. Regras de negocio testaveis por fase
7. Requisitos nao funcionais e conformidade
8. Transparencia e controle social

---

## Leitura Estrutural Por Documento

### index.md

- Posiciona o modulo como camada de gestao do ciclo de vida completo da obra.
- Explicita fronteira com TransfereGov para dimensao financeira/juridica.
- Estabelece as fases F0-F4 e o fluxo de reprogramacao transversal.

### escopo.md

- Define objeto: desenvolvimento, implantacao e sustentacao do modulo.
- Consolida capacidades minimas: times, documentos, atividades, orcamento, aprovacoes, medicao, supervisao, BIM opcional, auditoria e transparencia.
- Registra exclusoes criticas: TRD e prestacao de contas fora do modulo.

### etapas.md e fases/*

- Detalha entradas, saidas e papeis por fase.
- Formaliza transicao de estado da obra por eventos de aprovacao/assinatura.
- Define onde o sistema atua diretamente e onde apenas integra/sinaliza.

### artefatos.md

- Catalogo operacional de 40 artefatos com rastreabilidade por fase.
- Estrutura de dados orientada a evidencias e compliance.
- Base objetiva para desenho de workflow engine e artifact engine.

### perfis.md + administracao.md

- Clarifica hierarquia de permissao e responsabilidade entre atores.
- Separa fiscal tecnico (operacao de campo) de supervisor (marcos).
- Introduz regras de vinculo institucional e multipla lotacao de usuarios.

### sistemas-integracoes.md

- Mapeia criticidade de integracoes e maturidade (existente, prevista, desejada).
- Evidencia dependencias externas que afetam cronologia de entrega.
- Fundamenta necessidade de integration hub orientado a eventos.

### regras-negocio.md

- Consolida 78 regras testaveis por fase.
- Traduz linguagem de processo para criterios de aceite implementaveis.
- Identifica pre-condicoes bloqueantes (documentos, assinaturas, estados).

### requisitos-nao-funcionais.md

- Lista 66 RNFs, com 40 definidos e 26 pendentes.
- Aponta lacunas para fechamento de arquitetura (SLA, volumetria, performance BIM).
- Explicita que conformidade e observabilidade sao requisitos de primeira ordem.

---

## Aspectos Estruturantes do Projeto ObrasGov

### 1) Modelo Operacional

- Duas trilhas nativas: execucao direta e execucao indireta.
- Na indireta, o modulo opera em conjunto com TransfereGov (parceria, desembolso, aditivos).
- Na direta, o ciclo tecnico ocorre com menos atores e menor dependencia da camada de parceria.
- A cadeias de aprovacao mudam por trilha operacional, exigindo workflow configuravel por tipo de execucao.

### 2) Fases de Processo

- F0 Ingresso
- F1 Planejamento
- F2 Licitacao
- F3 Contratacao/Execucao/Acompanhamento
- F4 Recebimento (TRP)
- Reprogramacao transversal disparavel em F1/F2/F3

Leitura funcional por fase:

- F0: habilita obra e compoe equipes por entidade com base no Modulo de Cadastro.
- F1: consolida projeto basico, validacao tecnica e congelamento de baseline (snapshot estimado).
- F2: captura resultado de licitacao e gera baseline licitado sem executar a licitacao no modulo.
- F3: executa medicao, ateste, glosa e supervisao por marcos com cadeia de assinaturas.
- F4: encerra no TRP e preserva historico em modo somente leitura.
- Reprogramacao: reabre planejamento com comparativo de versoes sem descaracterizar o objeto.

### 3) Entidades e Perfis

- Entidades: Repassador, Recebedor, Contratante, Contratada, Mandataria, Interveniente, Executor.
- Perfis-base RBAC: Operacional, Analista, Gestor.
- Perfis funcionais criticos: Fiscal Tecnico, Supervisor (Mandataria), RT da Contratada, Orgaos de Controle (somente leitura), Administrador do Sistema.
- O desenho de permissao combina hierarquia base e papeis de responsabilidade tecnica, evitando aprovacao sem habilitacao profissional.

### 4) Artefatos e Governanca de Dados

- Catalogo formal com 40 artefatos do ciclo (projeto tecnico, VRPL, CETEF, BM/PLE, glosa, TRP, TA, apostilamento etc.).
- Uso de snapshots imutaveis (orcamento estimado, licitado, reprogramado).
- Cadeia de assinaturas com segregacao de responsabilidade tecnica.
- Trilha de auditoria orientada a orgaos de controle (TCU/CGU) como requisito nativo.

### 5) Integracoes Estruturantes

- Criticas: TransfereGov, Modulo de Cadastro.
- Relevantes: SINAPI, CONFEA (prevista), PNCP (desejada), Monitora GOV (2a etapa), APIs para sistemas de terceiros.
- Regras de integracao orientadas a eventos e retentativa assincrona.

Leitura de prioridade tecnica:

- Bloqueantes de operacao: TransfereGov + Cadastro.
- Bloqueantes de escala e automacao: PNCP + CONFEA + APIs terceiros.
- Bloqueantes de maturidade de campo: integracao com app de vistoria/fiscalizacao.

### 6) Regras de Negocio

- Documento consolidado com 78 regras testaveis por fase.
- Regras chave: bloqueio sem trio OS + ART fiscalizacao + ART execucao, trilha de glosas, marcos de supervisao, vedacao de descaracterizacao do objeto na reprogramacao.
- Regras permitem modelagem de testes de aceite orientados a estado, papel e pre-condicao documental.

### 7) Nao Funcionais e Conformidade

- Conformidade explicita com Lei 14.133/2021, LGPD, LAI, BDI TCU 2622/2013.
- Aderencia ao Gov.br Design System.
- 40 RNFs definidos e 26 pendentes (volumetria, SLAs, performance BIM, acessibilidade completa e dados abertos).

Principais lacunas para fechamento de arquitetura:

- volumetria-alvo de obras e usuarios concorrentes
- SLA de disponibilidade e tempos de resposta
- SLA de processamento BIM (IFC, IDS, clash, extração)
- politicas de retencao e ciclo de vida de dados historicos

### 8) Transparencia Publica

- Portal publico sem autenticacao para dados resumidos de obra.
- Delimitacao clara de dados publicos vs protegidos por LGPD.
- Previsao de evolucao para API de dados abertos e visoes georreferenciadas.

---

## Matriz de Decisoes de Produto Derivadas da Fonte

| Decisao | Evidencia da fonte | Implicacao |
|---|---|---|
| Separar core tecnico da camada financeira | escopo.md + administracao.md | Core reaproveitavel entre entes com conectores diferentes |
| Tratar artefato como objeto de primeira classe | artefatos.md | Necessidade de artifact engine com metadados e status |
| Governar por regra testavel | regras-negocio.md | Rule engine e testes orientados a compliance |
| Operar por trilhas direta/indireta | administracao.md + etapas.md | Workflow parametrico por topologia institucional |
| Preservar baseline historica | F1/F2/reprogramacao | Snapshot service imutavel com comparativo de versoes |
| Priorizar auditoria nativa | perfis.md + RNFs | Logging estruturado e trilha inviolavel |

---

## Implicacoes de Produto

- O projeto ObrasGov ja nasce como produto orientado a regulacao, interoperabilidade e auditabilidade.
- A arquitetura favorece reutilizacao em novos contextos governamentais via parametrizacao de regras, papeis e integracoes.
- A maturidade documental (fases, artefatos, regras, RNFs) permite transformar escopo em backlog verificavel com alta rastreabilidade.
- O material oferece base para uma estrategia de plataforma unica multi-jurisdicao, desde que o core seja mantido estavel e a variacao seja empacotada em policy packs e adaptadores de integracao.

---

## Lacunas Explicitamente Registradas na Fonte

- Definicoes de volumetria e capacidade concorrente em aberto.
- SLAs de performance e disponibilidade sem fechamento formal.
- Integracao PNCP classificada como desejada, nao consolidada.
- Integracao CONFEA prevista, com fase inicial por upload documental.
- Integracao de campo com Monitora GOV classificada para etapa posterior.

Essas lacunas nao invalidam o desenho de produto, mas impactam ordem de implementacao e estrategia de mitigacao de risco tecnico.

---

## Related Pages

- [[projects/proposta-mgi-serpro-obrasgov]]
- [[projects/proposta-parana-governanca-obras]]
- [[analyses/obrasgov-mgi-serpro-vs-parana-estrategia-solucao-unica]]
- [[bim-construction/documento-parana-governanca-obras]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[projects/altoqi-company]]
