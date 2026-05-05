---
title: "Axis e Visus Planning: Próximos Passos de Desenvolvimento e Relação Estrutural"
type: analysis
created: 2026-05-01
updated: 2026-05-01
sources: [altoqi-finep-axis-2026.md, eduardo-bandeira-ponte-logica.md]
tags: [altoqi, altoqi-axis, altoqi-visus-planning, construção-4.0, trl, digital-thread, aprendizagem-operacional, planejamento-preditivo, openBIM, análise]
---

# Axis e Visus Planning: Próximos Passos de Desenvolvimento e Relação Estrutural

*Síntese dos próximos passos de desenvolvimento do AltoQi Axis e do Visus Planning, incluindo a lógica da simbiose entre os dois produtos.*

---

## O Problema Central

O problema que o Axis resolve tem duas faces complementares:

- **Abismo informacional** — canteiro e escritório operam em silos; dados não se comunicam em tempo real; o processo decisório é reativo. Pedidos de material chegam por telefone, medições ficam em cadernos, diários de obra não têm padronização semântica. A consequência operacional é o ciclo de "apagar incêndios": estoques superdimensionados que degradam, ou paralisação por falta de materiais — ambos sintomas de ausência de fluxo de dados entre as pontas.

- **Ausência de memória** — dados de execução de cada obra não retroalimentam projetos futuros. Produtividade real por frente, lead times de fornecedores, padrões de atraso que se repetiram — tudo isso permanece preso no projeto onde foi gerado. Cada obra começa do zero, sem herdar o aprendizado das anteriores.

Essas duas faces são o mesmo problema em momentos diferentes do tempo: o abismo é o problema *durante* a obra; a ausência de memória é o problema *entre* obras.

---

## Próximos Passos do Axis

O Axis é composto por seis componentes técnicos, cada um com um nível de maturidade tecnológica (TRL) atual e uma meta. A sequência de desenvolvimento emerge diretamente dessa leitura.

### Componentes de evolução incremental (TRL 4→7)

Três componentes estão demonstrados em ambiente relevante e precisam de robustez e escala, não de pesquisa nova:

- **[[projects/altoqi-axis]] (Componente b — Motor de Orquestração)** coordena workflows multi-stakeholder com gatilhos automáticos por marcos do cronograma e issues vinculados a objetos do modelo via BCF. O próximo passo é tornar esses gatilhos confiáveis em ambiente de produção com múltiplos projetos simultâneos.

- **[[projects/altoqi-axis]] (Componente d — Coleta de Campo)** captura dados de execução no canteiro — formulários, fotos, leituras de QR/RFID — e os vincula ao modelo BIM. É o componente mais urgente operacionalmente: sem ele, o Axis tem inteligência sobre dados históricos de projeto, mas não sobre o que está acontecendo na obra agora. O gêmeo digital permanece um arquivo, não uma ferramenta ativa. O QR scan de uma peça montada no canteiro deveria atualizar automaticamente o percentual de execução no modelo virtual — enquanto isso não acontece, o loop entre execução física e modelo digital permanece quebrado.

- **[[projects/altoqi-axis]] (Componente e — Ambiente de Entrega da Informação)** produz dashboards de gestão e integra com plataformas governamentais (Transfere.GOV e Obras.GOV 2.0). O avanço aqui abre o mercado público — o Decreto 10.306/2020 torna o IFC obrigatório em obras federais, e a Lei 14.133/2021 prevê BIM nas contratações públicas, criando demanda estrutural por um ambiente de entrega que já fale a linguagem dessas plataformas.

### Componentes de ruptura (TRL 3→7)

Dois componentes têm o maior salto de maturidade e são os de maior risco técnico — e também os de maior diferencial percebido pelo cliente:

