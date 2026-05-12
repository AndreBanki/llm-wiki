---
title: "ObrasGov (MGI/SERPRO) vs Paraná — Analise Comparativa e Estrategia de Solucao Unica"
type: analysis
created: 2026-05-12
updated: 2026-05-12
sources: [obrasgov-mgi-serpro-workshop-requisitos-2026.md, documento-parana.md, proposta-parana-governanca-obras.md]
tags: [analise-comparativa, obrasgov, parana, mgi, serpro, produto, estrategia, plataforma-unica, compliance, integracoes]
---

# ObrasGov (MGI/SERPRO) vs Parana — Analise Comparativa e Estrategia de Solucao Unica

Comparacao detalhada entre os dois cenarios usando o mesmo framework estrutural do projeto ObrasGov, com foco em decisao de produto para uma plataforma unica capaz de atender contexto federal e estadual, preservando escala de engenharia e reduzindo custo de customizacao.

---

## Tese Central

Os dois projetos compartilham um nucleo funcional fortemente convergente (ciclo de vida da obra, governanca documental, medicao/fiscalizacao, transparencia), mas divergem em duas dimensoes que exigem arquitetura de produto parametrizavel:

1. Arquitetura institucional (federal com execucao direta/indireta e cadeia de parceria vs estadual com governanca UTEA para orgaos internos)
2. Ecossistema de integracoes obrigatorias (TransfereGov/PNCP/CONFEA no federal vs SIM-AM/TCE-PR + TransfereGov + ERP estaduais no Paraná)

Conclusao: viavel construir uma unica solucao, desde que baseada em nucleo comum + policy packs por jurisdicao + adaptadores de integracao + governanca forte de variabilidade para evitar bifurcacao de produto.

Hipotese de valor:

1. O que diferencia os cenarios nao exige reescrever o core, exige parametrizar regras, papeis e conectores.
2. O maior risco nao e funcional, e de proliferacao de customizacao ad hoc.
3. A vantagem competitiva esta em transformar compliance e integracao em capacidade de plataforma.

---

## 1) Modelo Operacional

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Estrutura institucional | Direta + indireta, com cadeia Repassador/Recebedor/Mandataria | Multi-secretarias estaduais com UTEAs e governanca descentralizada | Precisa de motor de ator/papel configuravel por topologia institucional |
| Camada de parceria | Forte dependencia da camada TransfereGov | Integracao TransfereGov requerida para convenios federais | Nucleo deve ser agnostico a camada financeira; conectores tratam regras locais |
| Escopo de encerramento | Fecha no TRP; TRD/prestacao em outra camada | Inclui pos-obra e garantia monitorada por 5 anos | Tratar encerramento e pos-obra como modulos opcionais ativaveis |

Leitura complementar:

- Federal privilegia interoperabilidade entre camadas (tecnica e financeira) com fronteiras bem definidas.
- Paraná amplia o escopo funcional para pos-entrega e monitoramento de garantia, empurrando o produto para lifecycle estendido.
- Uma solucao unica precisa separar fase operacional obrigatoria de capacidades de ciclo estendido ativaveis por pack.

---

## 2) Fases e Macrojornada

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Entrada e formalizacao | F0 Ingresso com ativacao por obra e equipe | Fluxo inicia no DFD e ETP antes de TR e licitacao | Incluir pre-fase de demanda (DFD/ETP) como modulo comum para ambos |
| Planejamento | F1 detalhado com PB, EAP, CFF, snapshots | Exigencia forte de ETP IA + orcamento + cronograma/eventograma | Planejamento deve ter dois modos: PB federal e ETP/TR estadual |
| Licitacao | F2 fora do modulo, com captura de resultado VRPL | Licitacao com analise automatica de planilhas e regras 14.133 | Motor de licitacao precisa suporte a regras parametrizaveis por edital |
| Execucao e medicao | F3 com BM/PLE, glosa e marcos de supervisao | Diario mobile, medicao por eventograma, compliance e aprovacoes | Engine unico de medicao deve suportar BM, PLE e eventograma |
| Reprogramacao | Fluxo transversal formalizado e versionado | Aditivos e reequilibrio tambem criticos | Reprogramacao e versionamento sao nucleo shared, nao customizacao |

Leitura complementar:

- ObrasGov fornece baseline forte para faseamento tecnico da obra.
- Paraná antecipa etapas de demanda e ETP com expectativa de apoio por IA.
- O core deve permitir pre-fase configuravel (DFD/ETP) sem quebrar fases operacionais comuns.

