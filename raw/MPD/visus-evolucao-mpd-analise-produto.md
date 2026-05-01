# Evolução da Plataforma Visus — Análise de Necessidades MPD Engenharia

> **Tipo:** Análise de Produto — AS IS / TO BE  
> **Perspectiva:** Especialista em Análise de Produtos  
> **Data:** 2026-05-01  
> **Fontes:** Exploração de produto realizada na MPD Engenharia (materiais coletados: Carta Convite Reffugio 359, Fluxos de Contratação, Método dos Pacotes de Entrega — AltoQi, QC Estrutura, Máscara de Medição, Quantitativos de Estrutura)

---

## 1. Contexto: Quem é a MPD Engenharia

A **MPD Engenharia** é uma construtora e incorporadora fundada há 43 anos, com atuação em 8 estados e mais de 45 cidades. São mais de 5,5 milhões de m² construídos ou em construção e aproximadamente 7.000 unidades lançadas, nos segmentos industrial, saúde, educacional, lazer, comercial, infraestrutura e residencial.

A MPD desenvolve empreendimentos de médio e alto padrão, principalmente em São Paulo e Alphaville (Barueri). Sua sede fica na Lapa (SP) e a filial em Alphaville. Lema: *"Projetos que transformam o futuro com excelência e qualidade."*

**Relevância para a AltoQi:** a empresa já adotou BIM (vencedora do Prêmio BIM SINDUSCON-SP), possui processos formalizados com forte base documental, utiliza modelos IFC para planejamento de ataque e produção de quantitativos para contratação — perfil de cliente avançado para a suíte Visus.

**Stack tecnológico atual observado:**

| Sistema | Uso |
|---|---|
| **BIM (Revit/similar)** | Modelos disciplinares, planos de forma, plano de ataque, quantitativos estruturais |
| **Senior Mega (ERP)** | Solicitação de compra, pedido e contrato |
| **DocuSign** | Assinatura digital de contratos |
| **Excel** | Mapa de cotação, equalização, máscara de medição, QC |
| **Email** | Carta convite, propostas de fornecedores |

---

## 2. AS IS — Processos MPD Mapeados

### 2.1 Método dos Pacotes de Entrega

A MPD estrutura o ciclo de vida do empreendimento em **4 fases + 5 gates + 2 colunas operacionais**:

```
Fase 01           Gate 1   Fase 02         Gate 2   Fase 03             Gate 3   Fase 04              Gate 4
Viabilidade   ────────── Estudo       ──────────  Desenvolvimento ──────────  Projetos         ──────────
do                        Preliminar              de Produto                  Executivos
Empreendimento

                                                                               ↓ Gate 4 (vermelho)
                                                                     Pacotes para Contratação:
                                                                     - Fundações, Estrutura, Instalações
                                                                     - Vedações, Esquadrias, Revestimentos
                                                                     - Concessionárias

Produção do Ativo / Obra         Gate 5         Gestão do Ativo
─────────────────────────── ──────────── ──────────────────────
Fundações → Infraestrutura        Habite-se      Manutenções e Garantias
→ Superestrutura →                As-Builts      Comissionamento
Instalações Infra →               Vistorias      Treinamento
Vedações → Instalações            Concessionárias Entrega e Transição
Finais → Acabamentos
```

**Observação crítica:** o Gate 4 é o portão mais complexo — ele transforma projetos executivos em **pacotes de contratação + pacotes de execução** por subsistema construtivo. É aqui que a maior oportunidade de Visus reside.

---

### 2.2 Fluxo de Contratação de Mão de Obra (8 etapas)

```
[obra]              [obra]             [obra]             [suprimentos]
1. Definição    →  2. Design Review  → 3. Carta Convite  → 4. Propostas
   Escopo           (Reengenharia)                          Fornecedores
(Levantamento
Quantitativo)

[suprimentos]                [obra]             [suprimentos]          [obra + suprim.]
5. Mapa Cotação +    →   6. Aprovação    →  7. Elaboração      →   8. Assinatura
   Equalização +          Mapa               Minuta                  Contrato
   Negociação             (GGO/Coorden.)                            (DocuSign)

Pós-contrato (Senior Mega):
[obra]                   [suprimentos]
7. Solicitação     →   8. Pedido/Contrato
```

