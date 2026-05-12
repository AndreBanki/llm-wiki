---
title: "Proposta AltoQi — MGI/SERPRO ObrasGov (Gestao de Obras Publicas Federais)"
type: project
created: 2026-05-12
updated: 2026-05-12
sources: [obrasgov-mgi-serpro-workshop-requisitos-2026.md]
tags: [altoqi, mgi, serpro, obrasgov, transferegGov, federal, gestao-obras, produto-publico, lei-14133, rbac, auditabilidade, integracoes]
---

Proposta de enquadramento do projeto ObrasGov (MGI/SERPRO) no portfolio AltoQi, a partir da extracao documental do repositorio obrasgov-docs. O projeto descreve um modulo federal de gestao tecnico-fisica de obras com forte acoplamento regulatorio e de integracao ao ecossistema TransfereGov, com potencial de reutilizacao como base para propostas estaduais.

---

## Objetivo do Projeto

Consolidar uma oferta de produto para o cenario federal (MGI/SERPRO) cobrindo o ciclo operacional da obra publica, da entrada da obra ao recebimento provisório, com rastreabilidade tecnico-regulatoria e interoperabilidade com sistemas estruturantes federais.

Objetivos especificos:

1. Garantir aderencia operacional ao ciclo F0-F4 com reprogramacao transversal.
2. Viabilizar governanca documental e trilha de auditoria orientadas a controle externo.
3. Reduzir operacao manual por integracoes e automacoes de fluxo.
4. Preservar base arquitetural reutilizavel para outros entes governamentais.

---

## Estrutura de Produto Utilizada no ObrasGov

### 1) Modelo Operacional

- Execucao indireta (com parceria e repasse).
- Execucao direta (contratante executa com menor cadeia de atores).
- Separacao de responsabilidades entre camada tecnico-fisica (modulo de obras) e camada juridico-financeira (TransfereGov).

Decisao de produto: tratar tipo de execucao como parametro de fluxo, nao como produto separado.

### 2) Macrofases

- F0 Ingresso
- F1 Planejamento
- F2 Licitacao
- F3 Contratacao/Execucao/Acompanhamento
- F4 Recebimento (TRP)
- Reprogramacao transversal

Entregas operacionais esperadas por macrofase:

- F0: obra ativa no modulo com equipes e papeis atribuídos.
- F1: baseline tecnica aprovada e congelada com trilha de parecer.
- F2: baseline licitada consolidada e comparada com baseline estimada.
- F3: medições registradas, atestadas e supervisionadas conforme trilha de execucao.
- F4: encerramento operacional com TRP e preservacao historica.
- Reprogramacao: nova versao ativa com comparativo rastreavel de alteracoes.

### 3) Papeis e Governanca

- RBAC hierarquico (Operacional, Analista, Gestor).
- Perfis tecnicos especializados (Fiscal Tecnico, Supervisor, RT).
- Segregacao de responsabilidade e cadeia formal de assinaturas por etapa.

Ponto critico: assinatura e aprovacao devem ser acopladas a habilitacao profissional e contexto institucional ativo do usuario.

### 4) Artefatos de Controle

- Catalogo formal de artefatos por fase.
- Snapshots imutaveis de orcamento (estimado, licitado, reprogramado).
- Historico completo para auditoria e controle externo.

Decisao de plataforma: cada artefato precisa metadados padrao (tipo, emissor, estado, validade, assinante, versao) para automacao de regra.

### 5) Integracoes Estruturantes

- TransfereGov e Modulo de Cadastro como espinha dorsal.
- SINAPI ja integrado.
- PNCP e CONFEA como integracoes relevantes para maturidade plena.
- Monitora GOV na trilha de evolucao de campo.

Diretriz de implementacao: integracoes criticas entram no baseline de entrega; integracoes desejadas entram com fallback operacional e eventos pendentes.

### 6) Regras de Negocio

- Regras explicitas e testaveis por fase.
- Tratamento de excecoes como glosas, paralisacoes e reprogramacoes.
- Gatilhos de desbloqueio de fluxo por documentos e assinaturas obrigatorias.

Implicacao tecnica: backlog deve ser estruturado por capability + regra + criterio de aceite mensuravel.

### 7) Nao Funcionais e Compliance

- Lei 14.133/2021, LGPD, LAI, BDI TCU.
- Aderencia Gov.br Design System.
- Governanca de dados e trilha de auditoria como requisito de primeira ordem.

Implicacao tecnica: requisitos nao funcionais devem ser tratados como trilha de entrega dedicada, nao como hardening de fim de projeto.

---

## Escopo Funcional Detalhado da Proposta

### Modulo de ingresso e contexto institucional

