---
title: "Evolução da Plataforma Visus — Análise de Necessidades MPD Engenharia"
type: source
created: 2026-05-05
updated: 2026-05-05
source_url: "Fonte interna de trabalho (arquivo local): raw/MPD/visus-evolucao-mpd-analise-produto.md"
source_type: internal-product-analysis
author: Equipe AltoQi (Peter, Felipe, Claudio)
published: 2026-05-04
tags: [altoqi, visus, mpd, procurement, contratos, medicao, pacote-entrega, gate-4, senior-mega, docusign, control-tower, tracking, bid, cost-management, planning, produto, bim, construcao]
---

# Evolução da Plataforma Visus — Análise de Necessidades MPD Engenharia

Transcrição integral da proposta de evolução do Visus para a MPD Engenharia (AS IS / TO BE), preservando todo o conteúdo original sem resumo.

**URL original:** Fonte interna de trabalho (arquivo local): `raw/MPD/visus-evolucao-mpd-analise-produto.md`

---

# Evolução da Plataforma Visus — Análise de Necessidades MPD Engenharia

> **Tipo:** Análise de Produto — AS IS / TO BE  
> **Perspectiva:** Especialista em Análise de Produtos  
> **Data:** 2026-05-04  
> **Fontes primárias:** Gravação de reunião interna AltoQi (30/04/2026), Carta Convite Reffugio 359, Fluxos de Contratação (Mão de Obra e Material), Framework Método dos Pacotes de Entrega (HTML), Máscara de Medição Estrutura, QC Estrutura, Quantitativos de Estrutura  
> **Status da oportunidade:** MPD encomendou solução; proposta a ser entregada na semana seguinte à reunião

---

## 1. Quem é a MPD Engenharia

A **MPD Engenharia** é uma construtora e incorporadora com quase 45 anos de existência. Atua em 8 estados e mais de 45 cidades, com mais de 5,5 milhões de m² construídos ou em construção e aproximadamente 7.000 unidades lançadas. Fatura cerca de **R$ 1,5 bilhão por ano**. Opera nos segmentos industrial, saúde, educacional, lazer, comercial, infraestrutura e residencial (médio e alto padrão). Sede em Lapa (São Paulo) e filial em Alphaville (Barueri). Lema: *"Projetos que transformam o futuro com excelência e qualidade."*

Vencedora do Prêmio BIM SINDUSCON-SP, a empresa utiliza modelos BIM ativamente para produção de quantitativos, plano de ataque e coordenação de projetos.

### 1.1 Momento institucional

A MPD passou por um processo de **profissionalização nos últimos 2 anos**. A liderança atual — incluindo o diretor Fábio e gerentes de obra como Adriano — veio de grandes construtoras como **Camargo Corrêa**, empresas de primeira linha que colapsaram após o escândalo da Lava Jato. Essas pessoas trouxeram consigo processos bem desenhados de obras de grande porte. O resultado é uma empresa que "funciona redonda" — entrega o que se propõe — mas que **opera processos maduros de forma completamente manual**, com Excel, e-mail, Word, WhatsApp e ligações.

> *"Eles estão há dois anos construindo os processos. O processo em si está bem desenhado, mas o fluxo de informação é descentralizado, dependendo muito de pessoas."* — Felipe (AltoQi)

### 1.2 Perfil operacional

| Dado | Valor |
|---|---|
| Faturamento anual | ~R$ 1,5 bilhão |
| Canteiros simultâneos ativos | 20+ |
| Equipe de suprimentos | 36 pessoas (separadas da obra) |
| Pacotes de entrega definidos | 200+ (Curva A, B e C) |
| Volume de Curva A | ~80% do custo da obra |

### 1.3 Interlocutores chave

| Nome | Papel | Relevância |
|---|---|---|
| **Carol** | Gerente de Inovação | *"Se ela adotar, a MPD inteira adota."* Interface principal da MPD com a AltoQi |
| **Fábio** | Diretor (ex-Camargo Corrêa) | Dono do processo; validou a solução: *"estou atendendo no mínimo 1.500 construtoras no Brasil"* |
| **Adriano** | Coordenação de obras | Interface entre projetos, suprimentos e obra |
| Engenheiros/Coordenadores | Equipe de obra e coordenação geral | Usuários diários do fluxo de pacotes |

### 1.4 Stack tecnológico atual

| Sistema | Uso atual |
|---|---|
| **BIM (Revit/similar)** | Modelos disciplinares, planos de forma, plano de ataque, quantitativos estruturais |
| **Senior Mega (ERP/RP)** | Solicitação de compra, pedido e contrato; recebimento de NF e pagamento |
| **DocuSign Enterprise** | Assinatura digital de contratos (com fluxo jurídico embutido no Enterprise) |
| **Excel** | Mapa de cotação, equalização, máscara de medição, QC, quantitativos |
| **E-mail / WhatsApp** | Carta convite, recebimento de propostas, aprovações de mapa, comunicação com fornecedores |
| **Word / PDF** | Escopo de fornecimento, carta convite, condições contratuais |

> **Posicionamento estratégico da AltoQi:** o ERP faz bem o que é dele — financeiro, contábil, NF, pagamento. A Visus deve criar a **camada de gestão digital** acima do ERP para tudo que acontece antes do pagamento. *"Nunca ouvi falar de uma consultora satisfeita com os fluxos do RP."*

---

## 2. Metodologia de Pacotes de Entrega (MPD)

### 2.1 Visão geral

A MPD estrutura o ciclo de vida completo do empreendimento em **4 fases + 5 gates + 2 colunas operacionais**. Esse framework foi formalizado em parceria com a AltoQi e está representado no documento "Método dos Pacotes de Entrega":