### 2.3 Fluxo de Contratação de Material (7 etapas)

Idêntico ao de mão de obra, sem a etapa de Carta Convite e sem elaboração de minuta de contrato. Encerra com Pedido/Contrato no Senior Mega.

### 2.4 Carta Convite — Estrutura Observada (caso Reffugio 359)

A Carta Convite da MPD é um documento rico que inclui:
- Dados do empreendimento e tipologia
- **Plano de ataque** com imagens do modelo BIM 3D por pavimento
- **Lista de projetos** com código de revisão e status (aprovado/liberado)
- **Escopo de fornecimento** detalhado com obrigações contratuais
- **Quantitativo estruturado** por item (ml, m², m³) — 13 itens para estrutura
- Condições de pagamento, reajuste (INCC), documentação trabalhista exigida

**Dor observada:** o Levantamento Quantitativo (etapa 1) e o próprio documento de Carta Convite são produzidos manualmente. As imagens BIM são coladas em PDF. Os quantitativos vêm de Excel/modelo BIM sem rastro direto ao modelo.

### 2.5 Medição e Controle de Qualidade

Dois documentos Excel na exploração revelam processos críticos não digitalizados:
- **Máscara de Medição Estrutura:** template Excel para boletins de medição mensais por item de contrato
- **QC Estrutura:** checklist de controle de qualidade para elementos estruturais

Ambos são instrumentos presentes nos contratos (documentação exigida junto à NF para pagamento), mas operados fora de qualquer sistema conectado ao BIM.

---

## 3. AS IS — Plataforma Visus (Estado Atual)

| Módulo | O que faz hoje |
|---|---|
| **Visus Collab** | Repositório de arquivos/projetos, coordenação de disciplinas, gestão de incompatibilidades |
| **Visus Cost Management** | Extração automatizada de quantitativos de IFC/DWG/PDF, orçamentação, 20 bases públicas (SINAPI, SICRO) |
| **Visus Planning** | EAP, cronograma, simulação 4D, rastreamento planejado vs. executado, relatórios (Curva S, histograma) |
| **Visus Bid** | Cotações de suprimentos originadas no modelo BIM |
| **Visus Tracking** | Medições de serviços e verificação de progresso |
| **Visus Control Tower** | Dashboards integrados a projetos BIM, orçamentos e cronogramas |
| **Visus Workflow** | Gestão de tarefas, Kanban/Gantt, produtividade de equipes |

**Capacidades transversais:** +50 tipos de relatório, rastreabilidade orçamento↔modelo 3D, OpenBIM (IFC), integração com catálogos de fabricantes (Bilds), 70.000+ clientes, 37+ anos.

**AltoQi Axis (2026):** camada de IA transversal que adiciona alertas preditivos e automação de sequenciamento ao Planning — recém-anunciado.

---

## 4. Gap Analysis — O que falta para atender a MPD

### Mapa de Gaps

| Processo MPD | Cobertura Atual Visus | Gap |
|---|---|---|
| Definição de Escopo (Levantamento Quantitativo) | ✅ Cost Management extrai quantitativos do IFC | Falta: Packager — agrupa quantitativos em "pacotes de contratação" por subsistema |
| Design Review / Reengenharia | ⚠️ Collab tem coordenação | Falta: ferramentas de comparação de alternativas e registro de decisões de VE |
| Geração de Carta Convite | ❌ Não existe | Gap total: geração de documento de cotação a partir de modelo BIM |
| Propostas de Fornecedores | ⚠️ Visus Bid parcial | Falta: portal de fornecedores externo, workflow multi-cotação, prazo de resposta |
| Mapa de Cotação + Equalização | ❌ Não existe | Gap total: análise comparativa de propostas num mesmo ambiente |
| Aprovação de Mapa (GGO/Coord.) | ❌ Não existe | Falta: workflow de aprovação hierárquica com alçadas configuráveis |
| Elaboração de Minuta | ❌ Não existe | Falta: módulo de gestão contratual com templates |
| Assinatura (DocuSign) | ❌ Sem integração nativa | Falta: integração DocuSign ou equivalente |
| Solicitação/Pedido no ERP | ❌ Sem integração nativa | Falta: conector com Senior Mega / outros ERPs |
| Medição Mensal | ⚠️ Tracking existe | Falta: workflow de medição com aprovação, documentação trabalhista, retenções |
| QC em Campo | ❌ Não existe | Falta: checklists de qualidade vinculados a elementos BIM |
| Gate Review (portões metodológicos) | ❌ Não existe | Falta: gestão de gates com checklist de critérios de passagem |
| Portfólio Multi-obra | ⚠️ Control Tower básico | Falta: templates de padrões MPD aplicáveis a múltiplas obras simultaneamente |
| Gestão de Ativo Pós-obra | ❌ Não existe | Falta: módulo de comissionamento, garantias, manutenção |