---

## 3) Entidades, Perfis e RBAC

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Perfis base | Operacional, Analista, Gestor | RBAC exigido com trilha de auditoria | Base RBAC comum reutilizavel |
| Perfis tecnicos | Fiscal Tecnico, Supervisor, RT, orgaos de controle | Tecnico fiscal, fiscal de contrato, tecnicos de projeto/orcamento | Precisa de catalogo de perfis por jurisdicao e mapeamento por fase |
| Segregacao de assinatura | Cadeia tecnica formal (RT execucao/fiscalizacao/supervisao) | Aprovacoes bloqueantes e assinatura digital A1 | Camada de assinatura deve ser pluggable (A1, gov stack, provedor externo) |

Leitura complementar:

- A semantica de perfil varia entre cenarios, mas a estrutura de controle de acesso e convergente.
- O produto precisa de um catalogo de papel canônico interno e mapeamentos por jurisdicao.
- Assinatura e aprovacao devem ser modeladas como politica de fase, nao como implementacao fixa.

---

## 4) Artefatos e Governanca Documental

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Catalogo de artefatos | 40 artefatos catalogados no ciclo | Escopo exige artefatos completos (DFD, ETP, TR, medições, laudos) | Criar metamodelo de artefato (tipo, estado, obrigatoriedade, assinante) |
| Versionamento | Snapshots imutaveis de orcamento | Necessidade equivalente em licitacao, aditivos e medicao | Snapshot/versioning deve ser componente central da plataforma |
| Evidencias de campo | Fotos, anexos, vistoria, glosa | Diario georreferenciado e evidencias mobile | Nucleo de evidencias com geoposicionamento e cadeia de custodia |

Leitura complementar:

- O nivel de formalizacao de artefatos no ObrasGov permite transformar governanca em componentes reutilizaveis.
- O Paraná adiciona artefatos de entrada (DFD/ETP/TR) e de pos-obra (laudos/garantia), que podem viver no mesmo metamodelo.
- A decisao correta e padronizar metadados e estados de artefato, variando obrigatoriedade por policy pack.

---

## 5) Integracoes Estruturantes

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Sistemas de governo | TransfereGov, Cadastro, PNCP, CONFEA, SINAPI, Monitora GOV | TransfereGov, SIM-AM/TCE-PR, ERPs estaduais, possivel CREA/CAU | Necessario integration hub com conectores e observabilidade por conector |
| Integracoes financeiras | Camada financeira no TransfereGov | APIs de contratos, aditivos, empenho, pagamento | Contratos financeiros devem ser abstraidos por eventos de negocio |
| Integracao de licitacao | PNCP como alvo principal | Analise de planilhas e importacao de proposta vencedora | Camada de procurement precisa API + regra de conformidade por norma |

Leitura complementar:

- O desenho de integracao deve ser orientado a eventos internos padronizados e nao a chamadas ponto a ponto.
- Cada conector precisa contrato de disponibilidade e estrategia de degradacao.
- O hub de integracao e ativo central para escalar da esfera federal para estadual.

---

## 6) Regras de Negocio e Compliance

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Formalizacao de regra | 78 regras testaveis por fase | Requisitos de POC com 45 criterios/500 pontos | Produto deve ter rule engine parametrico e rastreavel por exigencia |
| Normas centrais | Lei 14.133, LGPD, LAI, TCU/BDI | Lei 14.133, LGPD, LAI, decreto/estrategia BIM Paraná | Core regulatorio comum + pacotes normativos regionais |
| Auditoria | Trilha imutavel e historico integral | Compliance com aprovacoes sequenciais e transparencia | Compliance e auditoria sao diferencial de venda, nao somente requisito |

Leitura complementar:

- Regra de negocio deve ser versionada e rastreavel a dispositivo normativo ou criterio de POC.
- Aderencia precisa ser verificavel em teste automatizado e evidenciavel para auditoria.
- O produto deve oferecer matriz requisito-regra-evidencia para acelerar homologacao.

---

## 7) BIM e Engenharia Digital

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Posicao do BIM | Opcional/progressivo; sistema funciona sem BIM | BIM 2D/3D desktop exigido como parte da solucao | Arquitetura dual-track: modo sem BIM e modo BIM completo |
| Funcionalidades BIM | IFC, IDS, clash, quantitativos, BCF (progressivo) | BIM authoring completo + IFC + quantitativos + memorial | Convergencia favorece stack AltoQi (Eberick + Builder + Visus) |
| Maturidade esperada | Crescente e modulada por capacidade do orgao | Alta desde inicio (exigencia de edital) | Roadmap precisa suportar bootstrap nao-BIM e fast-track BIM |

