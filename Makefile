all:
	${HOME}/.cargo/bin/mdbook build

install-deps:
	sudo apt-get install rustc cargo -y
	cargo install mdbook mdbook-df mdbook-admonish

pdf: all
	cp -v ./book/pdf/output.pdf ./
