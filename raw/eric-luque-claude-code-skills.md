# Skills no Claude Code: O Guia Definitivo Para Quem Quer Parar de Subutilizar a Ferramenta Mais Poderosa da IA Agentica

**Author:** Eric Luque (Co-founder Ecotrace)  
**Published:** April 18, 2026  
**Source:** LinkedIn Pulse  
**URL:** https://www.linkedin.com/pulse/skills-claude-code-o-guia-definitivo-para-quem-quer-parar-eric-luque-kosuf/

---

Existe um recurso no Claude Code que a maioria dos desenvolvedores ignora ou usa de forma superficial. Skills. E o que me incomoda é que a documentação oficial trata isso como se fosse mais uma feature qualquer, quando na prática é o mecanismo que separa quem usa Claude Code como um autocomplete glorificado de quem usa como um engenheiro autônomo dentro do time.

Recentemente li um artigo do Mario Tort, engenheiro da Anthropic, onde ele compartilha como a equipe interna usa centenas de skills em produção. O que vou fazer aqui não é traduzir o artigo dele. É destrinchar cada conceito, adicionar o que aprendi na prática, e entregar para você um guia que você pode usar amanhã de manhã.

## O que são Skills, de verdade

A primeira coisa que precisa morrer é a ideia de que skill é um arquivo Markdown com instruções. Isso é como dizer que um carro é uma cadeira com rodas. Tecnicamente não está errado, mas você perdeu a parte que importa.

Uma skill é uma **pasta**. E essa pasta pode conter scripts, assets, dados, templates, documentos de referência, exemplos de código, configurações e qualquer outro recurso que o agente precise para executar uma tarefa com competência. O arquivo Markdown principal funciona como o ponto de entrada, ele diz ao Claude quando e como usar aquele conjunto de recursos. Mas o poder real está no que vem junto.

Pense assim: se o Claude Code é um estagiário extremamente inteligente mas sem contexto da empresa, a skill é o onboarding completo que transforma esse estagiário em alguém produtivo no primeiro dia. Não é uma lista de regras. É um kit de sobrevivência.

A estrutura típica de uma skill:

```
.claude/skills/minha-skill/
  skill.md          # Ponto de entrada com instruções
  config.json       # Configurações do usuário
  references/       # Documentação de apoio
    api-docs.md
    architecture.md
  assets/           # Templates e boilerplate
    template-component.tsx
    migration-base.sql
  scripts/          # Scripts auxiliares
    validate.sh
    seed-data.py
  examples/         # Exemplos de uso
    basic-usage.md
    advanced-patterns.md
```

Quando o Claude invoca uma skill, ele tem acesso a tudo isso. Ele pode ler a documentação, executar os scripts, usar os templates como base e consultar os exemplos antes de tomar qualquer decisão.

## As 9 categorias que cobrem 90% dos casos

### 1. Referência de Bibliotecas e APIs

**O problema que resolve:** o Claude conhece bibliotecas populares, mas erra nos detalhes. Ele vai sugerir um método que existia na v2 mas foi removido na v3. Vai usar a assinatura errada de uma função interna. Vai ignorar uma limitação conhecida que não está na documentação oficial.

**Como funciona:** você cria uma skill que contém a documentação atualizada da biblioteca, com foco nas partes que o Claude erra com frequência. Não é pra duplicar a documentação inteira, é pra preencher as lacunas.

Exemplos práticos:
1. **billing-lib:** documentação de uma biblioteca interna de cobrança, com os edge cases que só quem usa em produção conhece
2. **internal-platform-cli:** subcomandos, flags e exemplos de uma CLI proprietária
3. **frontend-design:** regras do design system, incluindo os clichês que devem ser evitados (tipo usar Inter com gradiente roxo em tudo)

O que incluir:
- Pasta examples/ com casos de uso reais
- Seção de gotchas (erros comuns que o Claude comete)
- Versão atual da biblioteca e breaking changes recentes
- Padrões de uso aprovados vs. padrões que parecem corretos mas causam problemas

### 2. Verificação de Produto