```
Fase 01              Gate 1    Fase 02          Gate 2    Fase 03                Gate 3    Fase 04
Viabilidade do   ──────────  Estudo        ──────────  Desenvolvimento     ──────────  Projetos
Empreendimento               Preliminar                de Produto                      Executivos

                                                                                         ↓ Gate 4 (crítico — vermelho)
                                                                               Pacotes para Contratação + Execução

        Produção do Ativo / Obra              Gate 5          Gestão do Ativo
────────────────────────────────────   ───────────────   ──────────────────────────
Fundações → Infraestrutura →                Habite-se         Manutenções e Garantias
Superestrutura → Instalações Infra →        As-Builts         Comissionamento
Vedações → Instalações Finais →             Vistorias         Treinamento
Revestimentos e Acabamentos                 Concessionárias   Entrega e Transição
```

**O conceito de Pacote não começa na obra** — ele é usado desde a fase de Viabilidade. Cada fase tem entregáveis definidos como pacotes de informação, e o handover entre fases é controlado por gates com checklists de critérios de aprovação.

### 2.2 Gate 4 — O portão mais crítico

O Gate 4 é o momento em que os projetos executivos se transformam em **pacotes operacionais** para a obra. É o ponto de maior transformação de informação no ciclo:

**Checklist de critérios do Gate 4 (pré-obra):**
- Projetos Executivos Coordenados Aprovados
- Detalhamentos Técnicos Liberados
- Compatibilização BIM Concluída
- Memorial de Cálculo Aprovado
- Pacote para Contratação de Fundações ✓
- Pacote para Execução de Fundações ✓
- Pacote para Contratação de Estrutura ✓
- Pacote para Execução de Estrutura ✓
- Pacote para Contratação Instalações ✓
- Pacote para Execução de Instalações ✓
- Pacote para Contratação Vedações ✓
- Pacote para Execução Vedações ✓
- Pacote para Contratação Esquadrias e Guarda Corpos ✓
- Pacote para Execução Esquadrias e Guarda Corpos ✓
- Pacote para Contratação Revestimentos ✓
- Pacote para Execução Revestimentos ✓
- Pacote para Contratação Concessionárias ✓
- Pacote para Execução Concessionárias ✓

### 2.3 O Pacote como unidade central

**Definição:** um Pacote é uma divisão lógica do escopo da obra que agrupa tudo necessário para contratar e executar um conjunto coerente de serviços ou materiais.

**Hierarquia de objetos (conforme alinhado na reunião):**

```
OBRA
└── PACOTE (ex: Pacote 02 — Estrutura)
    ├── CONTRATO A (ex: Estrutura de Concreto — Empreiteiro X)
    │   └── Marcos de Medição (ciclos mensais ou por entrega)
    └── CONTRATO B (ex: Estrutura Metálica — Fornecedor Y)
        └── Marcos de Medição
```

> *"O sistema tem que permitir que a gente quebre esse pacote em contratos diversos. Mas sempre vai ser Estrutura, Pacote, Contrato. E a arquitetura de informação é sempre a mesma."*

**Importante:** um pacote pode se transformar em novos pacotes se o escopo tiver natureza suficientemente distinta. Exemplo: a estrutura pré-moldada pode virar pacote separado da estrutura de concreto convencional.

### 2.4 Curva ABC de pacotes

| Curva | Pacotes | Gestão | Objetivo |
|---|---|---|---|
| **A** | ~Curva A de custo (~80%) | **Centralizada** — equipe corporativa | Consolidar compra por volume entre os 20+ canteiros; hoje não tem visibilidade cruzada entre obras |
| **B** | Foco inicial | **Descentralizada** por canteiro | Cada canteiro decide |
| **C** | 200+ pacotes fragmentados | **Descentralizada** por canteiro | Obras especiais têm particularidades únicas (hospital, laboratório, universidade) |

**Pain point de Curva A:** a MPD tem potencial gigante de compra por volume (20+ canteiros) mas não consegue cruzar demandas entre obras porque não há visibilidade do pipeline de contratações numa linha do tempo centralizada.

### 2.5 Conteúdo de um Pacote (5 pilares)

Cada pacote possui uma estrutura padronizada de informação:

| # | Pilar | Conteúdo |
|---|---|---|
| 1 | **Projetos** | Arquivos do projeto (links para CDE/Colab), modelos IFC, lista de projetos com revisão/status |
| 2 | **Memorial Descritivo** | Especificações técnicas, padrões de execução, condições gerais |
| 3 | **Quantitativos** | Quantitativos já com maturidade de projeto executivo (oriundos do BIM/Cost Management) |
| 4 | **Inspeção / Ensaios / QC** | Critérios de verificação de qualidade específicos do pacote (ex: SLAMP test para estrutura, laudo de concretagem) |
| 5 | **Cronograma de Execução** | Desdobramento temporal do pacote dentro do cronograma da obra, com marcos de entrega |
| 6 | **Condições Contratuais** | Cláusulas padrão por tipo de pacote (já existe padronização: "ele já sabe como compra estrutura, vedação, elétrica") |

> *"A gente tem uma equipe lá que só faz isso — montando o conjunto de informações que no fim vão compor arquivo em texto e planilhas."* — hoje 100% manual.

---

## 3. Fluxo de Procurement (AS IS → TO BE)

### 3.1 Gatilho de Contratação

**Input do planejamento:** os pacotes são posicionados numa linha do tempo. Cada pacote tem duas datas:
- **Data de início da execução** (vem do Planning — linha laranja)
- **Data de início da contratação** (predecessora — linha azul)

**Exemplo:** Pacote 02 Estrutura → execução começa no Mês 3 → contratação precisa iniciar no Mês 1 → alerta automático à equipe de suprimentos no Mês 1.

**Meta atual:** ao CON (início de obras), **30% da Curva A já deve estar contratada**. Hoje, muitas contratações iniciam apenas após o começo da obra, causando atraso.

