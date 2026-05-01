---
title: openBIM Standards
type: concept
created: 2026-05-01
updated: 2026-05-01
sources: [Formulário _ Projeto Finep_Axis_2026.pdf]
tags: [openbim, ifc, ids, bcf, bsdd, buildsmart, interoperabilidade, conformidade-bim, construção, bim]
---

# openBIM Standards

Conjunto de padrões abertos desenvolvidos pela **buildingSMART International** para viabilizar interoperabilidade entre ferramentas BIM de diferentes fornecedores. O princípio central: dados de construção devem fluir entre sistemas sem depender de formatos proprietários.

---

## Por que openBIM Importa

Em um projeto BIM típico, múltiplas ferramentas de fornecedores distintos coexistem: Autodesk Revit para arquitetura, Tekla para estrutura, Bentley para instalações, AltoQi Visus para planejamento. Sem padrões abertos, cada integração exige um conector proprietário bilateral — custoso, frágil e não escalável.

O openBIM define a "língua franca" que permite que todas essas ferramentas troquem dados com fidelidade semântica, não apenas geometria.

Conexão com [[bim-construction/construcao-40]]: o Fio Digital — a cadeia ininterrupta do projeto BIM à execução — só é possível quando os dados fluem livremente entre sistemas. Padrões fechados criam rupturas; padrões abertos eliminam a tradução humana entre etapas.

---

## Os Quatro Padrões Centrais

### IFC *(Industry Foundation Classes)*

- **O que é:** Formato de troca de modelos BIM entre disciplinas e sistemas
- **Norma:** ISO 16739, mantido pela buildingSMART International
- **Versão atual:** IFC 4.3 (com suporte a infraestrutura linear)
- **Analogia:** o "PDF do BIM" — qualquer software deve conseguir exportar e importar modelos em IFC sem perda de dados semânticos
- **Mandatório no Brasil:** Decreto 10.306/2020 exige entrega de modelos em formato IFC para obras federais
- **No Axis:** formato padrão para importação de modelos no CDE (Componente a) e no AltoQi Visus Planning

### IDS *(Information Delivery Specification)*

- **O que é:** Padrão para especificar formalmente o que deve ser entregue em um modelo BIM para uma finalidade específica
- **Forma:** arquivo XML validável automaticamente por software
- **Analogia:** um contrato técnico digital — define quais propriedades devem estar presentes em quais objetos, com quais valores, em quais fases do projeto
- **Exemplo de uso:** "Para aprovação de fundações na fase CD, todos os objetos `IfcPile` devem ter a propriedade `LoadBearing = True` e o campo `FireRating` preenchido"
- **No Axis:** núcleo da Plataforma CHECK — o IDS é o instrumento de verificação automatizada; um modelo que satisfaz o IDS é tecnicamente conformante
- **Implicação contratual:** o IDS pode funcionar como especificação técnica formal anexa a contratos — ver [[products/altoqi-check]]

### BCF *(BIM Collaboration Format)*

- **O que é:** Formato para comunicação de issues, comentários e solicitações de revisão vinculados a objetos específicos de um modelo BIM
- **Analogia:** GitHub Issues ou Jira, mas com coordenadas 3D — cada issue é ancorado ao objeto e ao viewpoint exatos no modelo
- **Formato:** arquivo BCF (ZIP com XML + capturas de tela)
- **No Axis:** Motor de Orquestração de Processos BIM (Componente b) usa BCF para gerenciar o fluxo de aprovações e revisões entre disciplinas

### bSDD *(buildingSMART Data Dictionary)*

- **O que é:** Banco de dados internacional aberto de classificações, propriedades e definições para objetos de construção
- **Acesso:** API REST pública em bsdd.buildingsmart.org
- **Analogia:** um "dicionário enciclopédico" que define o que é um parafuso estrutural, quais são suas propriedades padronizadas (diâmetro, material, norma de referência), em qual classe de objeto ele se encaixa
- **No Axis:** Plataforma CHECK usa bSDD para verificar se as propriedades dos objetos do modelo estão em conformidade com as definições internacionais e com os requisitos específicos do projeto (IDS)

---

## Pipeline de Conformidade openBIM

```
Contratante define requisitos → IDS (especificação formal)
                                    ↓
Disciplina entrega modelo → IFC (formato aberto)
                                    ↓
Propriedades verificadas contra → bSDD (dicionário de referência)
                                    ↓
Issues vinculados a objetos → BCF (formato de comunicação)
                                    ↓
Relatório: ✓ Conformante / ✗ Não-Conformidade + GUID + viewpoint
```

---

## Relação com Regulatório Brasileiro

O Decreto 10.306/2020 exige entrega de modelos IFC em obras federais. O IDS pode especificar os requisitos de conformidade mandatórios para cada fase. A Plataforma CHECK é a camada de verificação automatizada que comprova o atendimento — tornando-a relevante como ferramenta de compliance em licitações públicas e para o Ambiente de Entrega da Informação (Componente e do Axis, integrado com Transfere.GOV e Obras.GOV 2.0).

Ver: [[bim-construction/bim-regulatorio-brasil]]

---

## openBIM como Pré-Condição para Inteligência

Sem padrões abertos, os dados de cada ferramenta ficam em silos. O Axis depende de openBIM para a camada interna (CDE, Motor de Orquestração, Plataforma CHECK) funcionar como fonte única de verdade: se cada ferramenta fala uma língua proprietária, não há fonte única — há múltiplas fontes incompatíveis.

Paralelo com o domínio de IA: a mesma lógica de "meaning precedes intelligence" (Palantir) se aplica aqui — antes de qualquer inteligência preditiva, os dados precisam estar estruturados e interoperáveis. openBIM é a infraestrutura semântica da construção.

---

## Related Pages

- [[bim-construction/construcao-40]]
- [[bim-construction/bim-coordination]]
- [[bim-construction/bim-regulatorio-brasil]]
- [[products/altoqi-check]]
- [[products/altoqi-axis]]
- [[products/altoqi-visus-planning]]
- [[bim-construction/sources/altoqi-finep-axis-2026]]
- [[glossary]]
