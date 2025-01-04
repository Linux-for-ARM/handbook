#!/bin/env python
# Скрипт для генерации файла wget-list

import toml
from pathlib import Path

WGET_LST_PTH = Path("../wget-list")
PKG_IDX_PTH = Path("../packages.toml")

pkg_idx = toml.load(PKG_IDX_PTH)['package']
pkg_urls = ""

for pkg in pkg_idx.keys():
    if pkg_idx[pkg].get('display') is not None:
        continue
    url = pkg_idx[pkg]['download']
    pkg_urls = f"{pkg_urls}{url}\n"

pkg_urls.strip()
with open(WGET_LST_PTH, 'w') as f:
    f.write(f"{pkg_urls}\n")