### 3.2 Fluxo de Contratação de Mão de Obra (8 etapas)

```
[OBRA]                [OBRA]              [OBRA]               [SUPRIMENTOS]
1. Definição     →   2. Design Review  → 3. Carta Convite   → 4. Propostas
   de Escopo          (Reengenharia)       gerada do pacote     Fornecedores
   + Levantamento                          + disparada          (portal/e-mail)
   Quantitativo

[SUPRIMENTOS]                      [OBRA]              [SUPRIMENTOS]         [OBRA + SUPRIM.]
5. Mapa de Cotação +        →   6. Aprovação      → 7. Elaboração       → 8. Assinatura
   Equalização +                  (GGO / Coord.)      Minuta               Contrato
   Negociação                                                               (DocuSign)

PÓS-CONTRATO (Senior Mega):
[OBRA]                    [SUPRIMENTOS]
9. Solicitação        → 10. Pedido / Contrato no ERP
```

### 3.3 Fluxo de Contratação de Material (7 etapas)

Igual ao de mão de obra, sem a Carta Convite e sem elaboração de minuta de contrato. Encerra com Pedido/Contrato no Senior Mega.

### 3.4 Passo a passo detalhado

#### Etapa 1 — Definição de Escopo

- A equipe de obra define o escopo com base nos projetos em status **"Liberado Obra"**
- Os projetos chegam à obra com revisão aprovada; cada projeto tem código padronizado (ex: `0544-PRJ-ES-LO-0501-T01-FO-1PAV-R00.PDF`)
- O levantamento quantitativo é feito a partir do modelo BIM e documentado em planilha Excel (Máscara de Medição / Quantitativo)
- O escopo é estruturado em itens com descrição, quantidade e unidade (ex: Execução superestrutura 7º PAV à Cobertura — 2.938,51 m³)

#### Etapa 2 — Design Review (Reengenharia)

- A equipe de obra revisa o projeto antes de ir ao mercado
- Objetiva identificar oportunidades de **engenharia de valor** (alternativas construtivas, simplificações, substituições de material)
- **Ponto crítico:** a informação da carta convite deve ser precisa e completa; se alguma informação estiver faltando ao fechar o contrato, gera necessidade de aditivos e "ativação de monte de coisa"
- Hoje: reunião informal, sem registro formal de decisões

#### Etapa 3 — Geração da Carta Convite

A Carta Convite é um documento padronizado composto por:
- Identificação do empreendimento (nome, tipologia, endereço, número de unidades por pavimento)
- **Plano de ataque** com imagens do modelo BIM 3D (renderizações por pavimento: Térreo, 1ºSS, 2ºSS, 1ºPAV, 2ºPAV)
- **Lista de projetos** com código, revisão e status (aprovado/liberado)
- **Cronograma de execução** (início por etapa: vigas de coroamento, sapatas, superestrutura)
- **Escopo de fornecimento** (condições gerais, segurança, canteiro, escoramento, conclusão de serviços)
- **Quantitativo estruturado** por item (em média 13 itens para estrutura)
- Condições de pagamento (medições mensais, 21 dias, retenção de 5%, INCC data-base)
- Documentação trabalhista exigida (GRF, SEFIP, GPS, folha de pagamento, PPP, rescisões, etc.)

> Hoje: cada carta convite é montada manualmente do zero para cada pacote. São dezenas de cartas por obra, projeto a projeto.

#### Etapa 4 — Seleção de Fornecedores e Envio

- MPD tem **cadastro de fornecedores confiáveis** por tipo de serviço
- Envia carta convite por **e-mail** para os selecionados
- Existe processo de recebimento de **carta de declínio** de quem não pode participar
- Prazo de resposta fixo (ex: proposta até 05/07/24)
- **TO BE desejado:** portal com link de acesso centralizado, controle de prazo de resposta, confirmação de leitura, manifesto de interesse / carta de declínio digital

#### Etapa 5 — Portal do Fornecedor (TO BE)

O fornecedor entra em portal com identidade visual MPD e acessa:
- Caixa de entrada com pacotes enviados para cotação
- Todos os materiais do pacote (projetos via Collab Viewer, memorial, quantitativos, QC, cronograma)
- Formulário de proposta com **campos obrigatórios** (impede envio incompleto):
  - Material / Mão de obra / Mobilização (separados)
  - Condições comerciais (frete incluso, impostos, BDI, prazo de reajuste)
  - Critérios técnicos (aceite das condições de execução)
  - Condições de pagamento preferidas
- Pode também **prospectar fornecedores novos** via integração com **Bilds Match** (além da base cadastrada)

> *"Muitas vezes os fornecedores preenchem muita coisa, mas deixam campos em branco. Daí não conseguimos fazer a equalização porque um colocou uma coisa, o outro colocou outra."*

#### Etapa 6 — Mapa de Cotações e Equalização

O mapa recebe as propostas e exibe:

| Coluna | Conteúdo |
|---|---|
| Orçamento Executivo | Budget interno elaborado pela equipe técnica |
| Orçamento de Fechamento | Ajuste do executivo pela experiência da equipe de obra |
| Orçamento com INCC | Projeção com inflação da construção até a data prevista |
| Proposta Fornecedor A, B, C... | Valores recebidos por item |
| Ranking | Ordenação do mais ao menos competitivo financeiramente |
| Status | Preferência de fechamento, viabilidade por fornecedor |
| Condições aceitas | INSS, prazo de pagamento, modalidade de contrato |

**Equalização:** nivelamento de propostas que não são comparáveis diretamente (um incluiu frete, outro não; um colocou INSS, outro não declarou). Hoje em Excel com múltiplas abas auxiliares.

