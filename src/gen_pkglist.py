#!/bin/env python
# Скрипт для генерации страницы со списком пакетов

import toml

PKGS_MD = "../md/pkgs.md" # Markdown-страница со списком пакетов
PKGS_TOML = "../packages.toml" # Файл со списком пакетов

def get_md_content(pkg: str, packages: dict) -> str:
    return f"## {pkg}-{packages[pkg]['version']}\n{packages[pkg]['description']}\n\
- Домашняя страница: <{packages[pkg]['home_page']}>\n\
- Скачать: <{packages[pkg]['download']}>\n\
- MD5 сумма: `{packages[pkg]['md5']}`\n"

packages: dict = toml.load(PKGS_TOML)["package"]
s = ""

keys = list(packages.keys())
keys.sort()

# for pkg in packages.keys():
for pkg in keys:
    if packages[pkg].get('display') is None:
        s = f"{s}{get_md_content(pkg, packages)}"

with open(PKGS_MD, 'w') as f:
    f.write(s)
