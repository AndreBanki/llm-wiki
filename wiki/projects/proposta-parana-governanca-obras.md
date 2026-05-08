---
title: "Proposta AltoQi — Edital Governança de Obras Públicas do Paraná"
type: project
created: 2026-05-08
updated: 2026-05-08
sources: [documento_parana.md]
tags: [altoqi, paraná, obras-públicas, governança, licitação, edital, governo-estadual, visus, eberick, builder, bim, lei-14133, poc, utea, sim-am, transferegov, estratégia-bim-paraná]
---

Proposta da AltoQi para edital publicado pelo Governo do Estado do Paraná (SGSD) visando à contratação de plataforma integrada de gestão de obras públicas para 11 secretarias e órgãos estaduais. Primeira oportunidade de contrato governamental estadual documentada no wiki.

---

## Contexto do Edital

O Governo do Estado do Paraná publicou um Pregão Eletrônico para contratação de solução de software para governança de obras públicas, a ser implantada em todas as secretarias que executem obras (início com 11 entidades: DETRAN/PR, SECID/AMEP, SEIL/DER, IAT, IDR Paraná, SEED/FUNDEPAR, SESA/FUNEAS, SESP, SEJU, SEDEF, SEES).

**Decreto-base:** O Decreto Estadual nº 10.585/2025 criou o GT Obras Públicas e as UTEAs (Unidades Técnicas de Engenharia e Arquitetura), que estruturam o modelo de governança descentralizado que a solução deverá apoiar.

**Âncoras regulatórias:**
- Lei 14.133/2021 (Nova Lei de Licitações) — fluxo DFD → ETP → TR obrigatório
- Estratégia BIM Paraná + Decreto Estadual nº 10.086/2022 — adoção progressiva de BIM nas obras públicas estaduais, R$ 55M de investimento 2025-2026
- Transferegov — integração obrigatória para convênios federais
- SIM-AM TCE-PR — prestação de contas ao Tribunal de Contas do Estado

**Vigência:** 24 meses.

---

## Escopo Funcional Exigido

A solução exigida abrange o ciclo completo da obra pública:

| Etapa | Módulo/Ferramenta |
|---|---|
| DFD → ETP → TR | Módulo de solicitações (Kanban, timeline, DFD gerador de ETP) |
| Projeto BIM 2D/3D | Desktop: arquitetura, estrutura, elétrico, hidráulico, PPCI; IFC in/out |
| Orçamento | Referências de custo integradas (SINAPI/SICRO/CEF); eventograma; DMT |
| ETP | 12 tópicos art. 18 Lei 14.133/2021; IA integrada para validação e correção |
| Licitação | Planilha para licitantes; análise automática conforme Lei 14.133/2021 |
| Contratação | Integração via API (contratos, aditivos, empenhos, financeiro) |
| Execução | Diário de obras (mobile, georreferenciado, offline-sync); medição por eventos do eventograma |
| Fiscalização | BM digital; compliance (aprovações sequenciais bloqueantes); assinatura A1 |
| Transparência | Portal público de obras (QR Code na placa); georreferenciamento |
| Pós-obra | Laudo final; garantia monitorada por 5 anos via mobile |
| Prestação de contas | Exportação SIM-AM TCE-PR; integração Transferegov |

---

## Modelo Comercial do Edital

| Item | Quantidade | Tipo |
|---|---|---|
| Licença Perpétua 2D/3D BIM | 50 | Desktop (inclui Eberick + Builder + integração) |
| Licença Perpétua WEB | 1 | Estado inteiro do Paraná |
| Implantação | 1 | — |
| Treinamento | 16 módulos | ≥ 40h/módulo, ilimitado de usuários |
| Hospedagem em Nuvem | 24 meses | — |

---

## POC — Prova de Conceito (45 Critérios / 500 pontos)

A POC é o mecanismo formal de qualificação técnica no certame. Avalia maturidade técnica e aderência à solução. Resumo por bloco:

| Bloco | Critérios | Pontos |
|---|---|---|
| Solicitações / DFD / ETP | 1–12 | 155 |
| Projeto BIM 2D/3D | 13–15 | 50 |
| Engenharia WEB (orçamento, licitação, contratos) | 16–28 | 115 |
| Execução / medição / compliance | 29–43 | 165 |
| Pós-obra e gestão | 44–45 | 15 |

Detalhamento completo: [[bim-construction/documento-parana-governanca-obras]] (Seção 15).

---

## Tensão Estratégica para AltoQi

O edital exige **módulo de desenho 2D/3D BIM como parte da mesma solução**. A AltoQi possui:
- Eberick: projeto estrutural BIM
- Builder: instalações BIM (hidráulico, elétrico, PPCI)
- Visus: gestão WEB/mobile de obras

A proposta AltoQi **pode incluir o ecossistema completo** (Eberick + Builder + Visus), respondendo ao escopo integral. Isso diferencia da concorrência que pode oferecer apenas a camada WEB com IFC de terceiros.

---

## Diferenciais Relevantes da AltoQi

- **MPS.BR Nível F:** pré-requisito de conformidade para contratos governamentais federais
- **Histórico FINEP:** valida capacidade de execução e prestação de contas em contratos públicos
- **openBIM nativo:** Eberick e Builder exportam IFC; alinhados com Estratégia BIM Paraná
- **Transferegov:** já documentado no portfólio de integrações FINEP/Axis
- **Visus módulos:** Planning, Cost Management, Tracking, Control Tower, Workflow, Bid, Collab — cobertura ampla do fluxo exigido

---

## Gaps a Verificar

- **SIM-AM TCE-PR:** integração com o tribunal de contas estadual — verificar se já existe ou precisa ser desenvolvida
- **Eventograma nativo no Visus:** verificar se a medição por eventos do eventograma está disponível hoje
- **Assinatura A1 integrada:** módulo próprio de assinatura digital — verificar cobertura atual
- **Portal público de obras (QR Code):** funcionalidade de transparência pública — verificar roadmap
- **Mobile offline-sync:** diário de obras com sincronização offline — verificar maturidade atual

---

## Related Pages

- [[bim-construction/documento-parana-governanca-obras]]
- [[projects/altoqi-visus-planning]]
- [[projects/altoqi-axis]]
- [[projects/altoqi-company]]
- [[projects/finep-mais-inovacao-brasil-2026]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[bim-construction/openbim-standards]]
