all:
	${HOME}/.cargo/bin/mdbook build

install-deps:
	sudo apt update
	sudo apt install rustc cargo -y --fix-missing
	cargo install mdbook mdbook-df mdbook-admonish

pdf: all
	cp -v ./book/pdf/output.pdf ./
