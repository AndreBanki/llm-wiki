---
title: "AltoQi Axis — Plataforma CHECK"
type: product
created: 2026-05-01
updated: 2026-05-01
sources: [Formulário _ Projeto Finep_Axis_2026.pdf]
tags: [altoqi, altoqi-axis, plataforma-check, conformidade-bim, ids, bsdd, verificação-automática, trl, openbim, ia, construção]
---

# Plataforma CHECK

Componente **c** do AltoQi Axis: plataforma de verificação automatizada de conformidade BIM com inteligência artificial. Opera sobre padrões openBIM — IDS (Information Delivery Specification) e bSDD (buildingSMART Data Dictionary) — para validar se modelos entregues satisfazem os requisitos de informação especificados para o projeto.

**TRL atual → meta:** 3 → 7 (o componente de maior salto de maturidade no projeto Finep 2026)

---

## O Problema que Resolve

Hoje, a verificação de conformidade de modelos BIM é feita manualmente por coordenadores que abrem o modelo, navegam pelas disciplinas e verificam elemento a elemento se as propriedades exigidas estão presentes e corretas.

Esse processo:
- É lento (dias de trabalho por disciplina em projetos médios)
- É subjetivo (depende do analista — dois analistas podem chegar a resultados diferentes)
- Ocorre tarde (geralmente no recebimento do modelo, não ao longo do desenvolvimento)
- Não escala (um coordenador por projeto; não é viável em carteiras de dezenas de obras)

A Plataforma CHECK automatiza esse processo via IA + padrões openBIM — tornando a verificação contínua, objetiva e auditável.

---

## Como Funciona

```
Requisitos do Projeto (IDS) + Dicionário de Propriedades (bSDD)
              ↓
       Modelo BIM (IFC) chegando no CDE
              ↓
    Motor de Verificação CHECK (IA)
              ↓
   Relatório: ✓ Aprovado / ✗ Não-Conformidades
   (GUID do objeto + viewpoint BCF + propriedade em falta)
              ↓
   Motor de Orquestração: libera ou bloqueia aprovação do milestone
```

**Passo a passo:**

1. **Definição dos requisitos:** coordenador (ou contratante) cria/seleciona arquivo IDS que define o que cada objeto deve ter em cada fase
2. **Upload do modelo IFC:** disciplina entrega seu modelo no CDE (Componente a do Axis)
3. **Verificação automática:** CHECK cruza o modelo contra o IDS usando bSDD como referência de propriedades
4. **Resultado:** lista de conformidades e não-conformidades com localização exata no modelo
5. **Integração com Componente b:** não-conformidades bloqueiam automaticamente a aprovação do milestone correspondente

---

## IDS como Instrumento Contratual

Um aspecto técnico-jurídico com alto potencial: o IDS pode funcionar como **especificação técnica formal** em contratos de prestação de serviços BIM.

Se o contrato exige "entrega de modelo conformante com o IDS v1.2 anexo ao contrato", a Plataforma CHECK fornece evidência objetiva e auditável de cumprimento ou descumprimento — com rastreabilidade por objeto (GUID), por data de entrega e por analista responsável.

Isso transforma o IDS de documento técnico em instrumento contratual verificável, com implicações diretas para gestão de claims. Ver: [[bim-construction/tipos-contrato-engenharia]]

---

## Relação com Conformidade Governamental

O Decreto 10.306/2020 exige entrega de modelos BIM em obras federais no formato IFC. O IDS pode especificar os requisitos de conformidade mandatórios para cada fase. A Plataforma CHECK é a camada de verificação que comprova o atendimento — relevante para auditorias e para o Componente e do Axis (Ambiente de Entrega, integrado com Transfere.GOV e Obras.GOV 2.0).

Cenário concreto: uma construtora que reporta progresso de obra federal pode usar os relatórios da CHECK como evidência de conformidade BIM nos reports ao Transfere.GOV.

Ver: [[bim-construction/bim-regulatorio-brasil]]

---

## Posição no Ecossistema Axis

| Componente Axis | Relação com CHECK |
|---|---|
| **a — CDE** | Recebe os modelos IFC; aciona a CHECK automaticamente na chegada de nova versão |
| **b — Motor de Orquestração** | Usa resultado da CHECK para liberar ou bloquear aprovações de milestone |
| **e — Ambiente de Entrega** | Inclui relatórios de conformidade nos pacotes de entrega ao governo |
| **f — Agentes de IA** | Podem sugerir correções específicas a partir dos relatórios da CHECK |

---

## Knowledge Gaps

- Qual é a capacidade da componente IA vs. verificação puramente baseada em regras IDS (sem IA)?
- Como o CHECK lida com conformidade parcial (por fase, não binária)?
- Interface para criação/edição de arquivos IDS diretamente no produto?
- Integração com ferramentas de autoria (Revit, Archicad, Eberick) para validação em tempo de modelagem?

---

## Related Pages

- [[products/altoqi-axis]]
- [[products/altoqi-company]]
- [[bim-construction/openbim-standards]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[bim-construction/construcao-40]]
- [[bim-construction/tipos-contrato-engenharia]]
- [[bim-construction/bim-coordination]]
- [[bim-construction/sources/altoqi-finep-axis-2026]]
- [[glossary]]
