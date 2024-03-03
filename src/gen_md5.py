#!/bin/env python
# Скрипт для генерации файла md5sums

import toml
from pathlib import Path

MD5SUMS_PTH = Path("../md5sums")
PKG_IDX_PTH = Path("../packages.toml")

pkg_idx = toml.load(PKG_IDX_PTH)['package']
s = ""

for pkg in pkg_idx.keys():
    if pkg_idx[pkg].get('display') is not None:
        continue
    url = pkg_idx[pkg]['download']
    md5 = pkg_idx[pkg]['md5']

    file = url.rsplit('/')[-1]

    s = f"{s}{md5}  {file}\n"

with open(MD5SUMS_PTH, 'w') as f:
    f.write(s)
