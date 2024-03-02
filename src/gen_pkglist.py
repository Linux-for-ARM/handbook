#!/bin/env python
# Скрипт для генерации страницы со списком пакетов

import toml

PKGS_MD = "../md/pkgs.md" # Markdown-страница со списком пакетов
PKGS_TOML = "../packages.toml" # Файл со списком пакетов

def get_md_content(pkg: str, packages: dict) -> str:
    return f"- **{pkg} ({packages[pkg]['version']})** - {packages[pkg]['description']}<br>\
- Домашняя страница: [{packages[pkg]['home_page']}]({packages[pkg]['home_page']})<br>\
- Скачать: [{packages[pkg]['download']}]({packages[pkg]['download']})<br>\
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