**Verificação cruzada com outras obras:** antes de decidir, a MPD quer saber se aquele fornecedor já está alocado em outro canteiro da carteira. Um fornecedor que já está sobrecarregado pode não ter estrutura para atender mais uma obra.

#### Etapa 7 — Aprovação e Geração de Contrato

- Aprovação do mapa pelo GGO (Gerência Geral de Obras) e Coordenação
- Justificativa de escolha registrada no sistema
- Geração de contrato: **não** acontece dentro do Visus — vai para o **DocuSign Enterprise**, que tem o fluxo jurídico da MPD embutido
- DocuSign Enterprise gerencia versões, negociação e assinatura
- Após assinatura, o fornecedor recebe acesso ao Portal do Fornecedor

#### Etapa 8 — Solicitação e Pedido no ERP

- Obra abre solicitação no Senior Mega
- Suprimentos formaliza Pedido/Contrato no Senior Mega
- **O ERP só entra aqui**: financeiro e contábil, receber NF e pagar

---

## 4. Fluxo de Execução e Medição (AS IS → TO BE)

### 4.1 Visão geral

Após contratado, o fornecedor entra em obra. O fluxo de gestão contratual passa a ter **três pilares simultâneos**:

```
FORNECEDOR SUBMET E todo mês:
┌────────────────────────────────────────┐
│  1. Avanço Físico  (via Tracking app)  │
│  2. Qualidade      (checklists, fotos, │
│                     laudos de ensaio)  │
│  3. Medição        (Boletim de Medição │
│                     conforme contrato) │
└────────────────────────────────────────┘
          ↓
MPD valida (qualidade + medição)
          ↓
Aprovação do Boletim de Medição
          ↓
Trigger automático → ERP (Senior Mega) → Pagamento
```

### 4.2 Portal do Fornecedor — Execução

O fornecedor acessa o portal e:
- Visualiza o histórico de medições aprovadas e o andamento acumulado do contrato
- Submete mensalmente:
  - **Avanço físico:** puxado do aplicativo Tracking (medição BIM)
  - **Evidências de qualidade:** fotos de campo, checklists preenchidos, laudos de ensaio (SLAMP test para estrutura, etc.), certificados
  - **Boletim de Medição:** estruturado conforme o contrato, por item e valor
- Pode incluir **medições extraordinárias** (equipamentos específicos, faturamento por terceiro)

> *"Eu me vi no fluxo porque a gente é fornecedor deles. Eu tenho que todo mês mandar Excel medindo o nosso serviço. Eles demoram dias para responder o e-mail. Se eu tivesse lugar lá para a Luísa todo mês entrar e conseguir gerar as evidências, colocar a medição, submeter — putz, aqui seria um sonho."* — Felipe

### 4.3 Validação pela MPD

A equipe da MPD:
- Recebe notificação de submissão do fornecedor
- Revisa qualidade (fotos, laudos, checklists)
- Confere medição contra o contrato e a execução real
- Pode **adicionar glosa** (desconto) se qualidade não atingida ou se houver divergência
- Aprova ou rejeita com justificativa
- Ao aprovar → trigger automático para o ERP processar pagamento

**DataBook:** ao longo de todo o processo, tudo fica registrado — fotos, laudos, medições, aprovações. Gera repositório de qualidade e histórico de desempenho de fornecedor por obra.

### 4.4 Documentação Trabalhista Exigida

A MPD exige que os fornecedores de mão de obra entreguem mensalmente junto ao BM:
- Folha de pagamento individual + resumo dos alocados
- GRF (guia de recolhimento FGTS)
- SEFIP com protocolo de conectividade
- GPS (guia previdência social)
- Comprovante de ISS, ICMS
- Comprovante de benefícios (VR, VT, cesta básica, seguro de vida, plano de saúde)
- Controle de jornada com horas extras
- PPP para colaboradores que saíram
- Rescisões com GRRF, protocolo seguro desemprego, TRCT

**Regra:** pagamento só liberado quando **todos** os documentos estão presentes.

### 4.5 Retenção

- 5% retidos sobre cada NF emitida
- Devolvidos 90 dias após assinatura do Termo de Encerramento do contrato
- Reajuste: INCC data-base configurada por contrato (ex: data-base 01/04/2024)

---

## 5. A Visão de Produto — Mock-up Apresentado para a MPD

Em **4 dias de trabalho** (Peter + Felipe + Claudio), a AltoQi materializou o seguinte conjunto de telas em mock-up e apresentou à MPD. As telas foram validadas e geraram entusiasmo imediato.

### Tela 1 — Visão Geral da Obra (Pipeline de Pacotes)

A tela central que a MPD não tinha em lugar nenhum:

```
┌──────────────────────────────────────────────────────────────────┐
│  OBRA: REFFUGIO 359 — Pipeline de Contratações                   │
│                                                                  │
│  Pacote 01 — Fundações     ████░░░░░░ [Suprimentos] ████ [Exec]  │
│  Pacote 02 — Estrutura     ██░░░░░░░░ [Suprim M1]   ████ [M3]    │
│  Pacote 03 — Instalações   ░░░░░░░░░░ [Suprim M2]   ████ [M5]    │
│  ...                                                             │
│                                                                  │
│  Linha laranja = execução (input do Planning)                    │
│  Linha azul = contratação (predecessora de suprimentos)          │
│                                                                  │
│  [Painel] 30% Curva A contratada antes do CON  ✓/✗               │
└──────────────────────────────────────────────────────────────────┘
```

> *"Essa tela foi aquela que eles travaram e pensaram: meu Deus, se eu tiver isso aqui, minha vida é outra."*

**Input:** cronograma do Planning (linhas laranja — execução)  
**Complementado no módulo:** prazos de contratação (linhas azul)  
**Permite:** simular cenários, criar novos pacotes, ver status de tudo

### Tela 2 — Painel de Gestão (Dashboard)

