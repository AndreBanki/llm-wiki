---
title: "Planejamento da Construção com AltoQi Visus Planning — Objeto de Aprendizagem (módulos 1–4)"
type: source
created: 2026-04-26
updated: 2026-04-26
sources: [Planejamento da Construção com AltoQi Visus Planning_ objeto de aprendizagem módulo 1_4.md, Planejamento da Construção com AltoQi Visus Planning_ objeto de aprendizagem módulo 2_4.md, Planejamento da Construção com AltoQi Visus Planning_ objeto de aprendizagem módulo 3_4.md, Planejamento da Construção com AltoQi Visus Planning_ objeto de aprendizagem módulo 4_4.md]
tags: [altoqi, visus-planning, bim, planejamento-4d, ifc, eap, cronograma, simulacao, construção, mdic, construa-brasil]
---

Série de 4 vídeos tutoriais do Projeto Construa Brasil (MDIC) demonstrando o workflow completo de planejamento 4D com AltoQi Visus Planning. Cobertura end-to-end: importação de modelo federado → EAP → cronograma → simulação → relatórios.

## Metadata

| Campo | Valor |
|---|---|
| **Autor / Instrutora** | Mariana Farias (Núcleo de Inovação BIM — NIB) |
| **Coordenação** | Profa. Dra. Regina C. Ruschel (RECEPTi) |
| **Canal** | GT TIC ANTAC |
| **Autoria institucional** | Projeto Construa Brasil, MDIC |
| **Publicado** | 2025-05-06 |
| **URL Módulo 1** | https://www.youtube.com/watch?v=nc07E3T7xZY |
| **URL Módulo 2** | https://www.youtube.com/watch?v=9cI46o0o1WA |
| **URL Módulo 3** | https://www.youtube.com/watch?v=4fIEE4tSwGE |
| **URL Módulo 4** | https://www.youtube.com/watch?v=UudgDfSIhqY |
| **Versão do produto** | Visus Planning 2024 |
| **Projeto de referência** | Habitação de interesse social CDHU, Campinas-SP (Bloco H) |

---

## Contexto: Projeto Construa Brasil

Iniciativa do MDIC (Ministério do Desenvolvimento, Indústria, Comércio e Serviços) para modernização do setor da construção civil no Brasil. Os Objetos de Aprendizagem BIM (OA BIM) são produtos pedagógicos distribuídos gratuitamente via Portal BIM Acadêmico, desenvolvidos para capacitação de professores, estudantes e profissionais.

---

## Módulo 1 — Interface e Importação do Modelo Federado

### Tela de entrada
- Links de apoio e suporte organizados por tema e barra de busca
- Projetos-exemplo pré-configurados para referência
- Menu principal no centro: abrir projeto, novo projeto a partir de…

### Criação de projeto
Dois pontos de partida a partir de IFC:
- **A partir do IFC (diretório local):** carrega diretamente do diretório da máquina
- **A partir do IFC no Visus Colab:** carrega da plataforma em nuvem

### Templates de tipologia
- Ao abrir um IFC, o sistema oferece a seleção de um template de projeto
- Templates são padrões de estrutura de projeto (ex: edifício vertical, conjunto horizontal) salvos para reuso em projetos futuros

### Importação do modelo federado
1. Selecionar o IFC de arquitetura como arquivo base
2. Adicionar IFCs de estrutura, elétrica e hidráulica via botão `+`
3. O modelo federado aparece com todos os IFCs carregados

### Status dos modelos IFC
| Status | Indicação | Significado |
|---|---|---|
| 🟢 Verde | Modelo atualizado | OK para uso |
| ⚠️ Amarelo | Modelo desatualizado | Versão mais nova disponível na mesma pasta |
| 🔴 Vermelho | Caminho inválido | Arquivo movido ou excluído — caminho deve ser reconfigurado |

### Filtros de configuração
- **Ativo/inativo por modelo:** modelo inativo não aparece no projeto
- **Filtro por elemento:** dentro de cada modelo, possível ativar/desativar entidades IFC específicas

### Leitura automática de quantitativos
O Visus lê os modelos importados e organiza automaticamente:
- **Por disciplina** (arquitetura, estrutura, instalações) — inferido do IFC
- **Por pavimento** — baseado nos níveis definidos no modelo
- **Por elemento** — entidades IFC com unidade de medida padrão (janela = un, parede = m², etc.)

### Isolamento por propriedade IFC
Para montar a sequência construtiva de paredes (exemplo do vídeo):
1. Filtrar entidade `IfcWall` → selecionar → isolar
2. Verificar propriedades via aba Metadados para segmentar (ex: material)
3. Excluir elementos indesejados do conjunto (ex: paredes de concreto do reservatório)

---

## Módulo 2 — Quantitativos e Definição da EAP

### Inserção do modelo do canteiro de obras
- Adiciona como um IFC adicional nas configurações
- Por padrão é classificado em "Estrutura" — corrigir para "Outros" para mantê-lo separado

### Análise de metadados IFC
Aba **Metadados** exibe todas as propriedades do elemento selecionado:
- Disciplina, entidade, nome, ID, pavimento
- Propriedades de modelagem (dimensionamento, armadura, etc.)
- **Propriedades geométricas calculadas pelo Visus** (não vêm do IFC):

| Propriedade | O que mede |
|---|---|
| Área da projeção superior | Face superior do elemento |
| Área da projeção lateral | Face lateral |
| Área da projeção frontal | Face frontal |
| Altura da caixa delimitadora | Altura total |
| Largura da caixa delimitadora | Largura total |