- **[[projects/altoqi-check]] (Componente c — Plataforma CHECK)** realiza verificação automatizada de conformidade BIM usando IDS *(Information Delivery Specification)* e bSDD *(buildingSMART Data Dictionary)*. O IDS define o que deve ser entregue em cada fase do projeto — quais propriedades cada elemento precisa ter, com quais valores, em qual formato. O bSDD fornece o dicionário de propriedades para essa verificação. Hoje, a conformidade de um modelo BIM contra os requisitos do projeto é verificada manualmente — ou não é verificada. O CHECK automatiza essa etapa: dado um contrato ou conjunto de requisitos, o sistema verifica se o modelo IFC os satisfaz elemento a elemento. O próximo passo de desenvolvimento é a geração automática de regras IDS a partir de linguagem contratual — LLMs que leem o caderno de encargos e produzem as regras de verificação sem intervenção humana.

- **[[projects/altoqi-axis]] (Componente f — Agentes Especializados de IA)** operam sobre os dados estruturados dos demais componentes para gerar alertas preditivos, automatizar rotinas e simular cenários. Um agente que monitora o CDE *(Common Data Environment)* e o cronograma em busca de exceções pode emitir alertas como "70% de probabilidade de atraso na atividade X se o material não chegar até quinta" — não como heurística manual, mas como inferência sobre padrões de obras anteriores. A qualidade dos agentes é diretamente proporcional à qualidade dos dados nos componentes a–e: agentes inteligentes sobre dados ruins produzem alertas ruins.

---

## Próximos Passos do Planning: Três Gaps Estruturais

O Planning está maduro nas **Frentes 1** (planejamento e previsão) e **4** (rastreamento planejado vs. executado). Os gaps que limitam seu avanço são estruturais — não são funcionalidades faltando, são limitações de arquitetura que o Axis está posicionado para resolver:

**Gap 1 — O "executado" é manual.**
A aba de rastreamento requer entrada manual de percentuais de execução por atividade. A Frente 4 existe como conceito, mas não como loop automático. O dado de campo não chega ao modelo sem intervenção humana — o que significa que a acurácia do rastreamento depende da disciplina da equipe de campo, e que o dado chega com atraso. A Frente 4 atual é rastreamento reativo; a Frente 4 com o Componente d integrado seria monitoramento contínuo.

**Gap 2 — A Frente 5 não existe como produto.**
O Planning gera dados de desvio — produtividade real por frente, diferença entre planejado e executado, datas reais de início e término de atividades. Esses dados não saem do projeto. Não alimentam projetos futuros, não treinam modelos preditivos, não constroem nenhum banco de padrões. O Planning é o principal *gerador* do dado que resolveria a ausência de memória operacional, mas não tem a camada que o *processa*. Esse é exatamente o papel do Axis: acumular esses dados via CDE e processá-los via agentes para que a próxima obra herde o aprendizado.

**Gap 3 — A qualidade do IFC de entrada não é verificada.**
O Planning importa modelos IFC e confia neles. Modelos com propriedades inconsistentes, nomenclaturas incorretas e elementos sem GUID entram silenciosamente — e os erros se propagam para a EAP, o cronograma e os relatórios. O problema "lixo entra, lixo sai" precisa ser resolvido *antes* do Planning, não dentro dele. O Componente c — CHECK — é a resposta upstream: antes de o IFC chegar ao Planning, ele é validado contra regras IDS que garantem que cada elemento tem as propriedades necessárias para a fase em que se encontra.

---

## A Estrutura da Simbiose

A relação entre os dois produtos não é de integração lateral — é de dependência mútua assimétrica:

```
Planning → [dados de execução] → CDE → Agentes IA → [alertas, predições] → Planning
                ↑                                                                 ↓
         Campo fecha o loop                                        Frente 1 fica preditiva
```

**Planning alimenta Axis:** cada projeto executado no Planning gera os dados que tornam os agentes inteligentes — desvios por tipo de atividade, produtividade real por frente, padrões de risco que se materializaram em obras anteriores. A base de 10.000+ clientes ativos do Visus é o moat competitivo do Axis: nenhum outro player brasileiro tem essa escala de dados de obra reais para treinar modelos preditivos.