Visão de gestão para bater o olho e para reunião de diretoria:
- Status geral de cada pacote (em contratação / contratado / em execução / medido / encerrado)
- Quanto já foi contratado vs. quanto falta
- Ritmo de contratação
- **Visão de portfólio** (switch entre obras) — cruzamento de performance de fornecedores entre canteiros

### Tela 3 — Detalhe do Pacote (Delivery Tab)

Ao clicar em um pacote:
- **Projetos:** viewer integrado ao Colab (clicou → abre o Viewer do Colab, sem viewer próprio)
- **Memorial Descritivo:** documento anexado ou linkado do Colab
- **Quantitativos:** IFC exportado pelo Cost Management + relatórios
- **Inspeção/QC:** template de checklist de qualidade (editável por pacote)
- **Cronograma:** cronograma de execução do pacote com marcos
- **Condições Contratuais:** cláusulas padrão editáveis por pacote

> *"Uma vez esse pacote montado, completo, com tudo que ele precisa — e tudo isso aqui poderia vir do Colab — eu encaminho para os meus fornecedores."*

### Tela 4 — Portal do Fornecedor (Cotação)

Interface do fornecedor ao receber o convite:
- Caixa de entrada com pacotes disponíveis
- Visualização do pacote com todo o material
- Botão "Manifestar Interesse" (levanta a mão antes de submeter)
- Formulário guiado com campos obrigatórios:
  - Material / MO / Mobilização separados
  - Condições comerciais
  - Critérios técnicos
- Gatilho: não deixa enviar sem campos obrigatórios preenchidos
- Upload de documentos complementares

### Tela 5 — Mapa de Cotações

- Comparativo automático entre propostas recebidas
- Colunas: Orçamento Executivo / Orçamento de Fechamento / Versão INCC / Proposta A / B / C...
- Ranking automático por competitividade financeira
- Condições aceitas por fornecedor (INSS, pagamento, etc.)
- Cross-check: "esse fornecedor já está em qual outra obra?"
- Escolha com justificativa registrada

### Tela 6 — Contratação e Portal de Execução

- Fornecedor escolhido → acionamento de DocuSign Enterprise (externo)
- Após assinatura → fornecedor liberado no Portal do Fornecedor
- Interface de contrato com abas:
  - Avanço físico (pull do Tracking)
  - Qualidade (checklists, fotos, laudos)
  - Medição (BM conforme estrutura do contrato)
- Aprovação ou rejeição com glosa
- Histórico de medições anteriores
- Ao aprovar → integração ERP

---

## 6. AS IS — Plataforma Visus (Estado Atual)

| Módulo | O que faz hoje | Relevância para MPD |
|---|---|---|
| **Visus Collab** | Repositório CDE, coordenação de disciplinas, gestão de incompatibilidades, viewer IFC | Alta — CDE para projetos do pacote |
| **Visus Cost Management** | Extração de quantitativos de IFC/DWG/PDF, orçamentação, SINAPI/SICRO | Alta — quantitativos do pacote (mas precisa evoluir) |
| **Visus Planning** | EAP, cronograma, simulação 4D, planejado vs. executado | Alta — fornece as linhas laranja (cronograma de execução) |
| **Visus Bid** | Cotações de suprimentos originadas no modelo BIM | Alta — núcleo do que precisa evoluir |
| **Visus Tracking** | Medições de serviços e verificação de progresso | Alta — avanço físico e medição de campo |
| **Visus Control Tower** | Dashboards integrados a projetos BIM, orçamentos e cronogramas | Alta — mas atualmente muito granular (precisa visão macro de pacotes) |
| **Visus Workflow** | Gestão de tarefas, Kanban/Gantt | Média — fluxos de aprovação |

**Capacidades transversais:** +50 tipos de relatório, rastreabilidade orçamento↔modelo 3D, OpenBIM (IFC), integração com catálogos de fabricantes (Bilds/Bilds Match), 70.000+ clientes, 37+ anos.

**AltoQi Axis (2026):** camada de IA transversal — opera sobre todos os dados da plataforma. *"Já poderia vender com essa camada de inteligência em cima."*

---

## 7. Gap Analysis — O que falta

### 7.1 Gaps por módulo

| Processo MPD | Cobertura Atual Visus | Gap |
|---|---|---|
| Gatilho de contratação com prazo automático | ❌ | Alerta de "data de início de suprimentos" baseado no cronograma do Planning |
| Pipeline de pacotes na linha do tempo | ❌ | Tela central de Obra — pacotes × linha do tempo × status contratação/execução |
| Scope Packager (agrupar quantitativos em pacotes por subsistema) | ❌ | Cost Management é flexível demais — não obriga estrutura de pacotes |
| Geração de Carta Convite a partir do pacote | ❌ | Nenhum módulo gera documento de cotação a partir de modelo BIM |
| Portal de Fornecedores (externo, web) | ❌ | Bid não tem portal externo para fornecedor submeter proposta |
| Manifesto de interesse / carta de declínio digital | ❌ | Hoje por e-mail |
| Formulário de proposta guiado com campos obrigatórios | ❌ | Não existe |
| Mapa de Cotações com equalização | ❌ | Não existe análise comparativa digital |
| Ranking automático de fornecedores | ❌ | Não existe |
| Cross-check de fornecedor em outras obras | ❌ | Não existe |
| Workflow de aprovação de mapa (GGO/Coord.) | ❌ | Não existe |
| Geração/envio para DocuSign | ❌ | Sem integração nativa |
| Integração ERP (Senior Mega) | ❌ | Sem conector nativo |
| Portal do Fornecedor — execução (BM digital) | ⚠️ Tracking parcial | Falta: portal web para fornecedor submeter BM + qualidade + avanço físico |
| Validação de BM com glosa e aprovação | ❌ | Tracking não tem workflow de aprovação contratual |
| Checklist documental trabalhista | ❌ | Não existe — gatilho de pagamento só com docs presentes |
| Controle de retenção por contrato | ❌ | Não existe |
| DataBook automático por contrato | ❌ | Tracking não acumula histórico estruturado de fornecedor |
| Gestão de gates por fase do empreendimento | ❌ | Nenhum módulo suporta gate review com checklist |
| Control Tower com visão macro de pacotes | ⚠️ Existe mas granular demais | Precisa visão de portfólio por pacote, não por elemento BIM |
| QC em campo vinculado a elemento BIM | ❌ | Tracking não tem checklists de qualidade |

