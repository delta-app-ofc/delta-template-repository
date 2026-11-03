# Delta · Template de repositório

![Template GitHub](https://img.shields.io/badge/GitHub-Template-181717?logo=github&logoColor=white)
![Automação de PR](https://img.shields.io/badge/Automação-workflow%20compartilhado-2088FF?logo=githubactions&logoColor=white)
![Stack](https://img.shields.io/badge/Stack-definida%20por%20projeto-lightgrey)

Template inicial para criar repositórios Delta. Inclui os arquivos de governança compartilhada da organização e uma base de `.gitignore`; cada projeto define sua stack, estrutura e comandos.

**Tags:** `template` · `github` · `governança` · `pull-request` · `gitignore` · `delta`

## Sumário

- [Visão geral](#visão-geral)
- [O que vem no template](#o-que-vem-no-template)
- [Começar um repositório](#começar-um-repositório)
- [Testes e CI](#testes-e-ci)
- [Containers e desenvolvimento local](#containers-e-desenvolvimento-local)
- [Contribuir](#contribuir)

## Visão geral

| Arquivo | Papel |
|---|---|
| `.gitignore` | Regras iniciais para credenciais, ambientes locais, builds e saídas comuns de várias linguagens. |
| `LICENSE` | Base de licenciamento para o novo repositório. |
| `.github/workflows/trigger_actions.yml` | Conecta Pull Requests às verificações compartilhadas da organização. |
| `README.md` | Guia deste template; substitua-o pela documentação do novo projeto. |

## O que vem no template

```text
delta-template-repository/
├── .github/
│   └── workflows/
│       └── trigger_actions.yml
├── .gitignore
├── LICENSE
└── README.md
```

O `.gitignore` reúne exclusões para arquivos de ambiente e credenciais, caches, artefatos de build e arquivos de IDE. Ajuste as regras ao stack do projeto e mantenha as credenciais fora do controle de versão.

## Começar um repositório

1. No GitHub, use **Use this template** para criar um repositório.
2. Escolha o nome, a visibilidade e a organização do projeto.
3. Defina a stack e adicione os manifests e instruções de instalação do projeto.
4. Substitua este README por documentação de propósito, arquitetura, configuração, execução e testes.
5. Revise o arquivo `LICENSE` e adapte o `.gitignore` às tecnologias escolhidas.
6. Mantenha `trigger_actions.yml` para conectar o repositório às verificações compartilhadas. Configure o segredo de automação conforme as regras da organização.

## Testes e CI

`trigger_actions.yml` encaminha Pull Requests aos checks de governança da organização e ao roteamento de revisores. Ao criar o projeto, adicione testes para a stack escolhida e configure a CI para instalar dependências, executar a suíte e registrar falhas.

## Containers e desenvolvimento local

Escolha `Dockerfile` e `docker-compose.yml` de acordo com o runtime e as dependências do projeto. Use uma imagem própria quando precisar construir a aplicação; Compose ajuda a iniciar serviços auxiliares, como bancos e caches, durante o desenvolvimento ou os testes. Mantenha os dados de teste descartáveis.

## Contribuir

Consulte as [convenções de branches e commits](https://github.com/delta-app-ofc/delta-handbook/blob/main/DEVOPS/convencoes-desenvolvimento.md) e o [guia do processo de Pull Request](https://github.com/delta-app-ofc/delta-handbook/blob/main/DEVOPS/template-prs.md). Mantenha os arquivos de governança compatíveis com as automações compartilhadas da organização.
