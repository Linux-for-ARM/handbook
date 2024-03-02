#!/bin/env python
# Скрипт для генерации файла wget-list

import toml
from pathlib import Path

WGET_LST_PTH = Path("../wget-list")
PKG_IDX_PTH = Path("../packages.toml")

pkg_idx = toml.load(PKG_IDX_PTH)['package']

for pkg in pkg_idx.keys():
    if pkg_idx[pkg].get('display') is not None:
        continue
    url = pkg_idx[pkg]['download']
    with open(WGET_LST_PTH, 'a') as f:
        f.write(f"{url}\n")