**Axis alimenta Planning:** o aprendizado acumulado retorna ao Planning como inteligência de primeira classe — sugestões de sequenciamento baseadas em obras similares, alertas preditivos antes que o atraso aconteça, otimização automática de predecessoras. É o que torna concreta a promessa "cada obra começa em um nível mais alto de maturidade" dentro do produto de planejamento.

**O elo crítico é o Componente d.** O loop só se fecha automaticamente quando o dado de campo chega ao CDE sem intervenção manual — quando o QR scan no canteiro atualiza o Planning, não quando o engenheiro lembra de digitar o percentual. Sem esse elo, o ciclo de aprendizado existe mas é lento e sujeito a viés de entrada. Com ele, a Frente 4 vira input automático do Axis e a Frente 5 deixa de ser potencial para ser entregue via aprendizado contínuo.

---

## Sequência Lógica de Desenvolvimento

Ordenada por dependência funcional — cada fase desbloqueia a próxima:

| Fase | Componente | O que entrega | O que desbloqueia no Planning |
|---|---|---|---|
| **1** | [[projects/altoqi-axis]] (d — Campo, 4→7) | Coleta automática de dado de execução no canteiro | Frente 4 automática; fim da entrada manual |
| **2** | [[projects/altoqi-axis]] (b — Orquestração, 4→7) | Gatilhos automáticos por marcos do cronograma | Procurement triggers; alertas de marco |
| **3** | [[projects/altoqi-check]] (c — CHECK, 3→7) | Verificação IDS automática antes da importação | Qualidade garantida de IFC na entrada; IDS contratual |
| **4** | [[projects/altoqi-axis]] (f — Agentes IA, 3→7) | Predição e automação sobre dados estruturados | Frente 1 preditiva; Frente 5 via aprendizado acumulado |
| **5** | DaaS / Marketplace | Dados anonimizados como produto; integrações de terceiros | Planning vira nó de uma rede de dados de obras |

A ordem importa: os agentes (fase 4) só são úteis se os dados nos componentes anteriores forem confiáveis. O CHECK (fase 3) garante qualidade de entrada. O Campo (fase 1) garante que o dado de execução real chegue ao sistema. Inverter essa ordem produz inteligência artificial sobre dados ruins.

---

## Insight Estrutural

O Planning opera no nó mais crítico do fluxo de dados da construção: o cronograma 4D é o ponto de encontro entre o modelo virtual — geometria, propriedades, quantitativos — e a execução física — frentes de obra, produtividade, datas reais. É onde o fluxo de dados se torna fluxo de materiais, onde a decisão digital vira ação no canteiro.

Isso significa que o Planning não é apenas um dos módulos que o Axis potencializa — é o módulo estruturante da proposta de valor do Axis para o mercado de construção. O problema central que o Axis quer resolver ("cada obra começa do zero") só existe porque o dado de execução que o Planning já captura não retroalimenta projetos futuros. Não é um problema de captura — o Planning já captura. É um problema de memória.

**O Axis é a camada de memória que o Planning sempre precisou mas não tinha.**

---

## Related Pages

- [[projects/altoqi-axis]] — arquitetura dos seis componentes; seis capacidades de produto
- [[projects/altoqi-visus-planning]] — workflow operacional; posicionamento nas cinco frentes
- [[projects/altoqi-check]] — Componente c; verificação de conformidade upstream
- [[bim-construction/altoqi-finep-axis-2026]] — proposta FINEP; TRL por componente; modelos de negócio
- [[bim-construction/eduardo-bandeira-ponte-logica]] — Fio Digital; Digital Twin vivo; scripts sentinelas
- [[bim-construction/planejamento-preditivo-obras]] — conceito de planejamento preditivo; cinco frentes de IA
- [[bim-construction/construcao-40]] — paradigma de digitalização; processos determinísticos vs. empíricos
- [[bim-construction/openbim-standards]] — IFC/IDS/BCF/bSDD; base técnica do CHECK