### 7.2 Gap crítico de arquitetura (discutido na reunião)

> *"O Cost Management é muito flexível. Ele pode chegar nisso, mas ele não é obrigado a chegar nisso. A grande mudança que a gente está planejando é fazer um sistema em que ele obrigue a se estruturar dentro da quebra de pacotes."*

**O problema:** o Cost Management permite qualquer estrutura de EAP. Para alimentar a visão de pacotes da Control Tower e do módulo de Procurement, ele precisa ser reformulado para ter uma **EAP mínima obrigatória** alinhada à hierarquia Obra → Pacote → Contrato.

> *"Sem ter essa base que está no Cost dessa macro EAP, a Control Tower não consegue ter essa granularidade — fica pequena, fica você não sendo tão útil."*

### 7.3 Nomenclatura a ser definida

A reunião evidenciou que a nomenclatura ainda não está consolidada. Proposta derivada da discussão:

| Nível | Nome MPD | Equivalente Visus atual | Proposta Visus TO BE |
|---|---|---|---|
| Agrupador maior | Pacote | EAP nível 1 | **Pacote** |
| Contrato por fornecedor | (sem nome definido) | — | **Contrato** |
| Divisão de medição dentro do contrato | "Plano de ataque" / "marcos de medição" | Atividade | **Marco de Medição** |
| Subdivisão técnica do pacote | (sub-pacote, ex: estrutura metálica separada da estrutura de concreto) | — | **Subpacote** ou novo Pacote |

---

## 8. TO BE — Evoluções Necessárias

### 8.1 Horizonte 1 — Procurement Digital (Impacto imediato)

#### Novo módulo: **Visus Procurement** (evolução do Bid)

**Objeto central:** o **Pacote** como entidade persistente com ciclo de vida gerenciado.

**Funcionalidades:**

**a) Scope Packager**
- Agrupa itens de quantitativo (do Cost Management) em Pacotes por subsistema construtivo
- Estrutura obrigatória: Obra → Pacote → Contrato
- Herda lista de projetos do Colab (com status de revisão)
- Gera os 5 pilares do pacote automaticamente a partir dos inputs disponíveis na plataforma

**b) Timeline de Pacotes**
- Visualização de todos os pacotes da obra na linha do tempo
- Linha laranja = execução (input do Planning)
- Linha azul = contratação (configurável com lead time de suprimentos por tipo de pacote)
- Alerta automático para suprimentos quando o gatilho de contratação é atingido
- Simulação de cenários (antecipação/atraso de contratação e impacto na obra)
- Dashboard de portfólio: todas as obras × status de pacotes × % curva A contratada

**c) Geração de Carta Convite**
- Template parametrizado que importa automaticamente:
  - Dados do empreendimento (do projeto Collab)
  - Imagens do modelo BIM (captura da simulação 4D do Planning)
  - Lista de projetos com revisão e status (do Colab)
  - Quantitativos (do Cost Management)
  - Cronograma de execução do pacote (do Planning)
  - Condições contratuais padrão (biblioteca de cláusulas por tipo de pacote)
- Gera PDF/Word editável para revisão antes do envio
- Registro de versões e histórico de alterações

**d) Portal de Fornecedores (externo)**
- Interface web acessível sem instalação de software
- Identidade visual configurável por empresa (ex: MPD Engenharia)
- Caixa de entrada com convites recebidos
- Viewer integrado ao Colab (sem viewer próprio)
- Formulário de proposta guiado com campos obrigatórios por tipo de pacote
- Manifesto de interesse ou carta de declínio digital com prazo
- Gatilho: impede envio se campos obrigatórios não preenchidos
- Integração com **Bilds Match** para prospecção de novos fornecedores

**e) Mapa de Cotações Digital**
- Recebe propostas automaticamente do Portal do Fornecedor
- Exibe comparativo: Orçamento Executivo / Orçamento de Fechamento / Versão INCC / Propostas recebidas
- Equalização: campos configuráveis para nivelar condições (frete, impostos, BDI, INSS)
- Ranking automático por competitividade financeira
- Flag de condições aceitas (pagamento, modalidade)
- Cross-check: fornecedor alocado em outras obras da carteira (alerta de sobrecarga)
- Escolha de fornecedor com justificativa registrada

**f) Workflow de Aprovação**
- Configuração de alçadas por tipo/valor (ex: GGO aprova acima de R$ X)
- Notificação, prazo de resposta, aprovação ou retorno com comentário
- Registro completo do histórico de aprovações

#### Integração DocuSign

- Ao selecionar fornecedor → sistema abre processo DocuSign Enterprise
- Passa dados do pacote e condições contratadas para pre-populate o template
- Acompanha status da assinatura dentro do Visus
- Ao assinar → fornecedor liberado no Portal de Execução

#### Integração ERP (Senior Mega)

- Ao concluir fluxo de aprovação → exporta solicitação de pedido/contrato para o ERP
- Evita dupla entrada; o ERP recebe o que precisa para processar financeiro e contábil
- Pode ser via API REST, webhook ou exportação estruturada conforme capacidade do Senior Mega

---