O ícone de olho ao lado de cada propriedade destaca no modelo 3D qual área está sendo calculada — ferramenta de validação da especificação.

### Edição de classificação de entidade
- É possível reclassificar entidades IFC diretamente no Visus (ex: `IfcFlowMovingDevice` → `IfcSanitaryTerminal`)
- **Importante:** a edição é feita em cópia local — não modifica o IFC original. Se o IFC for recarregado, a reclassificação é perdida.

### Definição da EAP
A EAP é definida na aba de **Quantitativo** (não de Planejamento). Isso é central: a mesma estrutura alimenta quantitativo, orçamento e planejamento.

Dois caminhos de acesso à configuração da EAP:
- Menu principal → Configurações → aba EAP
- Atalho no canto superior direito: "Configurar EAP"

Estrutura de 5 níveis:

| Nível | Nomenclatura |
|---|---|
| 1 | Etapa |
| 2 | Subetapa |
| 3 | Subetapa do nível 2 |
| 4 | Subetapa do nível 3 |
| 5 | Subetapa do nível 4 |

Os critérios de cada nível são definidos a partir das propriedades disponíveis nos metadados (disciplina, pavimento, elemento, ambiente, etc.).

### Exemplo de EAP adotada no projeto
```
1. Disciplina (Fundação / Superestrutura / Instalações / Arquitetura)
  1.1. Elemento (Estaca / Sapata / Laje / Parede / …)
    1.1.1. Pavimento (Térreo / 1º Pavimento / …)
      1.1.1.1. Setor (Bloco A / Bloco B / Ligação)
```

---

## Módulo 3 — Cronograma e Setorização

### Configuração do calendário de obra
Menu principal → Configurações → aba Planejamento 4D:
- Dias úteis e carga horária por dia (segunda a sábado por padrão)
- Feriados e dias com turno reduzido
- Opção de trabalho no domingo

### Configuração de atividades no cronograma
Aba **Planejamento**: cada elemento/atividade da EAP recebe:
- Data de início (manual ou por predecessora)
- Duração (em dias úteis, conforme calendário)
- Data de conclusão (calculada automaticamente)

### Predecessoras
| Tipo | Significado |
|---|---|
| Término a Início (TI) | Atividade começa quando a anterior termina |
| Início a Início (II) | Atividades começam juntas |
| Latência | Espera N dias após a predecessora antes de iniciar |
| Múltiplas predecessoras | Atividade aguarda conclusão de várias predecessoras |

### Gantt integrado
Ícone no canto superior direito ativa o Gráfico de Gantt. Ao clicar em uma barra: exibe duração, data de início e data de fim. As barras são editáveis diretamente no Gantt.

### Setorização por coordenadas X/Y
Para dividir o projeto em setores que não têm propriedade de setor no IFC original:
1. Selecionar um elemento na extremidade do setor desejado
2. Verificar coordenadas X/Y na aba Metadados
3. No filtro de seleção de elementos: usar condição `X > [valor]` ou `X < [valor]`
4. Selecionar todos os elementos do trecho
5. Preencher o campo **Ambiente** nos metadados com o nome do setor (ex: "Bloco A")
6. Salvar — o setor torna-se um critério disponível na configuração da EAP

---

## Módulo 4 — Simulação 4D, Validação e Relatórios

### Animação 4D
Ícone "Executar animação 4D" (canto superior direito). Dois modos:

**Modo 1 — Data específica:**
- Selecionar uma data → visualizar estado da obra naquele dia
- Elementos executados = cores sólidas; elementos em execução = transparentes

**Modo 2 — Simulação com play:**
- Definir duração da animação (ex: 20s, 60s)
- Play → animação reproduz a sequência construtiva completa
- Comandos de visualização (rotacionar, ocultar, isolar) permanecem ativos durante a animação

Uso para validação: identificar atividades fora de sequência, serviços que aparecem antes do que deveriam.

**Limitação conhecida:** não há exportação nativa de vídeo da animação — recomendação: tela cheia + ferramenta de captura de tela externa.

### Rastreamento Planejado vs. Executado
Três abas no cronograma:
| Aba | Conteúdo |
|---|---|
| Planejado | Datas e durações previstas |
| Executado | Datas reais + percentual de execução por atividade |
| Ambos | Comparativo planejado × realizado |

O Gantt em modo "Ambos" exibe simultaneamente as barras do planejado e do executado — permite identificar descolamentos (atividades atrasadas ou adiantadas).

### Relatórios disponíveis
| Relatório | Fonte de dados | Formato |
|---|---|---|
| Curva S | Orçamento + cronograma integrados | Gráfico in-app |
| Histograma de mão de obra | Composições orçamentárias por período | Gráfico in-app (semana/mês/ano, quantidade de horas ou custo) |
| Orçamento por etapa de obra | EAP + valores do orçamento | Excel editável |

---

## Fluxo Completo: Visão de Processo

```
IFCs → Modelo Federado
    → Template de tipologia
    → Análise de metadados / propriedades geométricas
    → EAP (aba Quantitativo) ←→ Orçamento ←→ Planejamento
    → Setorização (campo Ambiente por coordenadas X/Y)
    → Calendário de obra
    → Cronograma (datas + durações + predecessoras)
    → Simulação 4D (validação visual)
    → Rastreamento Planejado vs. Executado
    → Relatórios (Curva S / Histograma / Excel)
```

---

## Related Pages

- [[projects/altoqi-visus-planning]]
- [[bim-construction/planejamento-preditivo-obras]]
- [[bim-construction/bim-coordination]]
- [[bim-construction/tipos-contrato-engenharia]]
- [[bim-construction/jhonatan-lazarin-ia-gestao-obras]]