Leitura complementar:

- O federal demanda dual-track robusto para operar com e sem BIM.
- O Paraná exige stack BIM integrada de partida (authoring + orcamento + execucao).
- A estrategia unica e modularizar capacidades BIM em camadas progressivas, mantendo o fluxo base funcional sem BIM.

---

## 8) Transparencia e Controle Social

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Portal publico | Previsto com dados resumidos e filtros LGPD | Exigido com QR code em placa e acompanhamento detalhado | Portal publico deve ser modulo nativo com niveis de exposicao configuraveis |
| Controle externo | TCU/CGU consulta ampliada | TCE-PR via SIM-AM + transparencia ativa | Integracao com orgaos de controle deve ser tratada como produto core |

Leitura complementar:

- Transparencia nao e apenas UI publica; e pipeline de dados com regras de exposicao.
- Integracoes com controle externo devem ser tratadas como responsabilidade de dominio, nao customizacoes locais.

---

## 9) Modelo de Entrega e Maturidade

| Aspecto | ObrasGov MGI/SERPRO | Paraná (SGSD) | Leitura de Produto |
|---|---|---|---|
| Natureza do escopo | Workshop de requisitos e modelagem de produto | Edital com POC formal, pontuacao e modelo comercial | Plataforma unica precisa suporte a discovery e a certame formal |
| Criticidade de demonstracao | Validação por governanca e integracoes | POC com prova funcional objetiva | Necessaria camada de "demo mode" rastreavel por criterio de POC |

Leitura complementar:

- A plataforma precisa suportar dois regimes comerciais: evolucao por discovery e validacao por prova formal.
- O mecanismo de demonstracao deve apontar diretamente para regras e evidencias do produto.

---

## Mapa de Convergencia (Comum vs Diferenciador)

### Comum de alto valor

- Ciclo de vida de obra estruturado por fases
- Governanca documental e trilha de auditoria
- Medicao, fiscalizacao, glosa e aprovacoes
- Reprogramacao com versoes historicas
- Transparencia publica com limites LGPD
- Integracao com ecossistema governamental

### Diferenciadores por cenario

- Federal: topologia direta/indireta, marcos de supervisao, dependencias fortes de TransfereGov
- Paraná: DFD/ETP com IA, exigencia de modulo BIM desktop pleno, SIM-AM/TCE-PR, pos-obra/garantia de 5 anos

Implicacao de produto:

- O comum deve entrar no core.
- O diferenciador deve entrar em packs.
- O que for conector deve entrar no hub, nunca no core.

---

## Estrategia de Produto para Solucao Unica

### Arquitetura proposta

1. Core Platform (comum)
2. Policy Packs (federal, estadual, municipal)
3. Integration Hub (conectores certificados por ente)
4. Experience Packs (perfil operacional/fiscal/gestor/controle)

Regra de arquitetura:

- Core nao pode conhecer regras locais especificas.
- Policy pack nao pode alterar contrato interno do core.
- Conector nao pode carregar logica de negocio de fase.
- UX pack nao pode suprimir trilha de auditoria obrigatoria.

### 1) Core Platform (imutavel)

- Workflow engine por fase
- Rule engine parametrico
- Artifact engine com versionamento/snapshots
- RBAC + trilha de auditoria
- Motor de medicao multimodal (BM, PLE, eventograma)
- Portal de transparencia modular

Capacidades minimas adicionais:

- baseline manager para comparacao de versoes
- assinatura e aprovacao desacopladas por provedor
- motor de checklist por fase e por papel
- biblioteca de evidencias de conformidade

### 2) Policy Packs (parametrizacao normativa)

- Pack Federal: direta/indireta, marcos, SPA, regras TransfereGov
- Pack Paraná: DFD/ETP/TR, POC mapping, SIM-AM/TCE-PR, pos-obra 5 anos
- Packs futuros: outros estados/municipios com variacao de normativos e controles

Estrutura recomendada de policy pack:

- mapa de fases ativas
- obrigatoriedade de artefatos por fase
- matriz de papeis e assinaturas
- regras de bloqueio/desbloqueio
- pacotes de conformidade normativa

### 3) Integration Hub

- Adaptadores por sistema externo
- Contratos de evento padronizados internos
- Monitoracao de SLA por integracao
- Fallback assincrono com retentativa e reconciliacao

