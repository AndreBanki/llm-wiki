---
title: Coordenação BIM
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [francieli-wagner-bim-coordination.md]
tags: [bim, coordenação, compatibilização, disciplinas, conflito, modelo-federado]
---

# Coordenação BIM

Processo de integração das disciplinas de projeto (estrutural, hidráulica, elétrica, HVAC, incêndio, etc.) dentro de um ambiente BIM, visando identificar e resolver conflitos antes da execução em obra.

---

## O Problema Central: Disciplinas em Silos

O maior risco em projetos complementares não é técnico — é **cultural**. Cada disciplina tende a agir de forma autônoma, priorizando o que é conveniente para si ("eu cheguei primeiro"), ao invés de otimizar o resultado total do empreendimento.

### Consequências do sequenciamento descontrolado

| Disciplina que "chega primeiro" | Impacto nas demais |
|---|---|
| Elétrica fixa caixas antes | Hidráulica se adapta ao local errado |
| Hidráulica passa dutos antes | Estrutura pode furar laje protendida incorretamente |
| PPCI define trajetos antes | Elétrica coloca quadros em locais caros de executar |

Resultado: retrabalho, atraso e custo de obra sem explicação clara ao incorporador.

---

## A Distinção Fundamental

> "Projeto integrado não é juntar 6 disciplinas no mesmo modelo federado. É ter uma cultura pautada no que realmente importa: o resultado total do empreendimento."
> — Francieli Wagner

| O que NÃO é coordenação BIM real | O que É coordenação BIM real |
|---|---|
| Colocar todas as disciplinas no mesmo modelo federado | Definir sequência de entregas que minimiza retrabalho |
| Cada disciplina defendendo seu território | Responsabilidade pelo resultado total |
| Resolver conflitos reativamente (clash detection) | Antecipar quem precisa do quê e quando |

---

## Pares de Maior Risco de Conflito

Tabela de referência (fonte: PROJETSE, F2-C — Compatibilização e Principais Riscos):

| Par de Disciplinas | Risco | Conflito Típico |
|---|---|---|
| Estrutural × HVAC | ALTO | Reserva de dutos em laje — furo vs. nervura |
| Hidro × Elétrico | ALTO | Shafts e eletrocalhas sobrepostos |
| Estrutural × Hidro | ALTO | Coletores vs. viga baldrame na garagem |
| HVAC × Incêndio | MÉDIO | Dutos e sprinklers no mesmo plenum de forro |
| Elétrico × Estrutural | MÉDIO | Eletrocalha passando em pilar ou cortina |

---

## Princípio de Coordenação

**Regra prática:** em qualquer decisão de sequenciamento de disciplinas, o critério não é quem chegou primeiro no modelo — é **o que resulta no menor custo total para o cliente**.

Isso exige que cada disciplina saiba:
1. **O que** precisa entregar (seus outputs críticos para as demais)
2. **Quando** precisa entregar (para não travar a disciplina seguinte)

---

## Conceitos Relacionados

- **Modelo Federado** — agregação dos modelos individuais de cada disciplina em um único ambiente de visualização. Condição necessária mas não suficiente para coordenação real.
- **Compatibilização** — processo de identificação e resolução de conflitos entre disciplinas. Pode ser feito com clash detection (automatizado) ou revisão manual.
- **Clash Detection** — verificação automatizada de interferências físicas entre elementos de disciplinas distintas.

---

## Knowledge Gaps

- Como estruturar a sequência de entregas entre disciplinas (protocolo de prioridade)?
- Quais ferramentas de coordenação BIM dão suporte ao sequenciamento explícito?
- Casos documentados de impacto financeiro de conflitos não resolvidos em obra.

---

## Related Pages

- [[francieli-wagner-bim-coordination]]
- [[glossary]]