### 8.2 Horizonte 2 — Gestão Contratual de Execução

#### Evolução: **Visus Tracking** + **Portal do Fornecedor — Execução**

**Boletim de Medição Digital**
- Estrutura do BM derivada do contrato (itens, valores, percentuais)
- Fornecedor submete pelo portal (web ou app mobile)
- Avanço físico puxado automaticamente do Tracking
- Upload de evidências de qualidade (fotos, laudos, checklists)
- Campos obrigatórios configuráveis por pacote (ex: SLAMP test para estrutura)
- Medições extraordinárias possíveis (fora da estrutura planejada)

**Workflow de Aprovação do BM**
- Equipe de obra: verificação de qualidade + conferência de medição
- Adição de glosa com justificativa (desconto por não conformidade)
- Aprovação final → trigger automático para ERP
- Rejeição → notificação ao fornecedor com motivo
- Histórico completo de medições por contrato

**Checklist Documental Trabalhista**
- Lista de documentos exigidos configurável por tipo de contrato (mão de obra vs. material)
- Status de cada documento (pendente / recebido / vencido)
- Sistema não libera trigger de pagamento enquanto documentação incompleta
- Alertas de vencimento (ex: guia FGTS mensal)

**Controle de Retenções**
- Campo de % de retenção por contrato (padrão MPD: 5%)
- Cálculo automático na medição
- Controle do prazo de devolução (90 dias após Termo de Encerramento)
- Dashboard de retenções a devolver por período

**DataBook**
- Acumulação automática de todo o histórico do contrato:
  - Fotos e laudos de qualidade
  - Medições aprovadas/rejeitadas
  - Comunicações e decisões registradas
- Permite aprendizado entre obras: como foi a performance deste fornecedor neste tipo de pacote?
- Base para qualificação de fornecedores e benchmark

---

### 8.3 Horizonte 3 — Backbone de Pacotes (Reformulação do Cost)

**O problema a resolver:** o Cost Management hoje é livre demais. Precisa de uma EAP mínima obrigatória que force a estrutura Obra → Pacote → Contrato para que toda a plataforma possa se beneficiar da mesma hierarquia.

**Evolução necessária:**
- Configuração de **EAP mínima obrigatória** por tipologia de obra (template)
- Pacote como objeto de primeira classe no Cost: cada item de custo pertence a um Pacote
- A hierarquia do Cost alimenta o Procurement, o Planning, o Tracking e a Control Tower com o mesmo agrupamento
- Templates de tipologia (residencial incorporação, industrial, saúde) com pacotes pré-configurados (Curva A padronizada)

> *"Esse conceito de dividir a obra em blocos desde a concepção precisa ser padronizado e fluir de fase a fase. Sempre: quais pacotes compõem essa fase? Quais são os entregáveis dessa fase para handover para a próxima?"*

---

### 8.4 Horizonte 4 — Control Tower com Visão Macro de Pacotes

**O problema atual:** a Control Tower mostra indicadores muito granulares. Para a MPD — e para qualquer visão de portfólio — o que importa é a visão de pacote, não de elemento BIM individual.

**Evolução necessária:**
- Painel de obra por Pacote: status, % executado, % medido, % pago
- Painel de portfólio: todas as obras × % Curva A contratada × alertas de atraso de contratação
- Benchmark: Pacote 02 (Estrutura) — comparação de custo/m³, prazo de ciclo, fornecedor por obra
- Consultas via Axis (IA): *"quais pacotes estão com risco de atraso de contratação nos próximos 30 dias?"*

---

### 8.5 Horizonte 5 — Gates e Lifecycle

**Evolução necessária:**
- Gate como objeto configurável no projeto: checklist de critérios de aprovação por gate
- Rastreamento de entregáveis por fase com status (emitido / em revisão / aprovado / reprovado)
- Notificação quando gate tem critérios pendentes
- Dashboard multi-obra de gates: em que fase está cada empreendimento? Quais gates têm bloqueios?

---

### 8.6 Horizonte 6 — QC em Campo e Design Review

**QC em campo:**
- Checklists de controle de qualidade vinculados ao elemento BIM
- Registro de não conformidades (RNC) com evidência fotográfica, responsável, prazo, ação corretiva
- Critério de liberação de pavimento: QC completo = prerequisito para próxima etapa
- Diário de obra digital (entrada/saída de equipamentos, efetivo diário)

**Design Review:**
- Registro de decisões de reengenharia no modelo Colab (antes/depois)
- Comparação de alternativas com impacto em custo (Cost) e cronograma (Planning)
- Ata digital de design review com rastreabilidade de mudanças de escopo

---

### 8.7 Horizonte 7 — Gestão do Ativo (Pós-Habite-se)

**Evolução necessária:**
- Checklists de comissionamento por sistema (elevador, água, elétrica, gerador, gás)
- Registro de aprovações de concessionárias
- As-Built digital (modelo BIM atualizado com condições reais)
- Manual do condomínio/proprietário digital gerado a partir do projeto
- Controle de garantias por subsistema com alertas de vencimento

---

## 9. Priorização Estratégica

### Matriz de Impacto vs. Esforço