- abertura de obra por origem valida
- composicao de times por entidade
- selecao de vinculo institucional ativo
- politicas de acesso por perfil e fase

### Modulo de planejamento tecnico

- cadastro e versionamento de documentacao tecnica
- estruturacao de EAP, orcamento e cronograma
- parecer tecnico e aprovacao formal
- congelamento de baseline estimada

### Modulo de licitacao e consolidacao contratual

- disponibilizacao de base tecnica aprovada
- captura de resultado de licitacao (VRPL)
- comparativo estimado x licitado
- transicao para contratacao operacional

### Modulo de execucao, medicao e fiscalizacao

- medicao em modalidades BM e PLE
- ateste tecnico com trilha de glosa
- supervisao por marcos (quando aplicavel)
- evidencias de campo e anexos comprobatórios

### Modulo de recebimento e fechamento operacional

- emissao de TRP
- bloqueio de novas medições apos encerramento
- preservacao de historico e consulta para auditoria

### Modulo de reprogramacao transversal

- solicitacao, analise e aceite por cadeia hierarquica
- comparativo de versoes de orcamento e cronograma
- ativacao de nova versao sem perder baseline anterior

### Modulo de transparencia publica

- visao resumida de obras por filtros
- exposicao controlada por LGPD
- base para evolucao de dados abertos

---

## Cobertura Funcional Consolidada

| Camada | Cobertura no projeto ObrasGov |
|---|---|
| Planejamento | Projeto basico, orcamento, cronograma, EAP, analise e parecer |
| Licitacao | Disponibilizacao de base tecnica e captura de resultado (VRPL) |
| Execucao | BM/PLE, fiscalizacao, glosa, marcos de supervisao |
| Recebimento | TRP e encerramento operacional |
| Reprogramacao | Fluxo transversal com versoes e comparativos |
| Transparencia | Consulta publica resumida com filtros LGPD |

---

## Arquitetura de Referencia Proposta

1. Workflow Core: orquestra estados e transicoes por fase e tipo de execucao.
2. Artifact Core: gere artefatos, versoes e snapshots imutaveis.
3. Rule Core: aplica regras de negocio parametrizadas e auditaveis.
4. Identity and Access Core: aplica RBAC e restricoes por vinculo institucional.
5. Integration Hub: conecta sistemas externos por eventos e APIs.
6. Transparency Core: publica visoes externas com filtros de exposicao.

Princípios arquiteturais:

- separacao de core e adaptadores
- configuracao por policy pack
- observabilidade de ponta a ponta
- auditabilidade by default
- degradacao controlada em falha de integracao

---

## Gaps e Pontos de Atencao

- Integracao PNCP ainda tratada como demanda desejada.
- Integracao CONFEA prevista, com MVP via upload de ART.
- Parte relevante de RNFs ainda sem SLA/volumetria formal.
- Integracao de app de campo com parcerias federais em segunda etapa.

Riscos adicionais:

- dependencia de servicos externos para continuidade de fluxo
- variacao de maturidade digital entre orgaos executores
- risco de sobrecarga operacional se UX nao refletir cadeia real de papeis

---

## Implicacao Estrategica para AltoQi

O projeto ObrasGov evidencia um padrao de produto governamental orientado a:

1. Compliance-by-design
2. Integracao-by-design
3. Auditabilidade-by-design

Esse padrao e reutilizavel para outras propostas governamentais (como o caso Paraná), desde que a plataforma tenha um nucleo comum robusto e camadas parametrizaveis por jurisdicao/integracao.

Posicionamento sugerido:

1. Produto gov-first com compliance explicito e comprovavel.
2. Plataforma unica com extensoes por cenario institucional.
3. Diferenciacao por rastreabilidade, integracao e capacidade de operacao multi-ente.

---

## Criterios de Sucesso da Proposta

| Dimensao | Criterio |
|---|---|
| Aderencia funcional | Cobertura integral das fases F0-F4 e reprogramacao |
| Governanca | Rastreabilidade completa de artefatos, decisoes e assinaturas |
| Integracao | Operacao estavel com sistemas estruturantes prioritarios |
| Operacao | Reducao de retrabalho manual na fiscalizacao e analise |
| Escalabilidade institucional | Capacidade de aplicar o mesmo core em novos entes |

---

## Related Pages

- [[bim-construction/obrasgov-mgi-serpro-workshop-requisitos-2026]]
- [[projects/proposta-parana-governanca-obras]]
- [[analyses/obrasgov-mgi-serpro-vs-parana-estrategia-solucao-unica]]
- [[bim-construction/documento-parana-governanca-obras]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[projects/altoqi-axis]]
- [[projects/altoqi-visus-planning]]
