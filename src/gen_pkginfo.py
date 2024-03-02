#!/bin/env python
# Скрипт для генерации Markdown-страниц с описанием пакетов

import os
import toml
from pathlib import Path


PKG_INDEX = "../pkg_info.toml"
PKGS_ALL = "../packages.toml"
DIRS = {
	"cross-compiler": Path("../md/cross-compiler/pkgs"),
	"base": Path("../md/base/pkgs"),
	"kernel": Path("../md/kernel/pkgs"),
	"bootloader": Path("../md/bootloader/pkgs")
}

packages = toml.load(PKGS_ALL)['package']
pkg_index = toml.load(PKG_INDEX)['package']
#print(pkg_index)

for d in DIRS.values():
	if not d.exists():
		print(f"[gen_pkginfo] create '{d}' dir...")
		try:
			os.makedirs(d)
		except:
			# да, я знаю, что все классы исключений обрабатывать - не есть хорошо.
			# но мне лень указывать конкретное исключение
			print(f"[gen_pkginfo] error!")

def get_md_str(pkg_name: str, pkg_lst: dict, pkg_idx: dict) -> str:
	return f"> {pkg_idx[pkg_name]['description']}\n\
> - **Версия:** {pkg_lst[pkg_name]['version']}\n\
> - **Домашняя страница:** [{pkg_lst[pkg_name]['home_page']}]({pkg_lst[pkg_name]['home_page']})\n\
> - **Ссылка для загрузки:** [{pkg_lst[pkg_name]['download']}]({pkg_lst[pkg_name]['download']})\n\
> - **MD5-сумма:** `{pkg_lst[pkg_name]['md5']}`\n\
> - **ОВС:** {pkg_idx[pkg_name]['sbu']}\n"

def write_to_pkg_md(data: str, pkg_id: str, dir_pth: str):
	pth = DIRS[dir_pth].joinpath(f"{pkg_id}.md")

	with open(pth, 'w') as f:
		f.write(data)

for pkg in pkg_index.keys():
	print(f"write information about {pkg_index[pkg]['dir_pth']}/{pkg_index[pkg]['id']}...")

	data = get_md_str(pkg, packages, pkg_index)
	write_to_pkg_md(data, pkg_index[pkg]['id'], pkg_index[pkg]['dir_pth'])