| # | Evolução | Impacto para MPD | Esforço Visus | Prioridade |
|---|---|---|---|---|
| 1 | Timeline de Pacotes (Pipeline view) | 🔴 Alto | 🟡 Médio | **P1** |
| 2 | Scope Packager + Geração de Carta Convite | 🔴 Alto | 🟡 Médio | **P1** |
| 3 | Portal do Fornecedor (cotação) + Formulário guiado | 🔴 Alto | 🟡 Médio | **P1** |
| 4 | Mapa de Cotações + Equalização + Ranking | 🔴 Alto | 🟡 Médio | **P2** |
| 5 | Workflow de Aprovação de Mapa (alçadas) | 🔴 Alto | 🟢 Baixo | **P2** |
| 6 | Integração DocuSign | 🔴 Alto | 🟢 Baixo | **P2** |
| 7 | Boletim de Medição Digital + Aprovação | 🔴 Alto | 🟡 Médio | **P2** |
| 8 | Checklist Documental Trabalhista | 🟡 Médio | 🟢 Baixo | **P3** |
| 9 | Controle de Retenções | 🟡 Médio | 🟢 Baixo | **P3** |
| 10 | Integração ERP (Senior Mega) | 🔴 Alto | 🔴 Alto | **P3** |
| 11 | Reformulação do Cost (EAP obrigatória de pacotes) | 🔴 Alto | 🔴 Alto | **P3** |
| 12 | Control Tower com visão macro de pacotes | 🔴 Alto | 🟡 Médio | **P3** |
| 13 | Cross-check fornecedor entre obras | 🟡 Médio | 🟡 Médio | **P4** |
| 14 | DataBook e qualificação de fornecedores | 🟡 Médio | 🟡 Médio | **P4** |
| 15 | QC em campo vinculado ao BIM | 🟡 Médio | 🟡 Médio | **P4** |
| 16 | Gates e Lifecycle management | 🟡 Médio | 🔴 Alto | **P5** |
| 17 | Design Review / Engenharia de Valor | 🟡 Médio | 🔴 Alto | **P5** |
| 18 | Gestão do Ativo / Comissionamento | 🟢 Baixo (CP) | 🔴 Alto | **P6** |

---

## 10. Narrativa Central do Produto

> *"O Visus que a MPD precisa não é o Visus que vende BIM — é o Visus que vende ciclo de vida de contrato."*

A MPD já aceita o BIM. O modelo existe, os quantitativos existem, o cronograma existe. O problema começa **depois**: o quantitativo vai para um Excel, vira Carta Convite em Word, as propostas chegam por e-mail, a equalização é feita em planilha, a aprovação acontece em reunião ou Whatsapp, a minuta vai para o suprimentos, o contrato assina no DocuSign, o pedido entra no Senior Mega — e nada disso conversa com o modelo BIM original.

**O gap central não é BIM. É a camada de procurement e contratos.**

O Visus Bid precisa se tornar um **módulo de procurement de obra completo** — do quantitativo ao contrato assinado. O Visus Tracking precisa se tornar um **módulo de gestão contratual de execução** — da medição ao pagamento liberado. Esses dois módulos, integrados pelo **Pacote como objeto central e persistente**, entregariam à MPD o que ela não tem hoje:

> **Rastreabilidade completa entre o elemento BIM → o pacote → o contrato → a medição → o pagamento.**

E com Axis operando sobre todos esses dados:
> **Inteligência sobre fornecedores, benchmarks entre obras, alertas preditivos de atraso de contratação.**

O Fábio (diretor da MPD) disse ao ver o mock-up: *"Filipe, estou atendendo esse fluxo — tu está atendendo no mínimo umas 1.500 construtoras no Brasil porque esse fluxo, pelo menos as primeiras linhas, não muda muito."*

---

## 11. Perguntas para Próximas Rodadas de Descoberta

1. **Escopo do piloto:** a MPD quer começar pela Curva A de quais obras? O Reffugio 359 seria o primeiro canteiro piloto?
2. **Estrutura de aprovação (alçadas):** qual é exatamente a hierarquia? GGO aprova qualquer valor? Acima de qual valor entra o diretor?
3. **DocuSign Enterprise:** o fluxo jurídico já está configurado no DocuSign da MPD? O Visus precisa apenas disparar um webhook ou é preciso construir template de contrato na integração?
4. **Integração Senior Mega:** é uma exigência dura (Visus alimenta o Senior obrigatoriamente) ou existe abertura para o Visus substituir a parte de gestão de compras/contratos e o Senior ficar só com financeiro/contábil?
5. **A Máscara de Medição Excel:** ela é padronizada entre obras ou cada engenheiro monta a sua? Quem formalmente aprova a medição (só o GGO ou também o coordenador de obra)?
6. **Curva B/C:** a MPD aceita começar com Curva A apenas ou quer visibilidade de Curva B/C desde o início (mesmo que gerida pelo canteiro)?
7. **DataBook e qualificação de fornecedores:** isso é uma necessidade real de curto prazo ou visão futura? Já existe algum sistema de avaliação de fornecedores hoje?
8. **O "Design Review"** é formal (reunião com pauta e ata) ou informal? Quem documenta as decisões de reengenharia hoje e como chegam ao suprimentos?
9. **Modelo de licenciamento esperado:** a MPD imagina pagar por canteiro? Por usuário? Por módulo? Qual é a expectativa de investimento?

---

*Documento produzido a partir de exploração de produto realizada na MPD Engenharia. Materiais utilizados: gravação de reunião interna AltoQi (30/04/2026) com apresentação de mock-ups à MPD; Carta Convite Reffugio 359; Fluxos de Contratação (Mão de Obra e Material); Método dos Pacotes de Entrega — AltoQi (framework HTML); Máscara de Medição Estrutura (Excel); QC Estrutura (Excel); Quantitativos de Estrutura (Excel).*

---

## Related Pages

- [[projects/mpd-visus-evolucao-plataforma]]
- [[projects/altoqi-visus-planning]]
- [[projects/altoqi-axis]]
- [[projects/finep-mais-inovacao-brasil-2026]]
- [[projects/altoqi-company]]
- [[bim-construction/gt-antac-visus-planning-objeto-aprendizagem]]
- [[bim-construction/altoqi-finep-axis-2026]]
- [[bim-construction/construcao-40]]
- [[bim-construction/tipos-contrato-engenharia]]
- [[bim-construction/planejamento-preditivo-obras]]
- [[glossary]]
