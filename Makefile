all:
	mdbook build

pdf: all
	cp -v ./book/pdf/output.pdf ./