---

## 5. TO BE — Evoluções Necessárias da Plataforma Visus

As evoluções estão organizadas por **horizonte de valor** — da dor mais imediata à transformação mais estratégica.

---

### 5.1 Horizonte 1 — Procurement Digital (Quick Wins)

#### 5.1.1 Visus Bid: Completar o Workflow de Cotação

O Visus Bid hoje inicia o processo de cotação, mas não acompanha a empresa até a contratação. É preciso evoluir para cobrir todo o **Fluxo de Contratação MPD**:

**Evolução necessária:**
- **Scope Packager:** agrupador de itens de quantitativo (oriundos do Cost Management) em "Pacotes de Contratação" nomeados (Estrutura, Instalações, Vedações, Revestimentos etc.) com escopo de fornecimento customizável
- **Gerador de Carta Convite:** documento parametrizado que importa dados do projeto (BIM, quantitativos, lista de projetos, cronograma, imagens do modelo) e produz PDF/Word padronizado
- **Portal de Fornecedores Externo:** ambiente web para recebimento de propostas com prazo, confirmação de leitura, carta de declínio (como exigido pela MPD), upload de documentos
- **Mapa de Cotação Digital:** comparativo automático das propostas recebidas, com campos de equalização (nivelar condições não comparáveis — frete, impostos, BDI) e campos de negociação
- **Workflow de Aprovação:** configuração de alçadas de aprovação do mapa (GGO, Coordenador) com notificações, prazo de resposta e registro de decisão

#### 5.1.2 Visus Contract: Novo Módulo (ou Expansão do Bid)

Atualmente, após o mapa aprovado, o processo sai do Visus. É necessário fechar este ciclo:

**Evolução necessária:**
- **Gestão de Contratos:** repositório de contratos por obra e fornecedor; vínculo direto ao Pacote de Contratação que originou o contrato; controle de status (minuta → em análise → assinado → em execução → encerrado)
- **Templates de Contrato:** base de cláusulas padrão configuráveis por tipo (mão de obra, material, serviço)
- **Integração DocuSign / Assinatura Digital:** envio e recebimento de contratos assinados sem sair da plataforma
- **Integração ERP (Senior Mega):** exportação ou trigger automático de solicitação de pedido/contrato para o ERP ao final do fluxo de aprovação — evitar redigitação e dupla entrada de dados
- **Controle de Retenções:** campo de retenção por contrato (ex.: 5% padrão MPD), cálculo automático na medição, controle do prazo de devolução pós-encerramento

---

### 5.2 Horizonte 2 — Medição e QC em Campo

#### 5.2.1 Visus Tracking: Evolução para Medição Contratual

O módulo Tracking precisa suportar o processo de **medição mensal** conforme exigência dos contratos MPD:

**Evolução necessária:**
- **Boletim de Medição Digital:** template de medição (Máscara de Medição) com itens vinculados ao escopo do contrato (Pacote de Execução), preenchível em campo ou escritório
- **Workflow de Aprovação de Medição:** engenheiro da obra confere → GGO aprova → liberação para faturamento
- **Checklist de Documentação Trabalhista:** campo estruturado para anexar os documentos exigidos junto à NF (GRF, SEFIP, GPS, ISS, folha de pagamento, comprovantes de benefícios, PPP) — trigger de pagamento só disponível quando todos documentos estão presentes
- **Controle de Reajuste:** aplicação automática de INCC sobre contratos com data-base parametrizada
- **Rastreabilidade Medição ↔ BIM:** cada item medido vinculado ao elemento BIM correspondente (IFC), permitindo visualização de progresso real no modelo 3D

#### 5.2.2 Visus Quality: Novo Módulo de QC em Campo

