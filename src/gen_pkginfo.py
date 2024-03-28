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
# print(pkg_index)

for d in DIRS.values():
	if not d.exists():
		print(f"[gen_pkginfo] create '{d}' dir...")
		try:
			os.makedirs(d)
		except:
			# да, я знаю, что все классы исключений обрабатывать - не есть хорошо.
			# но мне лень указывать конкретное исключение
			print(f"[gen_pkginfo] error!")

# def get_md_str(pkg_name: str, pkg_lst: dict, pkg_idx: dict) -> str:
# 	description = ""
# 	if pkg_idx.get("description"):
# 		description = pkg_idx["description"]
# 	else:
# 		description = pkg_lst["description"]

# 	return f"> {description}\n\
# > - **Версия:** {pkg_lst[pkg]['version']}\n\
# > - **ОВС:** {pkg_idx[pkg_name]['sbu']}\n"

def get_md_str(pkg: dict, pkg_lst: dict):
	descr = ""
	if pkg.get("description"):
		descr = pkg["description"]
	else:
		descr = pkg_lst[pkg["package"]]["description"]

	return f"> {descr}\n\
> - **Версия:** {pkg_lst[pkg['package']]['version']}\n\
> - **Домашняя страница:** <{pkg_lst[pkg['package']]['home_page']}>\n\
> - **Время сборки:** {pkg['sbu']} ОВС\n"

def write_to_pkg_md(data: str, pkg_id: str, dir_pth: str):
	pth = DIRS[dir_pth].joinpath(f"{pkg_id}.md")

	with open(pth, 'w') as f:
		f.write(data)

for pkg in pkg_index:
	print(f"write information about {pkg['dir_pth']}/{pkg['id']}...")

	data = get_md_str(pkg, packages)
	write_to_pkg_md(data, pkg['id'], pkg['dir_pth'])
