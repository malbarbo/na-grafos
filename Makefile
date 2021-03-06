.PHONY: default all pdf handout tex clean

SHELL=bash
DEST=target
DEST_PDF=$(DEST)/pdfs
DEST_PDF_HANDOUT=$(DEST)/pdfs/handout
DEST_ZIP=$(DEST)/zips
DEST_TEX=$(DEST)/tex
IGNORAR=README.md
NA=$(patsubst %/,%,$(dir $(shell find * -wholename '*/notas-de-aula.md')))
NA_PDF=$(addprefix $(DEST_PDF)/, $(addsuffix .pdf, $(NA)))
NA_PDF_HANDOUT=$(addprefix $(DEST_PDF_HANDOUT)/, $(addsuffix .pdf, $(NA)))
EX=$(patsubst %/,%,$(dir $(shell find * -wholename '*/exercicios.md')))
EX_PDF=$(addprefix $(DEST_PDF)/, $(addsuffix -exercicios.pdf, $(EX)))
EXS=$(patsubst %/,%,$(dir $(shell find * -type d -wholename '*/exemplos')))
EXS_ZIP=$(addprefix $(DEST_ZIP)/, $(addsuffix -exemplos.zip, $(EXS)))
TECTONIC=$(DEST)/bin/tectonic
PANDOC=$(DEST)/bin/pandoc
PANDOC_VERSION=2.11.3.2
PANDOC_CMD=$(PANDOC) \
		-V mathspec \
		--pdf-engine=$(CURDIR)/$(TECTONIC) \
		--metadata-file ../metadata.yml \
		--template ../templates/default.latex \
		--to beamer \
		--standalone

default:
	@echo Executando make em paralelo [$(shell nproc) tarefas]
	@make -s -j $(shell nproc) all

all: pdf handout ex zip

pdf: $(NA_PDF)

handout: $(NA_PDF_HANDOUT)

ex: $(EX_PDF)

zip: $(EXS_ZIP)

$(DEST_PDF)/%.pdf: %/notas-de-aula.md $(wildcard %/imagens/) templates/default.latex metadata.yml $(PANDOC) $(TECTONIC)
	@mkdir -p $(DEST_PDF)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
		-o ../$@ notas-de-aula.md

$(DEST_PDF_HANDOUT)/%.pdf: %/notas-de-aula.md $(wildcard %/imagens/) templates/default.latex metadata.yml $(PANDOC) $(TECTONIC)
	@mkdir -p $(DEST_PDF_HANDOUT)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
		-V classoption:handout \
		-o ../$@ notas-de-aula.md

$(DEST_PDF)/%-exercicios.pdf: %/exercicios.md templates/default.latex metadata-ex.yml $(PANDOC) $(TECTONIC)
	@mkdir -p $(DEST_PDF)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
			--to latex \
			--metadata-file ../metadata-ex.yml \
			-V papersize=a4 \
			-V geometry='margin=1.5cm' \
			-V fontsize=11pt \
			-o ../$@ exercicios.md

$(DEST_ZIP)/%-exemplos.zip: %/exemplos/*
	@mkdir -p $(DEST_ZIP)
	@zip -o $@ -r $$(dirname $<)
	@touch $@

$(PANDOC):
	mkdir -p $(DEST)
	curl -L https://github.com/jgm/pandoc/releases/download/$(PANDOC_VERSION)/pandoc-$(PANDOC_VERSION)-linux-amd64.tar.gz | tar xz -C $(DEST) --strip-components=1

$(TECTONIC):
	mkdir -p $(DEST)/bin/
	curl -L  https://github.com/tectonic-typesetting/tectonic/releases/download/continuous/tectonic-latest-x86_64-unknown-linux-musl.tar.gz | tar xz -C $(DEST)/bin/

clean:
	@echo Removendo $(DEST_PDF)
	@rm -rf $(DEST_PDF)