**O problema que resolve:** o Claude pode escrever código que compila, passa nos testes unitários e ainda assim está errado. Um formulário de cadastro pode renderizar perfeitamente nos testes mas ter um campo que não aparece no viewport mobile. Um fluxo de checkout pode funcionar com dados ideais mas quebrar com um cartão de teste específico.

**Como funciona:** skills de verificação usam ferramentas externas (Playwright, Cypress, tmux) para testar o comportamento real do código.

Exemplos práticos:
1. **signup-flow-driver:** abre um navegador headless, preenche o formulário de cadastro, verifica redirecionamento e criação do usuário
2. **checkout-verifier:** testa o fluxo completo de compra com cartões de teste do Stripe, incluindo cenários de falha
3. **tmux-cli-driver:** para CLIs que exigem um TTY real, usa tmux para simular a interação

### 3. Recuperação e Análise de Dados

**O problema que resolve:** o Claude não tem acesso aos seus dashboards, ao seu data warehouse, às suas métricas.

**Como funciona:** a skill fornece bibliotecas auxiliares para consultar seus sistemas de dados, junto com credenciais e instruções de workflow.

Exemplos práticos:
1. **funnel-query:** junta eventos de diferentes fontes para montar funis de conversão
2. **cohort-compare:** analisa retenção e conversão entre cohorts de usuários
3. **grafana:** mapeia dashboards existentes para que o Claude saiba onde buscar métricas específicas

### 4. Processos de Negócio e Automação de Time

**O problema que resolve:** todo time tem tarefas repetitivas que consomem tempo mas não exigem criatividade.

**Como funciona:** a skill automatiza o processo inteiro, incluindo a coleta de informações de múltiplas fontes e a formatação do resultado.

Exemplos práticos:
1. **standup-post:** agrega informações do task tracker, GitHub e Slack para gerar a daily automaticamente
2. **create-ticket:** garante que todo ticket siga o schema correto e executa as ações pós-criação
3. **weekly-recap:** compila PRs mergeados, tickets fechados e deploys feitos durante a semana

**Detalhe importante:** essas skills frequentemente usam logs persistentes. Um arquivo standups.log dentro da pasta da skill (ou em `${CLAUDE_PLUGIN_DATA}`) funciona como uma memória que sobrevive entre sessões.

### 5. Templates de Código e Scaffolding

**O problema que resolve:** cada time tem seus padrões. Quando alguém cria um novo serviço, uma nova migration, um novo componente, existem dezenas de decisões que já foram tomadas.

**Como funciona:** a skill combina templates pré-prontos com scripts de scaffolding.

Exemplos práticos:
1. **new-workflow:** scaffolding completo de um novo serviço, incluindo docker-compose, CI e testes
2. **new-migration:** template de migration com rollback, validação e seed data
3. **create-app:** aplicação interna pré-configurada com auth, logging e monitoring

### 6. Qualidade de Código e Code Review

**O problema que resolve:** manter padrões de qualidade em um time é difícil. Reviews são inconsistentes.

**Como funciona:** skills de qualidade podem funcionar como ferramentas invocadas manualmente ou como hooks automáticos (pré-commit, pré-push, GitHub Actions).

Exemplos práticos:
1. **adversarial-review:** usa sub-agentes para fazer múltiplas rodadas de crítica no código
2. **code-style:** enforcement de estilo com scripts determinísticos
3. **testing-practices:** guia de como testar diferentes tipos de código no contexto específico do projeto

### 7. CI/CD e Deploy

**O problema que resolve:** deploy não é só git push. É monitorar o pipeline, esperar os checks passarem, lidar com conflitos de merge, decidir se faz rollback ou avança.

**Como funciona:** skills de deploy orquestram todo o processo, frequentemente referenciando outras skills.

Exemplos práticos:
1. **babysit-pr:** monitora o PR após o push, retenta checks flaky, resolve conflitos de merge
2. **deploy-service:** faz deploy com shift gradual de tráfego (canary), monitorando métricas e fazendo rollback automático
3. **cherry-pick-prod:** gerencia cherry-picks para produção usando worktrees isoladas

### 8. Runbooks

**O problema que resolve:** quando algo quebra em produção, o engenheiro de plantão precisa investigar rapidamente usando múltiplas ferramentas.

**Como funciona:** a skill mapeia sintomas para ferramentas de investigação e produz um relatório estruturado no final.