Controles recomendados do hub:

- health check por conector
- fila de reconciliacao por tipo de evento
- trilha de erro classificada por impacto operacional
- simulador de indisponibilidade para testes de resiliencia

### 4) Experience Packs

- Interfaces e jornadas por papel (fiscal, supervisor, gestor, controle)
- Capas de UI orientadas ao contexto (federal/estadual)
- Evidencias guiadas por checklist de conformidade por etapa

Princípio: variar linguagem e fluxo de interface sem variar semantica de dado e governanca.

---

## Proposta de Roadmap Unificado em Fases de Projeto

| Fase | Objetivo | Entregas sugeridas |
|---|---|---|
| Fase 1 - Fundacao do Core | Consolidar capacidades comuns e contratos internos da plataforma | Workflow core por fase, rule engine parametrico, artifact engine com snapshots, RBAC/auditoria, medicao multimodal |
| Fase 2 - Parametrizacao Governamental | Tornar a plataforma configuravel por jurisdicao sem bifurcar codigo | Policy Pack Federal v1, Policy Pack Paraná v1, matriz de artefatos por fase, matriz de papeis/assinaturas por pack |
| Fase 3 - Integracoes e Conformidade Operacional | Conectar ecossistemas externos criticos com resiliencia e rastreabilidade | Integration Hub base, conectores prioritarios (TransfereGov, SINAPI, PNCP, SIM-AM), observabilidade de conectores, reconciliacao assincrona |
| Fase 4 - Certificacao e Escala Multi-Cenario | Provar aderencia em cenarios reais e preparar expansao | Harness de POC por criterio, biblioteca de evidencias de compliance, onboarding de novos packs regionais, modelo de evolucao governado de conectores |

---

## Riscos de Unificacao e Mitigacoes

| Risco | Impacto | Mitigacao |
|---|---|---|
| Customizacao excessiva por cliente | Fragmentacao de produto | Congelar core e forcar extensao via packs |
| Dependencia de integracoes externas | Atrasos e bloqueios | Contrato de eventos interno + filas + retries + monitoracao |
| Divergencia regulatoria crescente | Custos de manutencao | Governanca de policy packs versionados por jurisdicao |
| Sobrecarga de UX por muitos fluxos | Baixa adocao | UX por perfil e contexto, nao por menu unico universal |

Riscos adicionais de produto:

| Risco | Impacto | Mitigacao |
|---|---|---|
| Variacao sem controle entre packs | Divergencia funcional entre clientes | Governanca de policy packs com revisao arquitetural obrigatoria |
| Acoplamento indevido de conector no core | Perda de mantenibilidade | Contrato de extensao estrito e testes de regressao de core |
| Mudanca normativa recorrente | Custo alto de manutencao | Versionamento semantico de regras com trilha de impacto |
| Falta de evidencias para auditoria | Risco comercial e regulatorio | Camada nativa de evidencias e exportacao de trilhas |

---

## Matriz de Decisao Build vs Configure

| Item | Build no Core | Configure em Pack | Conector |
|---|---|---|---|
| Fases base F0-F4 | Sim | Nao | Nao |
| DFD/ETP pre-fase | Nao | Sim | Nao |
| Regras de assinatura A1 | Nao | Sim | Sim (provedor) |
| Integracao TransfereGov | Nao | Parcial (ativacao por pack) | Sim |
| Integracao SIM-AM | Nao | Parcial (ativacao por pack) | Sim |
| Transparencia publica | Sim | Sim (nivel de exposicao) | Parcial |

---

## Conclusao

A convergencia funcional entre ObrasGov e Paraná e suficiente para justificar uma plataforma unica de produto. A divergencia principal nao esta no "o que" fazer, mas em "como" parametrizar governanca, integracoes e compliance por ambiente institucional.

A estrategia recomendada e construir um Product Core Governamental com extensao por Policy Packs e Integration Hub, governando rigorosamente onde cada variacao pode ocorrer. Isso preserva escala de engenharia, reduz retrabalho comercial e posiciona a AltoQi para disputar cenarios federais e estaduais com uma base tecnologica unica, auditavel e comprovavel.

---

## Related Pages

- [[projects/proposta-mgi-serpro-obrasgov]]
- [[projects/proposta-parana-governanca-obras]]
- [[bim-construction/obrasgov-mgi-serpro-workshop-requisitos-2026]]
- [[bim-construction/documento-parana-governanca-obras]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[projects/altoqi-company]]
- [[projects/altoqi-axis]]