**Evolução necessária:**
- **Checklists de Controle de Qualidade** vinculados ao elemento BIM (ex.: QC Estrutura = checklist por elemento estrutural: concretagem, prumo, nível, limpeza, retirada de formas)
- **Registro de Não Conformidades (RNC):** com evidência fotográfica, responsável, prazo, ação corretiva e status de resolução
- **Critérios de Liberação de Pavimento:** um pavimento só é liberado para a etapa seguinte quando todos os itens do QC estão aprovados — gate de qualidade integrado ao Planning
- **Integração com Diário de Obra:** registro de entrada/saída de equipamentos, efetivo diário, condições climáticas — atende exigência contratual MPD

---

### 5.3 Horizonte 3 — Gestão de Gates e Pacotes de Entrega

#### 5.3.1 Visus Lifecycle: Novo Módulo de Gestão de Gates

O "Método dos Pacotes de Entrega" da MPD (formalizado junto à AltoQi) precisa de uma casa na plataforma:

**Evolução necessária:**
- **Configuração de Gates:** cada empreendimento tem gates configuráveis com checklist de critérios de passagem (ex.: "Compatibilização BIM Concluída", "Orçamento Executivo Aprovado", "Pacote para Contratação de Estrutura emitido")
- **Rastreamento de Entregáveis por Fase:** visibilidade do status de cada entregável (emitido, em revisão, aprovado, reprovado) para cada fase do ciclo de vida
- **Pacotes de Entrega como Objeto de Plataforma:** um Pacote é uma entidade persistente que nasce na fase de Projetos Executivos, gera um Pacote de Contratação (→ Bid), alimenta o cronograma (→ Planning), é executado na obra (→ Tracking) e encerra com medição (→ Contract)
- **Visibilidade Multi-Obra:** dashboard de ciclo de vida de todos os empreendimentos ativos — em que Gate está cada obra? Quais gates têm critérios pendentes?

---

### 5.4 Horizonte 4 — Design Review e Engenharia de Valor

A etapa **Design Review (Reengenharia)** no fluxo de contratação MPD é onde a equipe de obra revisa o projeto antes de ir ao mercado. É uma etapa de engenharia de valor não suportada pelo Visus hoje.

**Evolução necessária:**
- **Comentários e Decisões no Modelo:** capacidade de registrar no Collab decisões de reengenharia vinculadas a elementos BIM, com versão antes/depois
- **Análise de Alternativas:** comparação de soluções construtivas (ex.: parede diafragma vs. estacas) com impacto em custo (Cost Management) e cronograma (Planning) calculados automaticamente
- **Registro de Design Review:** ata digital da reunião de design review com rastreabilidade das mudanças de projeto e impacto nos pacotes de contratação

---

### 5.5 Horizonte 5 — Padronização e Portfólio (Escala MPD)

A MPD opera múltiplos empreendimentos simultaneamente em 8 estados. Hoje os "padrões técnicos MPD" são documentos PDF/Word aplicados manualmente.

**Evolução necessária:**
- **Templates de Obra por Tipologia:** pré-configuração de EAP, Pacotes de Entrega, Gates, checklists QC, cláusulas de contrato, e modelo de medição por tipologia de obra (residencial, industrial, hospitalar)
- **Biblioteca de Escopo de Fornecimento:** cláusulas contratuais padronizadas por serviço reutilizáveis na geração de Carta Convite
- **Benchmark Multi-Obra:** comparação de produtividade, custo por m³ de concreto, duração de ciclo de laje entre empreendimentos da mesma tipologia
- **Relatórios de Portfólio para Alta Gestão (GGO):** painéis de aprovação centralizada (como GGO/Coordenação hoje faz por email/reunião)

---

### 5.6 Horizonte 6 — Gestão do Ativo (Pós-Habite-se)

O Gate 5 do Método MPD exige uma série de entregas operacionais (comissionamento, as-builts, manutenções) que hoje ficam fora de qualquer sistema digital.

**Evolução necessária:**
- **Módulo de Comissionamento:** checklist de comissionamento por sistema (elevador, água, elétrica, gerador, gás) com registro de testes e aprovação de concessionárias
- **As-Built Digital:** modelo BIM atualizado com as condições reais de obra, vinculado ao empreendimento entregue
- **Manual do Proprietário / Condomínio Digital:** pacote de documentação de entrega (plantas, manuais, garantias) gerado a partir dos dados do projeto
- **Gestão de Garantias:** período de garantia por subsistema, alertas de vencimento, registro de chamados de pós-obra

