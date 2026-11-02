# Delta · Template de repositório

![Template GitHub](https://img.shields.io/badge/GitHub-Template-181717?logo=github&logoColor=white)
![Automação de PR](https://img.shields.io/badge/Automação-workflow%20compartilhado-2088FF?logo=githubactions&logoColor=white)
![Stack](https://img.shields.io/badge/Stack-definida%20por%20projeto-lightgrey)

Comece um repositório Delta com a convenção de Pull Requests da organização já conectada, sem escolher antecipadamente a linguagem ou o runtime da aplicação. Este template fornece os arquivos iniciais de governança; cada novo projeto define sua própria estrutura, dependências e testes.

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
| `.gitignore` | Base para ignorar credenciais, ambientes locais, builds e saídas comuns de várias linguagens. Ajuste-a ao stack real do projeto. |
| `LICENSE` | Ponto de partida de licenciamento. Confirme se os termos servem para o novo repositório antes de publicar ou redistribuir código. |
| `.github/workflows/trigger_actions.yml` | Conecta Pull Requests às verificações compartilhadas da organização. |
| `README.md` | Guia de uso do próprio template; substitua pelo README específico do novo projeto após criá-lo. |

Este repositório não contém aplicação, runtime, arquivo de dependências, Dockerfile ou suíte de testes de produto. Sua automação compartilhada verifica governança da PR, não o comportamento do código que será criado a partir dele.

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

O `.gitignore` reúne exclusões comuns para arquivos de ambiente e credenciais, caches, artefatos de build e arquivos de IDE. Revise-o ao adotar tecnologias específicas e preserve as regras que impedem versionar segredos.

## Começar um repositório

1. No GitHub, use **Use this template** para criar um novo repositório.
2. Escolha o nome, a visibilidade e a organização apropriados ao projeto.
3. Defina a stack a partir do código e dos requisitos do novo projeto; adicione manifests e instruções de instalação reais.
4. Substitua este README por documentação de propósito, arquitetura, configuração, execução e testes do projeto criado.
5. Confira o arquivo `LICENSE` e adapte o `.gitignore` ao stack escolhido.
6. Mantenha `trigger_actions.yml` se o repositório deve continuar usando as verificações comuns da organização. O workflow chama o repositório `.github` e precisa do segredo de automação configurado conforme a governança do time.

Não assuma que o template instalou ferramentas, criou uma branch ou publicou o repositório. Essas ações dependem de como o novo repositório é criado e configurado.

## Testes e CI

Este template não inclui testes de aplicação. O workflow de Pull Request conecta os checks de governança da organização, que verificam informações da PR e acionam o roteamento de revisores. Ele não substitui a suíte técnica.

Depois de criar o projeto, adicione testes adequados à stack real e um workflow de CI que instale dependências, execute esses testes e falhe quando houver erro. Documente aqui os comandos efetivamente disponíveis no repositório gerado.

## Containers e desenvolvimento local

O template não define um Dockerfile ou `docker-compose.yml` universal. Um projeto deve escolher a imagem base e as dependências de acordo com seu manifesto e seu runtime. Crie um Dockerfile quando o projeto precisar construir sua própria imagem; use Compose quando os testes ou o desenvolvimento precisarem de dependências auxiliares como banco de dados ou cache. Os dados de testes automatizados devem ser descartáveis.

## Contribuir

Consulte as [convenções de branches e commits](https://github.com/delta-app-ofc/delta-handbook/blob/main/DEVOPS/convencoes-desenvolvimento.md) e o [guia do processo de Pull Request](https://github.com/delta-app-ofc/delta-handbook/blob/main/DEVOPS/template-prs.md). Mantenha os arquivos de governança compatíveis com as automações compartilhadas da organização.