Exemplos práticos:
1. **service-debugging:** dado um sintoma, executa a sequência de investigação: verifica métricas, correlaciona com deploys recentes, analisa logs
2. **oncall-runner:** recebe um alerta e executa a investigação inicial automaticamente
3. **log-correlator:** rastreia uma requisição específica através de múltiplos serviços usando trace IDs

### 9. Operações de Infraestrutura

**O problema que resolve:** manutenção de infraestrutura envolve operações que podem ser destrutivas.

**Como funciona:** a skill inclui guards de segurança que impedem ações destrutivas sem confirmação explícita.

Exemplos práticos:
1. **resource-orphans:** identifica recursos cloud que não estão mais em uso, mas pede confirmação antes de deletar
2. **dependency-management:** gerencia atualizações de dependências com processo de aprovação
3. **cost-investigation:** analisa a fatura cloud e identifica gastos anômalos

**Guard rails são obrigatórios aqui.** Nenhuma skill de infraestrutura deveria executar `rm -rf`, `DROP TABLE`, force-push, ou `kubectl delete` sem confirmação humana. Isso se implementa com hooks no PreToolUse.

## Como Construir Skills Que Funcionam de Verdade

### Não escreva o óbvio

O Claude Code já sabe muito sobre o seu codebase. Foque no que o Claude **não pode inferir**:
- Decisões de design que não estão documentadas no código
- Restrições políticas ou organizacionais
- Gotchas que só quem operou o sistema em produção conhece
- Preferências estéticas que não são capturadas por linters

### A seção de Gotchas é o conteúdo mais valioso

"O conteúdo mais valioso de qualquer skill é a seção de gotchas" (Mario Tort, Anthropic).

Gotchas são os erros que o Claude comete repetidamente. As melhores skills da Anthropic começaram com "poucas linhas e um único gotcha" e cresceram organicamente à medida que novos edge cases apareciam.

Exemplo de seção de gotchas:

```markdown
## Gotchas

### Não use findOne sem .lean() em queries de leitura
O Mongoose retorna documentos completos por padrão. Sem isso, cada query aloca ~3x mais memória do que o necessário.

### O campo status aceita null no banco mas não na API
A migration original permitiu null, mas o schema da API valida como required. Sempre use o valor default "pending".

### Testes de integração precisam rodar com --runInBand
Os testes compartilham a instância do banco de teste. Se rodarem em paralelo, vão interferir uns nos outros.
```

### Use a estrutura de pastas como ferramenta de context engineering

O sistema de arquivos não é só organização, é uma ferramenta de engenharia de contexto. **Progressive disclosure aplicado a prompts de IA.** O arquivo principal da skill dá a visão geral e as regras. As subpastas contêm os detalhes que o Claude consulta sob demanda.

### Mantenha flexibilidade, não seja um micromanager de IA

Skills muito rígidas quebram assim que aparece um caso que você não previu. Dê ao Claude a informação necessária, mas deixe espaço para ele adaptar a abordagem ao contexto específico.

**Ruim:** 1. Sempre crie o arquivo no diretório src/components 2. Use o nome PascalCase...

**Bom:** "Componentes seguem a convenção do projeto: PascalCase, em src/components/, com interface de Props tipada. Veja examples/component-pattern.tsx para o padrão atual. Adapte conforme a complexidade do componente."

### Configure com config.json, não com hardcode

Armazene configurações em um config.json dentro do diretório da skill. Se o arquivo não existir, o Claude pergunta ao usuário usando a ferramenta AskUserQuestion.

### Escreva descriptions para o modelo, não para humanos

O campo description de uma skill não é um resumo. É o conjunto de condições que determina quando o Claude deve considerar invocar aquela skill.

**Ruim:** `"Skill para fazer deploy de serviços na AWS"`

**Bom:** `"Use quando o usuário pedir para deployar, publicar ou subir um serviço. Também quando mencionar staging, produção, canary, rollback, ou quando um PR for aprovado e precisar ir para produção."`

### Persista dados com inteligência

Use `${CLAUDE_PLUGIN_DATA}` para dados que precisam sobreviver a atualizações da skill. Templates e scripts ficam no diretório da skill.

