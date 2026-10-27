"""Links relativos simples nos Markdown alterados. Nao acessa HTTP."""
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


def main():
    base = os.environ.get("BASE_SHA", "")
    args = (["git", "diff", "--name-only", "--diff-filter=ACM", base, "HEAD"]
            if base and set(base) != {"0"}
            else ["git", "show", "--pretty=format:", "--name-only", "HEAD"])
    names = subprocess.check_output(args).decode().splitlines()
    errors = []
    total = 0
    for name in names:
        path = Path(name)
        if path.suffix.lower() != ".md" or not path.is_file():
            continue
        total += 1
        text = path.read_text(encoding="utf-8-sig")
        # Subconjunto: links inline. Ignora blocos fenced e ancoras.
        fence = chr(96) * 3
        text = re.sub(r"(?ms)^\s*" + fence + r".*?^\s*" + fence + r"[^\n]*", "", text)
        for raw in re.findall(r"\]\((<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)", text):
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            relative = unquote(parsed.path)
            candidate = (Path.cwd() / relative.lstrip("/")
                         if relative.startswith("/")
                         else path.parent / relative)
            if not candidate.exists():
                errors.append(f"{name}: link local inexistente: {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK: links locais simples de {total} Markdown alterados; sem rede.")


if __name__ == "__main__":
    main()