---

## 6. Priorização Estratégica

### Matriz de Impacto vs. Esforço

| Evolução | Impacto para MPD | Esforço Visus | Prioridade |
|---|---|---|---|
| Scope Packager + Gerador de Carta Convite | 🔴 Alto | 🟡 Médio | **1** |
| Mapa de Cotação + Equalização Digital | 🔴 Alto | 🟡 Médio | **2** |
| Workflow de Aprovação de Mapa (Alçadas) | 🔴 Alto | 🟢 Baixo | **3** |
| Boletim de Medição Digital + Aprovação | 🔴 Alto | 🟡 Médio | **4** |
| Integração DocuSign | 🔴 Alto | 🟢 Baixo | **5** |
| Integração Senior Mega (ERP) | 🔴 Alto | 🔴 Alto | **6** |
| QC em Campo (checklists BIM-linked) | 🟡 Médio | 🟡 Médio | **7** |
| Checklist Documental de Medição | 🟡 Médio | 🟢 Baixo | **8** |
| Gates + Pacotes de Entrega como objetos | 🔴 Alto | 🔴 Alto | **9** |
| Templates de Tipologia (escala MPD) | 🟡 Médio | 🟡 Médio | **10** |
| Design Review / Análise de Alternativas | 🟡 Médio | 🔴 Alto | **11** |
| Gestão do Ativo / Comissionamento | 🟢 Baixo (curto prazo) | 🔴 Alto | **12** |

---

## 7. Narrativa de Produto: O Visus que a MPD Precisa

> *"O Visus que a MPD precisa não é o Visus que vende BIM — é o Visus que vende ciclo de vida de contrato."*

A MPD já aceita o BIM. O modelo está lá, os quantitativos existem. O problema dela começa **depois** que o quantitativo sai do modelo: ele vai para um Excel, vira uma Carta Convite em Word, as propostas chegam por email, a equalização é feita num mapa de cotação Excel, a aprovação é dada em reunião ou Whatsapp, a minuta vai para o suprimentos, o contrato assina no DocuSign, o pedido entra no Senior Mega — e nada disso conversa com o modelo BIM original.

**O gap central não é BIM. É a camada de procurement e contratos.**

O Visus Bid precisa se tornar um **módulo de procurement de obra** completo — do quantitativo ao contrato assinado — e o Visus Tracking precisa se tornar um **módulo de gestão contratual de execução** — da medição ao pagamento liberado. Estes dois módulos, integrados pelo Pacote de Entrega como objeto central, entregariam à MPD o que ela não tem hoje: **rastreabilidade completa entre o elemento BIM, o contrato que o cobre, e a medição que o liquida.**

---

## 8. Perguntas para Próximas Rodadas de Descoberta

1. **Qual é a dor número 1 do suprimentos** com o processo atual de carta convite e mapa de cotação? Prazo? Retrabalho? Falta de visibilidade do que o modelo BIM prevê vs. o que está sendo contratado?
2. **O GGO** aprova o mapa hoje por email ou por sistema? Qual é o prazo médio de aprovação e o principal motivo de atraso?
3. **A integração com o Senior Mega** — é uma exigência dura (o Visus precisa alimentar o Senior) ou existe abertura para substituição parcial do ERP para a parte de obras?
4. **A Máscara de Medição Excel** é padronizada entre obras ou cada engenheiro monta a sua? Quem aprova a medição antes do pagamento?
5. **O Design Review** é uma reunião formal com ata ou uma troca informal? Quem documenta as decisões de reengenharia e como elas chegam ao suprimentos?
6. **O Método dos Pacotes de Entrega** já foi adotado formalmente ou ainda é aspiracional? Em quais obras ele está sendo praticado?

---

*Documento produzido a partir de exploração de produto realizada na MPD Engenharia. Materiais utilizados: Carta Convite Reffugio 359, Fluxos de Contratação (Mão de Obra e Material), Método dos Pacotes de Entrega — AltoQi, QC Estrutura, Máscara de Medição Estrutura, Quantitativos de Estrutura.*