### Inclua scripts reutilizáveis

Scripts auxiliares mudam a dinâmica. Com scripts, o Claude se concentra em **composição** — decidir o que fazer e em que ordem — em vez de reimplementar boilerplate.

### Hooks condicionais: potência quando precisa, silêncio quando não

Hooks que rodam o tempo todo são irritantes. A solução são hooks que só ativam quando a skill é invocada:
- **/careful:** ativa um hook que bloqueia comandos destrutivos durante a sessão
- **/freeze:** bloqueia edições fora de um diretório específico

## Distribuição: do Repositório ao Marketplace

**Caminho 1 — Commit no repositório:** `.claude/skills/` no repositório do projeto. Versioned alongside code. Best for small teams.

**Caminho 2 — Plugin no marketplace:** Empacote a skill como parte de um plugin Claude Code. Best for generic, multi-project skills.

## Composição: Skills que Referenciam Skills

Uma skill pode referenciar outra pelo nome. Não há tooling formal ainda (sem package.json de skills), mas funciona por convenção.

## Medindo Adoção

Use hooks de PreToolUse para logar quando uma skill é invocada. Métricas: quais são mais usadas, quais estão abandonadas, quais são invocadas mas não completam o fluxo.

## O Efeito Opus 4.7: Por Que Skills Acabam de Se Tornar 10x Mais Importantes

Em 16 de abril de 2026, a Anthropic lançou o Claude Opus 4.7. Mudanças relevantes para skills:

### O modelo que pensa antes de agir
"4.7 pensa mais e age menos." Número de tool calls por tarefa caiu. Taxa de erros em ferramentas caiu para um terço. O Claude agora absorve o contexto da skill, planeja, e só então age.

### Auto-verificação nativa
O modelo escreve testes, roda, corrige falhas e só então reporta o resultado — sem que você peça. Skills de verificação de produto ficam muito mais poderosas.

### Memória de filesystem turbinada
Opus 4.7 é nativamente melhor em usar memória baseada em filesystem. Skills que mantêm estado (logs de standups, histórico de deploys) funcionam dramaticamente melhor.

### Interpretação literal
O 4.7 interpreta instruções de forma mais literal. Descriptions vagas resultam em skills que nunca são invocadas. Gotchas precisam ser ainda mais explícitos.

### Task budgets (beta)
Capacidade de definir um orçamento de tokens para um loop agente completo. Skills críticas em xhigh; skills de rotina em high.

### Coordenação multi-agente
Melhorias na orquestração de workstreams paralelos. Mas o 4.7 é mais conservador em disparar sub-agentes — só faz quando explicitamente instruído.

### Benchmark deltas (Opus 4.7 vs 4.6)

| Métrica | Opus 4.6 | Opus 4.7 | Delta |
|---|---|---|---|
| CursorBench | 58% | 70% | +12pp |
| Rakuten-SWE-Bench (produção) | baseline | 3x resolução | +200% |
| Erros de tool calls (Notion Agent) | baseline | 1/3 dos erros | -66% |
| Visual acuity (XBOW) | 54.5% | 98.5% | +44pp |
| Factory Droids (tarefas complexas) | baseline | +10-15% | +10-15% |

### Breaking changes do Opus 4.7 que afetam skills
1. **Parâmetros de sampling removidos:** temperature, top_p, top_k retornam erro 400
2. **Tokenizer novo:** inputs de texto consomem 1.0x–1.35x mais tokens; imagens saltam de ~1.600 para ~4.784 tokens
3. **Prefill bloqueado:** assistant message prefilling retorna erro 400

## Por Onde Começar

1. Identifique uma tarefa que você explica pro Claude repetidamente
2. Crie uma skill mínima com um único gotcha
3. Use a skill por uma semana e adicione gotchas conforme aparecem
4. Evolua para pastas com scripts e referências quando a complexidade justificar
5. Compartilhe com o time quando a skill estiver estável

---

*Este artigo foi inspirado pelo guia original de Mario Tort, engenheiro da Anthropic. As ideias centrais sobre skills são dele. A interpretação, os exemplos adicionais, a análise do Opus 4.7 e as opiniões sobre o futuro são do autor (Eric Luque).*
