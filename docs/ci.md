# CI do template

Em pull requests e por acionamento manual, o workflow valida a sintaxe YAML dos workflows, a presença de `LICENSE` e `.gitignore` não vazios e algumas regras essenciais de ignore (`.env`, `node_modules`, `target` e a exceção `.env.example`).

Para repetir localmente, com Ruby e Git instalados, execute na raiz:

```sh
ruby -e 'require "psych"; Dir.glob(".github/workflows/*.{yml,yaml}").each { |f| Psych.parse_file(f); puts "OK: #{f}" }'
test -s LICENSE && test -s .gitignore
git check-ignore --no-index -q .env && git check-ignore --no-index -q node_modules/exemplo && git check-ignore --no-index -q target/exemplo
! git check-ignore --no-index -q .env.example
```

A análise YAML verifica sintaxe, não a semântica do GitHub Actions. Repositórios criados a partir deste template devem adaptar o CI à sua própria stack e aos seus testes.
